show = print
show("something")

int a[]={1,2,3}
names = ["jatin", "saransh", "vishal"]
for i in enumerate(names):
    print(i)


a = 5
b = 9
temp = a
a=b
b=temp
print(a,b)

c= 5
d=9
c,d=d,c

names = ["jatin", "vishal", "ankit"]
marks = [50,80,95]
state = ["UP", "Delhi", "Punjab"]
for i, name in enumerate(names):
    marks=marks[i]
    print(name,"-",marks,state)