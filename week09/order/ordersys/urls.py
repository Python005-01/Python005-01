from django.conf.urls import url, include
from ordersys import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'users', views.UserList)
router.register(r'goods', views.GoodList)
router.register(r'orders', views.OrderList)
urlpatterns = [
    # jwt token
    url(r'^jwt_auth/', obtain_jwt_token),
    # token
    url(r'^tk_auth/', obtain_auth_token),
    url(r'^orders/create/$', views.CrOrder.as_view()),
    url(r'^', include(router.urls)),
    url(r'^$', views.api_root),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^goods/(?P<pk>[0-9]+)/$', views.GoodDetail.as_view(), name='goods-detail'),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(), name='orders-detail'),
    url(r'^orders/(?P<pk>[0-9]+)/cancel/$', views.OrdercancelDetail.as_view(), name='orderscancel-detail')
]
