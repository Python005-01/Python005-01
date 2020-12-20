from django.db import models

# Create your models here.
class dpbooks(models.Model):
    # 短评
    short_comments = models.TextField()
    # 星级
    stars = models.IntegerField()
    # 评论时间
    comment_time = models.DateTimeField()




