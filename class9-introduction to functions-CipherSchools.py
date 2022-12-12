# functions - reusable piece of code

def show_loading():
    for i in range(3):
        print("loading...")


a = 5
b = 7
show_loading()


def sheldon_knocks(name):
    for i in range(3):
        print("knock knock knock",name)

sheldon_knocks(penny)

#return statement
def add(a,b):
    return(a+b)

a = add(1,2)
print(a)
