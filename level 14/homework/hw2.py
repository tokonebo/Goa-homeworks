# 2) გამოიყენეთ or ოპერატორი, რათა შეამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე მეტი ან 50-ზე ნაკლები.

num = int(input("input a number and we will see if its greater than 10 and less than 50: "))

if num > 10 or num < 50 :
    print("its either less than 50 or greater than 10")
else:
    print("try again")

    # ეს კოდი ითხოვს მომხმარებლისგან რიცხვის შეყვანას და ამოწმებს 
    # არის თუ არა ის 10-ზე დიდი და 50-ზე ნაკლები. თუ პირობა შესრულდება
    # გამოდის წარმატების შეტყობინება თორემ ითხოვს კიდევ სცადოს.