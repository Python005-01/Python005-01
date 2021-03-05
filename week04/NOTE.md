django orm插入语句方法

1.进入shell终端

python manager.py shell

2.导入库

from dpbooks.models import *

import doupan

3.批量添加条目

alist = doupan.inadd_db()

for i in alist:

    dpbooks.objects.create(short_comments=i[0], stars=i[1], comment_time=i[2])
