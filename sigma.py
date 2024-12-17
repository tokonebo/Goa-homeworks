num = int(input("input a number: "))
i = 0
sum = 0
sum1 = 0
while i <= num :
  if i % 5 == 0:
     sum = sum + i
  elif i % 3 == 0:
     sum1 = sum1 + i

  i = i + 1

print(sum)
print(sum1)