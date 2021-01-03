from abc import ABCMeta, abstractmethod
# 动物园
class Zoo(object):
    # 判断重复动物的list
    zoolist=[]
    
    # 实例化后添加类属性名(动物园名字)
    def __init__(self,zname):
        self.add_zooname(zname)

    @classmethod
    def add_zooname(cls, zooname):
        cls.zooname=zooname
    # 添加动物
    # animal_str:属性名(为字符串), func:实例名, 添加方法add_animal('cat1',cat1)
    @classmethod
    def add_animal(cls, animal_str, func):
        # 判断动物属性名是否存在
        if hasattr(Zoo, animal_str):
            print("动物已存在")
        else:
            ad = func.__dict__
            # 判断动物名称是否存在，不存在就添加
            if ad['name'] in cls.zoolist:
                print(func.__dict__['name'], "动物已存在")
            else:
                setattr(Zoo, animal_str, func.__dict__)
                cls.zoolist.append(ad['name'])
class Animal(metaclass=ABCMeta):
    """
    shape_dict
    (0 1 2)
    0 代表 小
    1 代表 中
    2 代表 大
    """

    def __init__(self, name, a_type, shape):
        shape_dict={'小':0,'中':1,'大':2}
        self.name = name
        a_type_list=["食肉","食草"]
        if  not a_type in a_type_list:
            print("类型输入字符只能是： 食肉， 食草,请重新输入")

        self.a_type = a_type
        self.shape = shape
        if shape_dict[shape] >= 1 and self.a_type == "食肉":
            self.character = "凶猛"
        else:
            self.character = '温顺'

    # 动物类Animal()不允许实例化
    @abstractmethod
    def _abc(self):
        pass


class Dog(Animal):
    jiaoshen = "汪汪汪"

    def if_pet(self):
        print(self.character)
        if self.character == "温顺":
            print("适合做宠物")
        else:
            print('不适合做宠物"')
    # 覆盖Animal类_abc方法,不然实例化不了
    def _abc(self):
        pass

class Cat(Animal):

    # 添加动物叫声
    @classmethod
    def jiaos(cls,ys):
        cls.jiaoshen = ys

    # 判断是否适合做宠物
    def if_pet(self):
        print(self.character)
        if self.character == "温顺":
            print("适合做宠物")
        else:
            print('不适合做宠物"')

    # 覆盖Animal类_abc方法,不然实例化不了
    def _abc(self):
        pass

if __name__ == '__main__':
    z = Zoo("时间动物园")

    print("----------------大花猫----------------")
    cat1 = Cat('大花猫 1', '食肉', '小')
    Cat.jiaos("喵喵喵喵")
    print("打印叫声: ", cat1.jiaoshen)
    cat1.__dict__["jiaoshen"] = cat1.jiaoshen
    cat1.if_pet()

    print("----------------熊猫----------------")
    cat2 = Cat('熊猫 1', '食草', '中')
    cat2.if_pet()

    print("----------------老虎----------------")
    cat3 = Cat('老虎 1', '食肉', '大')
    cat3.if_pet()
    print("----------------狗类----------------")
    dog1= Dog("泰迪 1", '食肉', '小')
    print("----------------添加动物----------------")
    z.add_animal('cat1',cat1)
    z.add_animal('cat2',cat2)
    z.add_animal('cat3',cat3)
    z.add_animal('dog1',dog1)
    print(z.cat1)
    print(z.cat2)
    print(z.cat3)
    print(z.dog1)

    print("----------------重复添加处理----------------")
    z.add_animal('cat1', cat1)
    z.add_animal('cat5',cat1)

    print("---------------动物类不允许实例后，实例后报错----------------")
    animal = Animal()
