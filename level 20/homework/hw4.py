# 5) დაწერეთ ციკლი რომელიც ლუწს გამოიტანს " 
# მე მიყვარს გოა" და კენტს " მე მიყვარს პროგრამირება".

num = int(input("number: "))

for i in range( 0,num):
    if i % 2 == 0:
       print(" i love goa")
    else:
       print("i love programming")