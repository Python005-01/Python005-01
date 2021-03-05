from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import Http404
from rest_framework import generics
from .models import goods, goodorders
from .serializers import GoodSerializer, OrderSerializer, UserSerializer
from rest_framework import permissions
from .permissions import Ispermission_post_w_get_r, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


#page分页
#用户分页
class UserPagination(PageNumberPagination):
    #每页显示多少个
    page_size = 5
    #默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    #最大页数不超过10
    max_page_size = 10
    #获取页码数的
    page_query_param = "page"

# 订单分页
class OrderPagination(PageNumberPagination):
    #每页显示多少个
    page_size = 3
    #默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    #最大页数不超过5
    max_page_size = 5
    #获取页码数的
    page_query_param = "page"

# 用户列表
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = UserPagination

# 订单列表
class OrderList(viewsets.ModelViewSet):
    queryset = goodorders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    # 分页
    pagination_class = OrderPagination

    def perform_create(self, serializer):
        serializer.save(userowner=self.request.user)

# 创建订单/order/create
class CrOrder(generics.ListCreateAPIView):
    queryset = goodorders.objects.all()
    serializer_class = OrderSerializer
    # 分页
    pagination_class = OrderPagination
    # 获取token curl -X POST -d "username=root&password=123456" http://127.0.0.1:8000/tk_auth/
    # 获取jwt token curl -X POST -d "username=root&password=123456" http://127.0.0.1:8000/jwt_auth/
    # Base认证,Token认证,JWT Token认证
    authentication_classes = (BasicAuthentication, TokenAuthentication, JSONWebTokenAuthentication)
    permission_classes = [permissions.IsAuthenticated, Ispermission_post_w_get_r]


    def perform_create(self, serializer):
        serializer.save(userowner=self.request.user)

# 商品列表
class GoodList(viewsets.ModelViewSet):
    queryset = goods.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# 用户详情
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# 订单详情
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = goodorders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# 商品详情
class GoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = goods.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# 取消商品GET请求
class OrdercancelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = goods.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            return goodorders.objects.get(pk=pk)
        except goodorders.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        # orm操作订单状态(orderactive)设置False
        goodorders.objects.filter(pk=pk).update(orderactive=False)
        goodorders.save
        # 获取序列化实例
        ordercancel= self.get_object(pk=pk)
        serializer = OrderSerializer(ordercancel, context={'request': request})

        return Response(serializer.data)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'goods': reverse('good-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format)
    })
#
