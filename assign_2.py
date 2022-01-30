# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:35:00 2022

@author: Agroveggies
"""

#assignment 2 : task 1 and task 2

 #fibonacci series
 
n = int(input("enter the value of n : "))

a = 0

b = 1

sum = 0

count = 1

print("fibonacci series : " , end = " ")

while(count <= n) :
    print(sum , end = " ")
    count += 1
    a = b
    b = sum 
    sum = a + b


 
 #print positive numbers in range
 
list1 = [12 , -7 , 5 , 64 , -14]


for num in list1 :
    if num >= 0 :
        print(num , end = " ")
        
        
list2 = [12 , 14 , -95 , 3]   

     
for num in list2 :
    if num >= 0 :
        print(num , end = " ")









