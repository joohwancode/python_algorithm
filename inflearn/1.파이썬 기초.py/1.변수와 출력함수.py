"""a = 1  ##같은게 아니라 eodlq  하는 것이다.
A = 2
_b=4 
print(a, A)"""


a, b, c = 3, 2, 1
print(a, b, c)

##변수값을 바꾸면 기존 값은 사라진다.
##값교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

##변수타임

a = 12345
print(type(a))
a = 12.34334324239048023482039492394
print(a)

a = "student"
print(type(a))
## 출력방식
a, b, c = 1, 2, 3
print(a, b, c)
print("number")
print("number :", a, b, c)
print(a, b, c, sep=", ")
print(a, b, c, sep=",")
print(a, b, c, sep="")
print(a, b, c, sep="\n")
