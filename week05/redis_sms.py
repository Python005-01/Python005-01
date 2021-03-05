import redis
import time

# 连接redis
r = redis.Redis(host='192.168.16.172', port=6379, password='test123')

"""
telephone_number 手机号
content 消息内容
key hashkey键值
start_time 计时初始时间
"""
def sendsms(telephone_number, content, key='sms_telephone', start_time=time.time()):
    # 判断hash key sms_telephone是否存在
    # 不存在建立sms_telephone的 key值 {手机号:初始时间}
    if not r.hexists(key, telephone_number):
        r.hset(key, telephone_number, start_time)

    # 如果当前时间减去hash key值 {手机号:初始时间}的初始时间大于60 就重新设置时间
    if time.time() - float(r.hget(key, telephone_number)) > 60:
        r.hset(key, telephone_number, start_time)

    # 如果当前时间减去hash key值 {手机号:初始时间}的初始时间小于等于60，就建立执行下面建立记录次数key值
    if time.time() - float(r.hget(key, telephone_number)) <= 60:
        # 判断key是否存在
        if not r.exists(telephone_number):
            r.set(telephone_number, 1, ex=60)
            print('发送成功')
            print(content)
        # 超过5次
        elif int(r.get(telephone_number)) >= 5:
            print('一分钟只能发送5次，请等待一分钟')
        # 自增加1
        else:
            r.incr(telephone_number)
            print('发送成功')

    print('秒数: ', int(time.time()-float(r.hget(key, telephone_number))))
    print('发送次数：', r.get(telephone_number))

sendsms(13078781994, 'helloword')
