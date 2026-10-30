#def sumTo(n):
#    return (n * (n+1) / 2)

#print(sumTo(10))

#import turtle
#def star(n):
    #t = turtle.Turtle()
    #for i in range(n):
        #t.forward(100)
        #t.right(360 * 2 / n)

#star(5)
#wn.screen()

#def sumTo(n):
    #total = 0
#
   # for i in range(1, n + 1):
  #      total += i
#
 #   return total
#
#print(sumTo(10))

#def mySqrt(n):
 #   guess = n / 2
#
 #   for i in range(10):
  #      newguess = (1/2) * (guess + (n / guess))
   #     guess = newguess
#
 #   return guess

#print(mySqrt(25))


#import turtle
#
#def drawSprite(t, size):
#    for i in range(1):
#        t.forward(size)
#        t.right(120)
#        t.forward(size)
#        t.right(120)
#        t.forward(size)
#        t.left(60)
#        t.backward(size)
#
#def fancySquare(t, size):
#    for i in range(4):
#        drawSprite(t, 20)
#        t.forward(size)
#        t.right(90)
#
#
#t = turtle.Turtle()
#t.speed(5)
#t.pensize(3)
#
#fancySquare(t, 150)


#def checkNumber(n):
#    if n > 0:
#        return("this number is postive")
#    elif n < 0:
#        return("this number is negative")
#    else:
#        return("this number is zero")
#
#    
#print(checkNumber(5))
#print(checkNumber(-3))
#print(checkNumber(0))


#import turtle

#def drawBar(t, height, label, move_up):
#    width = 30
#
#    t.begin_fill()
#
#    t.left(90)
#    t.forward(height)
#    t.right(90)
#    t.forward(width)
#    t.right(90)
#    t.forward(height)
#    t.right(90)
#    t.forward(width)
#
#    t.end_fill()
#
#    t.penup()
#    t.right(90)
#    t.forward(height + move_up)
#
#    t.backward(height + move_up)
#    t.right(90)
#    t.backward(width / 2)
#
#    t.pendown()
#    t.forward(width + 15)
#
#def barChart(data):
#    maxheight = 200
#    border = 20
#
#    maxvalue = max(data)
#
#    move_up = (maxheight + border) * 0.02
#
#    t = turtle.Turtle()
#    t.speed(5)
#    t.fillcolor("skyblue")
#
#    t.penup()
#    t.goto(-250, -150)
#    t.pendown()
#
#    for value in data:
#        height = (value / maxvalue) * maxheight
#        drawBar(t, height, value, move_up)
#
#    turtle.done()
#
#data = [48, 117, 200, 240, 160, 260, 220]
#
#barChart(data)