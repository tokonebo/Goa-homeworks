from turtle import *

#we want to paint a house

#step 1 draw a square
speed(30)
width(7)
begin_fill()
color("darksalmon")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#door

forward(70)
color("darkorange2")
begin_fill()
left(90)
forward(120)

right(90)
forward(60)

right(90)
forward(120)

right(90)
forward(60)

left(90)

end_fill()

penup()
goto(200,200)
pendown()


#roof
color('brown3')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
left(120)
forward(200)


end_fill()

penup()
goto(20,130)
pendown()

#first window
color('darkslategray1')
begin_fill()


forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
end_fill()

color('darkorange2')
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)

penup()
goto(130,130)
pendown()

#secondwindow
color('darkslategray1')
begin_fill()

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
end_fill()



color('darkorange2')
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)


#doorhandle
color("darkorange4")
penup()
goto(75,60)
pendown()

forward(15)






exitonclick()