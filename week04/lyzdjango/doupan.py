import os
import sys

import requests
from lxml import etree
import re


class douban_dp():

    def __init__(self, myurl):
        self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'

        self.header = {'user-agent': self.ua,
                       'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
                       }
        self.response = requests.get(myurl, headers=self.header)
        self.selector = etree.HTML(self.response.text)


    def get_dplist_pl(self):
        """获取豆瓣短评内容"""
        list_dp_pl = self.selector.xpath('//div[@class="comment-item "]/div[@class="comment"]/p/span[1]/text()')
        return list_dp_pl

    def get_dplist_xj(self):
        """获取豆瓣星级内容"""
        list_dp_xj = self.selector.xpath('//div[@class="comment-item "]/div[@class="comment"]/h3/span[2]/span[2]/@class')
        return list_dp_xj

    def get_dplist_pl_time(self):
        """获取豆瓣星评论时间"""
        list_dp_pl_time = self.selector.xpath('//div[@class="comment-item "]/div[@class="comment"]/h3/span[2]/span[@class="comment-time "]/text()')
        return list_dp_pl_time

    def get_dptitle(self):
        """获取豆瓣短评的标题"""
        dptitle = self.selector.xpath('//div[@id="content"]/h1/text()')
        tit = str(dptitle).replace(" 短评", "")
        return tit
    def get_all(self):
        """获取短评,星级,评论时间内容"""

        # 短评
        pl = self.get_dplist_pl()
        # 星级
        xj = self.get_dplist_xj()
        # 评论时间
        pltime = self.get_dplist_pl_time()

        # 整合短评,星级,评论时间内容
        jh = tuple(zip(pl, xj, pltime))

        # 短评,星级,评论时间内容字串处理
        jh_list = []
        for a, b, c in jh:
            b = re.sub('[a-z]|[A-Z]|\s', '', b)
            if b == "-":
                b = "0"
            else:
                b = b.replace('0','')
            c = c.strip()
            jh_list.append((a, b, c))
        # 返回短评,星级,评论时间内容
        return jh_list

# 把数据添加到数据库函数
def inadd_db():

    """
    django orm插入语句方法

    1.
    #进入shell终端
    python manager.py shell
    2.
    #导入库
    from dpbooks.models import *
    import doupan
    3.
    #批量添加条目
    alist = doupan.inadd_db()
    for i in alist:
        dpbooks.objects.create(short_comments=i[0], stars=i[1], comment_time=i[2])
    """

    mylist = []
    for num in range(0, 100, 20):
        myurl2 = f'https://movie.douban.com/subject/1889243/comments?start={num}&limit=20&status=P&sort=new_score'
        dp = douban_dp(myurl2)
        mylist.extend(dp.get_all())
    return mylist


if __name__ == '__main__':
    myurl1 = f'https://movie.douban.com/subject/1889243/comments?limit=0&status=P&sort=new_score'
    dp = douban_dp(myurl1)
    dp.get_dptitle()
    mylist = []

    for num in range(0, 200, 20):
        myurl2 = f'https://movie.douban.com/subject/1889243/comments?start={num}&limit=20&status=P&sort=new_score'
        dp = douban_dp(myurl2)
        mylist += dp.get_all()
    print(mylist)
    for i in mylist:
        print(i)




