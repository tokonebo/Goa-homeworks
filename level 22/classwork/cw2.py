

# num = int(input("enter number: "))

# sum1 = 0
# for i in range(1,num,1):
#     sum1 = sum1 + i 

# sum = 0
# for i in range(1,num,2):
#     sum = sum + i  
   
# print(sum)
# print(sum1)






num = int(input("enter number: "))

sum1 = 0
for i in range(num):
    if i % 2 == 1:
        sum1 = sum1 + i 

sum = 0
for i in range(num):
    if i % 2 == 0:
        sum = sum + i  
   
print(sum)
print(sum1)




