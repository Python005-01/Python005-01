from inspect import isfunction
def gmap(func,*args, **kwargs):
    if not isfunction(func):
        print("必须转入func")
        return None
    if args and kwargs:
        print("args,kwargs不能同时有值")
        return None

    if args:
        if isinstance(args[0], list) or isinstance(args[0], tuple) or isinstance(args[0],range) or isinstance(args[0],dict):
            for ib in args[0]:
                yield func(ib)

    elif isinstance(kwargs, dict):
            yield from func(kwargs.items())


def ag1(i):
    return i*i
def adict(i):
    return i

print("-"*20)
a = gmap(ag1,range(9))
print(next(a))
print(next(a))
print('for-')
for i in a:
    print(i)
print("-"*20)
b = gmap(adict, a=1,b=3,c=3, d=4)
print(next(b))
print(next(b))
print('for-')
for i in b:
    print(i)
print("-"*20)
c = gmap(adict, {'a':1,'b':2,'c':3,'d':4})
print(next(c))
print(next(c))
print('for-')
for i in c:
    print(i)
