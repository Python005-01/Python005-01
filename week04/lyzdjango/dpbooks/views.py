from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from dpbooks.models import dpbooks

class books(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        data={}
        # 标题内容
        data['title'] = "星际穿越"
        # 表单内容
        queryset = dpbooks.objects.all()
        data['ulist'] = list(queryset.values("id", "short_comments", "stars", "comment_time").filter\
                                 (stars__gte = 3))
        # 搜索功能
        if request.GET.get("q"):

            if queryset.values("id", "short_comments", "stars", "comment_time").filter\
                        (short_comments__contains = request.GET.get("q"), stars__gte = 3):
                data['ulist'] = queryset.values("id", "short_comments", "stars", "comment_time").filter\
                    (short_comments__contains = request.GET.get("q"),  stars__gte = 3)
            else:
                data['ulist'] =""
        return self.render_to_response(data)