import redis
import random

class redis_video():

    def __init__(self):
        self.r = redis.Redis(host='192.168.16.172', port=6379, password='test123', decode_responses=True)
    # 返回计数统计
    def counter_video(self, vid):
        count = self.r.zscore('video_id', vid)
        #print(count)
        return count
    # 模拟播放id和计数初始值
    def set_key(self, vid):
        self.r.zadd("video_id", {vid:0})
    # 播放
    def play_video(self, vid):
        self.add_counter(vid)
    # 增加计数器
    def add_counter(self, vid):
        self.r.zincrby('video_id', 1, vid)

if __name__ == "__main__":
    rd = redis_video()

    # 模拟播放id和计数初始值
    #for i in range(1001, 1100):
    #    rd.set_key(i)
    #rd.play_video(1003)


    # 模拟播放数据
    #for i in range(0, 10000):
    #    rd.play_video(random.randint(1000, 1100))

    # 计数器返回
    for i in range(0, 10):
        vd_id = random.randint(1000, 1100)
        print(f"播放id {vd_id} :", int(rd.counter_video(vd_id)))