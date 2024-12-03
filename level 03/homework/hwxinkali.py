#5) Turtle ბიბლიოთეკის დახმარებით დახატეთ ფასანაურული ხინკალი


from turtle import *



speed(30)
width(15)
color('bisque')
begin_fill()


backward(200)
forward(400)
left(60)
forward(50)
left(70)
forward(285)
right(40)
forward(60)
left(90)
forward(80)
left(90)
forward(60)
right(40)
forward(285)
left(70)
forward(50)
left(60)

end_fill()


penup()
goto(-10,240)
pendown()
backward(20)

color('burlywood')
width(25)
right(115)
forward(190)

penup()
goto(3,230)
pendown()
left(25)
forward(180)

penup()
goto(35,240)
pendown()
left(25)
forward(190)

left(65)
penup()
goto(0,0)
pendown()

width(20)
color('tan')


backward(200)
forward(400)
left(60)
forward(50)
left(70)
forward(285)
right(40)
forward(60)
left(90)
forward(82)
left(90)
forward(60)
right(40)
forward(285)
left(70)
forward(50)

exitonclick()