
#-------連結-----------
print("Hello" + "world")
name = "tom"
print("My name is" + name)

age = 24

print("My name is " + name +" " + "My age is " + str(age))

#----------リスト------------
li = []
li.append("python")
li.append("php")
print(li[0])

#------辞書型---------
profile = {"name": "tani", "email": "kazunori-t@cyberbra.in"}
print(profile["name"])

profile["gender"] = "male"

print(profile)

#-------条件分岐（if文）--------------
score = 80
if score > 78:
    print("合格です")
elif score == 50:
    print("ちょうど半分！？")
else:
    print("不合格")

#--------for文---------------
for i in ["apple", "banana", "melon"]:
    print(i)

for i in range(11):
    print(i)

date = [20, 40, 50, 60]
for d in date:
    print(d)

sum_d = 0
for d in date:
    sum_d += d
print(sum_d)

sum_d = 0

for d in date:
    sum_d += d
else:
    print(sum_d)

for i in range(11):
    if i == 3:
        continue
    print(i)

for i in range(10):
    if i == 3:
        break
    print(i)

data = [1, 2, 3, 4, 5, "f"]
for x in date:
    if x == 'f':
        print("found")
        break
else:
    print("not found")

for char in "hello":
    print(char)

for index, name in enumerate(["apple", "banana", "melon"]):
    print(index,name)

print(list(range(101)))

data = {"tani": 21, "kazu": 22, "python": 100}
for key, value in data.items():
    print("key: {} value: {}".format(key, value))

#-------------while文---------------
n = 0
while n < 10:
    print(n)
    n += 1

    
result = [x**2 for x in range(1,11)]
print(result)

#----------上記と同じ--------------
result = []
for i in range(1,11):
    result.append(i**2)

print(result)

s = {x**2 for x in range(1,6)}
print(s)

d = {x*2:x**2 for x in range(1,11)}
print(d)

t = (x for x in range(5))
print(t)

t = tuple([x for x in range(5)])
print(t)

print("名前を入力してください")
name = input()
print("あなたの名前は"+name+"です")

#-----関数--------

def hello():
    print("hello!")

hello()

def test():
    pass

def say_hello(name):
    print("こんにちは" + str(name)+ "さん")

say_hello("山田")

def adder(a,b):
    return a+b

value = adder(4,2)

data = [1,2,3,4,5]

value = len(data)

print(value)

def adder1(a, b):
    print(a+b)

def adder2(a, b):
    return a + b

adder1(2, 4)
sum = adder2(2, 4)
print(sum)

def a(a,b):
    return a + b

def b(a,b):
    return a * b

x = a(2,2)
y = b(x,x)

print(y)

def power(x):
    return x*x

def absolute(x):
    if (x < 0):
        return -x
    else:
        return x
print(power(10))
print(absolute(-10))

def func(a, b=5):
    print(a)
    print(b)

func(10,15)
func(3)

def sample(arg, ):
    arg_list = []
    arg_list.append(arg)
    print(arg_list)

sample("python")
sample("Python")

def add(x1):
    x2 = 10
    result = x1 + x2
    print(result)

add(5)

def add(x1):
    x2 = 10
    result = x1 + x2
    print(result)

add(5)
#print(x2)

def add(x1,x2):
    result = x1 + x2
    return result

x1 = 5
x2 = 10
result = add(x1, x2)
print(result)

#-----------グローバル宣言、グローバル変数-------------

glb = 0

def func1():
    glb =  1

def func2():
    global glb
    glb = 5

print(glb)
func1()
print(glb)
func2()
print(glb)
