


import turtle
eddietheturtle = turtle.Screen()
eddietheturtle.bgcolor("grey")
eddietheturtle.screensize(450,450)


eddietheturtle = turtle.Turtle()
eddietheturtle.speed(10)
eddietheturtle.penup()



'''
eddietheturtle.forward(150)
eddietheturtle.left(90)
eddietheturtle.forward(75)
eddietheturtle.color("white")
eddietheturtle.pensize(12)
'''


#code for reading text file

TEXTFILENAME = "turtle-draw.txt"

#ask user for the file name

turtledrawTextfile = open(TEXTFILENAME, "r")
line = turtledrawTextfile.readline()
while line:
    print(line, end="")
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0] 
        x = int(parts[1])
        y = int(parts[2])

        
        eddietheturtle.color(color)
        eddietheturtle.goto(x,y)

        # calculate the distance and add to the total distance
        
        eddietheturtle.pendown()

    if (len(parts) == 1):
        eddietheturtle.penup()


    line = turtledrawTextfile.readline()

#print total in the bottom right of the screen

turtle.done()
turtledrawTextfile.close()
print('\nEnd')





input("press enter to continue")

