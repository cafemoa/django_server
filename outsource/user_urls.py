from outsource.user_views import *
from django.conf.urls import url,include
from rest_framework import routers


urlpatterns = [
    url(r'^social-api-auth/', ObtainJSONWebToken.as_view()),
    url(r'^social-api-signup/', SocialSignUp.as_view({'post':'create'})),
    url(r'^rest-api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user-manage/',UserManageViewSet.as_view({'get': 'list','put':'update',
                                                    'post':'create','delete' : 'destroy'})),

    url(r'^get_cafe_beverage/(?P<cafe_pk>\d+)', CafeBeverageList.as_view({'get':'retrieve'})),
    url(r'^get_cafes/',CafeBeverageList.as_view({'get':'list'})),
    url(r'^get_beverage_option/(?P<pk>\d+)',BeverageOption.as_view()),

    url(r'^get_favorite_cafe/',UsersFavoriteCafe.as_view({'get':'list'})),
    url(r'^add_favorite_cafe/(?P<cafe_pk>\d+)',UsersFavoriteCafe.as_view({'post': 'update'})),

    url(r'^get_all_coupons/',CouponViewSet.as_view({'get':'list'})),
    url(r'^get_one_coupon/(?P<pk>\d+)',CouponViewSet.as_view({'get':'retrieve'})),

    url(r'^order_beverage/(?P<cafe_pk>\d+)',OrderViewSet.as_view({'post':'create'})),
    url(r'^recent_payment_list_by_order/(?P<coupon_pk>\d+)',OrderViewSet.as_view({'get':'retrieve'})),
    url(r'^recent_payment_list_by_id/(?P<term_year>\d+)/(?P<term_month>\d+)',OrderViewSet.as_view({'get':'list'})),
    url(r'^ready_payment/(?P<cafe_pk>\d+)', ReadyPayment.as_view()),

    url(r'^get_cafe_event/(?P<cafe_pk>\d+)',EventViewSet.as_view({'get':'retrieve'})),
    url(r'^get_events/',EventViewSet.as_view({'get':'list'})),

    url(r'^get_alerts/', AlertViewSet.as_view({'get': 'list'})),
    url(r'^email_check/', EmailCheck.as_view()),
]
