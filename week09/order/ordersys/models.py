from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# 商品
class goods(models.Model):
    goodsname = models.CharField(max_length=50, verbose_name='商品名')
    amount = models.IntegerField(verbose_name='数量', default=10)
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


# 订单
class goodorders(models.Model):
    order_choices = ((1, True),
                     (2, False))
    order_id = models.IntegerField(verbose_name="订单编号")
    # 用户外键
    userowner = models.ForeignKey('auth.User', related_name='orderuser', on_delete=models.CASCADE)
    # 商品外键
    goodowner = models.ForeignKey(goods, related_name='ordergood', on_delete=models.CASCADE, verbose_name="下单商品")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    ordersname = models.CharField(max_length=50, verbose_name='订单')
    # 订单状态True False
    orderactive = models.BooleanField(choices=order_choices, verbose_name='订单状态', default=True)
