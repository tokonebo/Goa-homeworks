# 5) შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.


num1 = int(input("enter the first digit: "))
num2 = int(input("enter the second digit: "))

if num1 > 10 or num2 < 50:
    print("the first number is greater than 10 or the second number is less than 50.")
else:
    print("the conditions are not met.")