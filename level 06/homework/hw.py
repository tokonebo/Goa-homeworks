string1="15"

print(int(string1))


# 2)დაწერე პროგრამა, რომელიც შეამოწმებს, არის თუ არა მოცემული ცვლადი float ტიპის.

number=input("input a number and well check if its a float: ")

if "." in number:
  print("this is a float")

else:
   print("this is not a float")




# 3)დაწერე პროგრამა, რომელიც integer ტიპს float ტიპად გადააქცევს

integer1=60

print(float(integer1))



# 4)დაწერეთ პროგრამა სადაც მომხმარებელს შემოატანინებთ ინფორმაციას თავის თავზე (name,surname,age,address,gmail) და შემდეგ დაუპრინტეთ ეს ინფორმაცია ერთ დიდ წინადადებად

name =input("hello user input your name: ")


surname=input("now enter your surname: ")
address=input("weed need your address as well: ")
gmail=input("also your gmail to contact you: ")

print("your name is " + name + " " + surname + " your address is " + address + " .we will contact you on " + gmail)



# 5)ჩამოწერეთ რომელი data type'ბი იცით და ახსენით რა რას ემსახურება

#boolean,integer,string და float
# boolean-ით ჩვენ ვიღებთ დადებით ან უარყოფით მნიშვნელობებს და კარგია რაიმეს შედარებისას

# integer მთელი რიცხვებია და მიმატება გამოკლებისას გამოგვადგება

# string კი სიტყვებითი მნიშვნელობისაა და წინადადებების შექმნისთვისაა კარგი

# float ათწილადების სახით ჩაწერილი რიცხვებია და როგორც integer მიმატება გამოკლება შეგვიძლია




# 6)დაადეკლარირეთ 3 სტრინგ ტიპის ცვლადი რომელშიც შეინახავთ თქვენი დაბადების წელს,თვეს,დღეს შემდეგ გარდაქმენით ინტეჯერებად და დაბეჭდეთ

year="2001"
month="11"
day="12"

print(int(year))
print(int(month))
print(int(day))



# 7) გარდაქმენით Boolean ტიპის ცვლადი str ტიპის ცვლადად

boolean= True

print(str(boolean))


# 8) ჩამოწერეთ ოთხივე ტიპის ცვლადი  და ჩაატარეთ ექსპერიმენტული გარდაქმნები 

int9=12
string9="hello"
boolean9= False
float9=7.6

