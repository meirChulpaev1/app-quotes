import math
# Python - Basic
# condition
def ax(a, b, c):
    if a == 0 and b == 0 :
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

def b(s, age):
    
    years = int(age)              
    decimal = age - years         
    months = int(decimal * 12)    

    
    total_months = years * 12 + months

   
    enlist_months = 18 * 12

   
    if total_months < enlist_months:
        print("Before Army")
        return

   
    women_release_months = 20 * 12        # 240
    men_release_months   = 20 * 12 + 8    # 248

    if s == "woman":
        if total_months >= women_release_months:
            print("Released Citizen")
        else:
            print("Currently Serving")
    else:  # גבר
        if total_months >= men_release_months:
            print("Released Citizen")
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
 

def Olderguy():
    currAge = 0
    oldest_names = []  

    num = int(input("Enter N: "))

    for i in range(num):
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        if age > currAge:
            currAge = age
            oldest_names = [name]   
        elif age == currAge:
            oldest_names.append(name)

    
    for person in oldest_names:
        print(person, ":", currAge)
   
      
def longestName():
 num = int(input("Enter N: "))
 currn=""
 for i in range (num):
     name = input("What is your name? ")
     if len(currn)>len(name):
         currn=name
 print(currn)         