from turtle import *

shape('turtle')
speed(0)

length = 10

for i in range (100):
   forward(length)
   length += 5
   left(90)


mainloop()
