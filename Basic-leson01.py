import math
# Python - Basic
# condition
def ax(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return
    elif a == 0 and b == 0:
        return
    elif a == 0:
        x = -c/b
        return x
    else:
        delta = b*b - 4*a*c

    if delta < 0:
        return
    elif delta == 0:
        x = -b/(2*a)
        return x
    else:
      x1 = (-b + math.sqrt(delta)) / (2*a)
      x2 = (-b - math.sqrt(delta)) / (2*a)             
      return x1, x2              

def b(s,age):
 if age<18:
    print("before army")
 else:
    if s == "woman":
       if age<20:
          print("Currently Serving")
       else:
          print("Released Citizen")
    else:
       if age>20:
          age1=str(age)
          if "."in age:
              month=age1.split(".")[1]
              month1= int(month)
              if month1>=8:
                 print("Released Citizen")
              else:
                 ("Currently Serving")
       else:
          print("Currently Serving")

def previous_letter(a, b):
    a = a.lower()
    b = b.lower()
    if a < b:
        return a
    else:
      return b
      
   
# loops
    
def firstNumber(num):
    listFirstNum = []

    for i in range(2, num + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            listFirstNum.append(i)
print(firstNumber(20))
 
def Olderguy(num=input):
   for i in range (0,num+1):
      name = input("What is your name? ")
      age = input("What is your name? ")
      
