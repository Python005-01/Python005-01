from rest_framework import serializers
from .models import goods,goodorders
from django.contrib.auth.models import User

# 用户序列化
class UserSerializer(serializers.HyperlinkedModelSerializer):
    orderuser = serializers.HyperlinkedRelatedField(many=True, view_name='orders-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'orderuser')
# 商品序列化
class GoodSerializer(serializers.HyperlinkedModelSerializer):
    ordergood = serializers.HyperlinkedRelatedField(many=True, view_name='orders-detail', read_only=True)
    class Meta:
        model = goods
        fields = ('url', 'id', 'goodsname', 'ordergood', 'amount', 'createtime')
# 订单序列化
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    userowner = serializers.ReadOnlyField(source='userowner.username')
    orderactive = serializers.BooleanField()
    class Meta:
        model = goodorders
        fields = ('url', 'id', 'order_id', 'userowner', 'goodowner','createtime','ordersname','orderactive')