"""l=10
def function1(n):
    print(n, "I have printed")
    l=5
    m=7
    print(l, m)

function1("This is me")
print(l)"""

"""m=88
def func1():
    global m
    m=m+10
    print(m)

func1()"""

def sonu():
    x=30
    def shivam():
        global x
        x=40
    print("before calling shivam()",x)
    shivam()
    print("after calling shivam()",x )

sonu()
print(x)


