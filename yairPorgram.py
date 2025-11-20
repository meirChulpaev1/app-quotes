def funSum101():
  total=0
  for i in range(1,101):
   total+=i
   

def func(num):
 sum=1
 for i in range(1,num+1):
        sum *= i
 return sum



def func2(n):
 for i in range(2,n):
    if n%i==0:
      return False
 return True
    
print(func2(5))
print(func2(6)) 
print(func2(7))     
print(func2(8))

print(func(5))
print(func(6)) 
print(func(7))
print(func(8))
