# 3) შეადარეთ თქვენი ასაკი მომხმარებლის შემოტანილ ასაკს,
# თუ თქვენი ასაკი მეტია მომხმარებლის ასაკზე უთხარით რომ თქვენ მასზე დიდი ხართ, თუ მასზე პატარა ხართ დაუპრინტეთ რომ მასზე პატარა ხართ და სხვა შემთხვევაში დაუპრინტეთ რომ ტოლები ხართ.

myage = 15
userage = int(input("input your age here --> : "))

if myage > userage:
    print("im older than you")
elif myage < userage:
    print("your older than me")
else:
    print("we're the same age")
