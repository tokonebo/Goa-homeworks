# 11) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი 
# მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ კენტი რიცხვები


num12 = int(input("input your number: "))

for i in range(num12):
    if i % 2 != 0:
        print(i)