# add this to the jupitor notebook --> every single-line/method or class indicates a block code in jupitor

# Callable

def add(x,y):
    return x+y

add

ad(1,2)

callable(add)

a = 123
callable(a)

class Add:
    def __call__(self, xy):
        return x+y

add1 = Add()
callable(add1)

add1(1, 2)

add(1,2)



#Generators & iterator class:
from time import sleep

def compute():
    l = []
    for i in range(10):
        sleep(0.5)
        l.append(i)
    return l

compute()
# [0,1,2,3,4,5,6,7,8,9]

l = [1,2,3,4]

for i in l:
    print(i)

li = iter(l)

next(li)
# when running next(li) you can run every element seperatly and maybe do something about the single element and then throw it away. so everytime you run the code it goes from 1 --> 2 ---> 3 ---> 4

class Computer:
    def __iter__(self):
        self.last = 0 # the last value i have looked at
        return self

    def __next__(self):
        if self.last > 10:
            raise StopIteration()
            self.last += 1



compute1 = Compute()

# ic = iter(compute1)

# next(ic)
# # 1 --> 2 --> 3 --> 4 ... --> 10

for i in Compute():
    print(i)


# Generator functions (generator object) 
def compute_x():
    for i in range(10):
        yield i

x = compute_x()

next(x)


for i in compute_x():
    print(i)

# Generator expressions

l = [l for i in range(10)]
l
# [0,1,2,3,4,5,6,7,8,9]

gen_expr = (l for i in range(10))
gen_expr

next(gen_expr)