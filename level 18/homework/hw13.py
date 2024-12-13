#  13) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი 
# მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები


num= int((input("input a number: ")))


if num % 5==1:
    num = num + 4 
    
if num % 5==2:
    num = num + 3

if num % 5==3:
    num = num + 2

if num % 5==4:
    num = num + 1

if num % 5==0:
    print(num)
