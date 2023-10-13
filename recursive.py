#1
# def sum_list(x):
#     if len(x) == 0:
#         return 0
#     else:
#         return x[0] + sum_list(x[1:])
# print(sum_list([1,2,3,4,5]))
# 
# 
#2
# def fact(n):
#     if n <=1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

 

 

#3
# T= int(input("Enter a term"))
# 
#     
# def fibonacci(term,term2,T):
#     x = term + term2
#     term = term2
#     term2 = x
#     if T <= 1:
#         return 1
#     else:
#         return  term + fibonacci(term,term2,T-1)
# if T == 0:
#     print(0)
# elif T == 1:
#     print(1)
# else:
#     print(fibonacci(0,1,T))

 

 

#4
# def sum_digi(x):
#     x2 =x
#     len1=0
#     while x2 >0.9:
#         len1 += 1
#         x2 = x2 / 10
#     
#     if len1 < 1:
#         return 1
#     elif len1 == 1:
#         return x
#     else:
#         
#         return (x%10) + sum_digi(int(x/10))
# 
# num = int(input("Enter a number"))
# print(sum_digi(num))

 

 

#5
# def HCF(x,y):
#     if x > y :
#         div = x
#         divi = y
#     elif y > x :
#         div = y
#         divi = x
#     elif y == x:
#         return x
#     if x == 0:
#         return div
#     quot = int(div/divi)
#     rem = div-(quot*divi)
#     if quot == divi and rem == 0:
#         return quot
#     else:
#         return  HCF(rem,divi)
#     
# num = int(input("1st number"))
# num2 = int(input("2nd number"))
# 
# print(HCF(num, num2))

 

 

#6
# def LCM(y,z,m):
#     low = y
#     if z%low == 0 and z>=low:
#         return z
#     else:
#         return LCM(low,z+m,m)
# 
# num = int(input("1st number"))
# num2 = int(input("2nd number"))
# if num > num2:
#     mul = num2
# elif num2 > num:
#     mul = num
# mul2 = mul    
# print(LCM(num2,mul,mul2))

 

#7
# def sum(x,a,sum1):
#     if a == x:
#         return sum1
#     elif a % 2 == 0:
#         return sum(x,a+1,sum1)
#     else:
#         return sum(x,a+1,sum1+a)
#             
# n = int(input("Enter a num: "))
# a = 1
# sum1=0
# print(sum(n,a,sum1))

#8
# def sumrecip(n,sum1):
#     if n < 1:
#         return 0
#     else:
#         sum1 = 1/n
#         return sum1 + sumrecip(n-1,sum1) 
#         
#     
# n=10
# sum1 = 0
# print(sumrecip(n,sum1))

#9
# def sumpie(n,sum1):
#     if n < 1:
#         return 0
#     elif n%2!=0:
#         sum1 = 4/(n+(n-1))
#         return sum1 + sumpie(n-1,sum1) 
#     elif n%2==0:
#         sum1 = 4/(n+(n-1))*-1
#         return sum1 + sumpie(n-1,sum1)  
#         
#     
# n=int(input("Enter a term: "))
# sum1 = 0
# print(sumpie(n,sum1))

#10
# def fact(n):
#     if n <=1:
#         return 1
#     else:
#         return n * fact(n-1)
# 
# 
# def sume(n,sum1):
#     if n < 0:
#         return 0
#     else:
#         sum1 = 1/fact(n)
#         return sum1 + sume(n-1,sum1) 
#         
#     
# n=int(input("Enter a term: "))
# sum1 = 0
# print(sume(n,sum1))

#11
