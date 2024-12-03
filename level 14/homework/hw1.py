# 1) თუ ასაკი არის 18 ის ზემოთ ან 50 წლის ქვემოთ  ან თუ  ასაკი  ნაკლებია 18 ზე და მეტია 50 ზე გამოტანეთ ის უნდა იყოს ან მოხუცი ან ახალგაზრდა

age = int(input("enter your age: "))

if 18 > age:
    print("your a kid or a teenager")
elif 50 > age >= 18:
    print("you are young")
else:
    print("you are old")