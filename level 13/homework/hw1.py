# 1 ) მომხმარებელს შემოატაინეთ ორი რიცხვი და მათზე მოახდინეთ მათემატიკური ოპერაციები.
num = int(input("input your 1st number: "))
num1 = int(input("input your 2nd number: "))

print(num * num1)
print(num // num1)
print(num + num1)
if num > num1:
    print(num - num1)
elif num1 > num:
    print(num1 - num)
else :
    print("try again")