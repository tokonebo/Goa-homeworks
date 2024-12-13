#  12)  მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე
# დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტი



n = int(input("input your number: "))
 
for i in range(n): 
 if i % 2 == 0:
        print(str(i) + " even")
else:
        print(str(i) + " odd")
