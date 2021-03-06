from rest_framework import serializers
from outsource.models import *
import jwt

from calendar import timegm
from datetime import datetime, timedelta

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import get_username_field, PasswordField,Serializer

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyDevice
        fields = ('dev_id','reg_id','name','is_active')

class CafeSerializerForCafe(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cafe
        fields = ('cafe_image', 'locationString', 'name', 'pk','is_open','tag')

class CafeSerializerForUser(serializers.HyperlinkedModelSerializer):
    coupon_num = serializers.SerializerMethodField('GetCouponNum')

    def GetCouponNum(self, instance):
        coupon=Coupon.objects.filter(user_id=self.context['request'].user.pk, cafe_id=instance.pk)
        if coupon.count()==0:
            return 0
        else :
            coupon=coupon.first()
        return coupon.coupon_progress

    class Meta:
        model = Cafe
        fields = ('cafe_image','locationString', 'name', 'pk','is_open','tag', 'min_time','coupon_price','coupon_num')

class CouponSerializer(serializers.HyperlinkedModelSerializer):
    cafe = CafeSerializerForCafe()
    class Meta:
        model=Coupon
        fields = ('pk', 'coupon_progress', 'cafe')



class OptionSelectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=OptionSelection
        fields = ('content','pk','add_price')

class BeverageOptionSerializer(serializers.HyperlinkedModelSerializer):
    selections=OptionSelectionSerializer(many=True)
    class Meta:
        model=BeverageOption
        fields = ('content', 'pk', 'selections','one_selector')


class BeverageOrderOptionSerializer(serializers.HyperlinkedModelSerializer):
    options=OptionSelectionSerializer(many=True)
    beverage_name = serializers.SerializerMethodField('GetBeverageName')
    def GetBeverageName(self, instance):
        return instance.beverage.name
    class Meta:
        model = BeverageOrderOption
        fields = ('beverage_id', 'beverage_name', 'size','shot_num','options','amount')

class BeverageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Beverage
        fields = ('name', 'image', 'price', 'pk','type','is_best','have_shot','add_shot_price')

class CafeFullSerializer(serializers.HyperlinkedModelSerializer):
    beverages = BeverageSerializer(many=True)
    class Meta:
        model = Cafe
        fields = ('cafe_image','locationString', 'name', 'pk','beverages','is_open', 'min_time')

class UserManageSerializer(serializers.HyperlinkedModelSerializer):
    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.phone_number = validated_data.get('phone_number',instance.phone_number)
        instance.birth_year = validated_data.get('birth',instance.birth)
        instance.gender = validated_data.get('gender',instance.gender)

        if not validated_data.get('password') == None :
            instance.set_password(validated_data.get('password', instance.password))

        instance.save()
        return instance
    class Meta:
        model = User
        fields = ('username','birth', 'password',
                  'gender','name','phone_number','profile_picture')
        extra_kwargs = {
            'security_question': {'write_only': True},
            'security_question_answer': {'write_only': True},
            'password': {'write_only': True}
        }

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    cafe_name=serializers.SerializerMethodField('GetOrderCafeName')
    cafe_location = serializers.SerializerMethodField('GetOrderCafeLocation')
    menu_name=serializers.SerializerMethodField('GetOrderMenuName')
    remain_order=serializers.SerializerMethodField('RemainOrder')
    def RemainOrder(self, instance):
        return instance.cafe.orders.filter(state__lt=2).count()
    '''
    get_time = serializers.SerializerMethodField('GetTime')

    def GetTime(self, instance):
        deltaTime=(int)(datetime.now().strftime('%s'))-(int)(instance.order_time.strftime('%s'))
        get_time=instance.get_time*60-deltaTime
        if get_time<0:
            return 0

        return int(get_time/60)
    '''

    def GetOrderCafeName(self, instance):
        return instance.cafe.name

    def GetOrderCafeLocation(self, instance):
        return instance.cafe.locationString

    def GetOrderMenuName(self, instance):
        if instance.beverages.count()>1 :
            return  instance.beverages.first().beverage.name + " 및"+str(instance.beverages.count()-1)+" 잔"
        else :
            if instance.beverages.count()==0 :
                return instance.cafe.name

            return instance.beverages.first().beverage.name


    orderer_username = serializers.SerializerMethodField('GetOrdererUserName')
    beverages = BeverageOrderOptionSerializer(many=True,read_only=True)

    def GetOrdererUserName(self, instance):
        return instance.orderer.name

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    class Meta:
        model=Order
        fields = ( 'pk', 'order_time','payment_type', 'orderer_username', 'beverages', 'amount_price', 'order_num', 'cafe_name','cafe_location','menu_name','state','remain_order')
        read_only_fields = ('order_time','orderer_username', 'order_num', 'cafe_name','cafe_location','menu_name')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    beverages = BeverageSerializer(many=True,read_only=True)
    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    class Meta:
        model = Event
        fields = ('pk','event_type','price', 'to_time', 'from_time','beverages')

class AlertSerializer(serializers.HyperlinkedModelSerializer):
    cafe_name=serializers.SerializerMethodField('GetCafeName')
    def GetCafeName(self, instance):
        return instance.cafe.locationString+" "+instance.cafe.name

    def create(self,validated_data):
        return Alert.objects.create(**validated_data)

    class Meta:
        model=Alert
        fields=('cafe_name', 'content', 'is_event', 'alert_life')

        extra_kwargs = {
            'alert_life': {'write_only': True},
        }

baseUser = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

class JSONWebTokenSerializer(Serializer):
    def __init__(self, *args, **kwargs):
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)
        self.fields['access_token'] = serializers.CharField()

    @property
    def username_field(self):
        return get_username_field()

    def validate(self, attrs):
        token=attrs.get('access_token')
        user=SocialUser.objects.get(token=token).user

        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise serializers.ValidationError(msg)

            payload = jwt_payload_handler(user)

            return {
                'token': jwt_encode_handler(payload),
                'user': user
            }
        else:
            msg = _('Unable to log in with provided credentials.')
            raise serializers.ValidationError(msg)