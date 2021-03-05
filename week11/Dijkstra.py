import threading
import time
import random
import queue

class DiningPhilosophers(threading.Thread):
    def __init__(self, philosopher_num, leftlock, rightlock,  operate_queue):
        super().__init__()
        # 哲学家的编号
        self.philosopher_num = philosopher_num
        # 左边叉子的锁
        self.leftlock = leftlock
        # 右边叉子的锁
        self.rightlock = rightlock
        self.operate_queue = operate_queue

    def run(self):
        left = self.leftlock.acquire()
        right = self.rightlock.acquire()
        if left and right:
            self.pickLeftFork()
            self.pickRightFork()
            self.eat()
            self.putLeftFork()
            self.putRightFork()
    # 就餐
    def eat(self):
        self.operate_queue.put([self.philosopher_num, 0, 3])
        print(f'哲学家{self.philosopher_num} 就餐')
        self.sleep()

    # 拿起左边的叉子
    def pickLeftFork(self):
        self.operate_queue.put([self.philosopher_num, 1, 1])
        print(f'哲学家{self.philosopher_num} 拿起左边的叉子')

    # 拿起右边的叉子
    def pickRightFork(self):
        self.operate_queue.put([self.philosopher_num, 2, 1])
        print(f'哲学家{self.philosopher_num} 拿起右边的叉子')


    # 放下左边的叉子
    def putLeftFork(self):
        self.operate_queue.put([self.philosopher_num, 1, 2])
        print(f'哲学家{self.philosopher_num} 放下左边的叉子')
        self.leftlock.release()

    # 放下右边的叉子
    def putRightFork(self):
        self.operate_queue.put([self.philosopher_num, 2, 2])
        print(f'哲学家{self.philosopher_num}  放下右边的叉子')
        self.rightlock.release()

    def sleep(self):
        time.sleep(random.randint(1,3))

if __name__ == '__main__':
    lock0 = threading.RLock()
    lock1 = threading.RLock()
    lock2 = threading.RLock()
    lock3 = threading.RLock()
    lock4 = threading.RLock()
    operate_queue = queue.Queue()
    alist = []
    cnt = 2
    for i in range(cnt):
        zxj0 = DiningPhilosophers(0, lock0, lock1, operate_queue)
        zxj1 = DiningPhilosophers(1, lock1, lock2, operate_queue)
        zxj2 = DiningPhilosophers(2, lock2, lock3, operate_queue)
        zxj3 = DiningPhilosophers(3, lock3, lock4, operate_queue)
        zxj4 = DiningPhilosophers(4, lock4, lock0, operate_queue)

        zxj0.start()
        zxj1.start()
        zxj2.start()
        zxj3.start()
        zxj4.start()

        zxj0.join()
        zxj1.join()
        zxj2.join()
        zxj3.join()
        zxj4.join()
    for i in range(cnt * 5 * 5):
        alist.append(operate_queue.get())
    print(alist)
    print(len(alist))
