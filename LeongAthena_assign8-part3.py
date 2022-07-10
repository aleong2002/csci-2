"""
Athena Leong
Assignment 8 Part 3
04/11/2022
"""
import turtle
turtle.setup(600,600)

# function:   bar_chart
# input:      x & y value (integers), labels, values and colors (lists)
# processing: draws a bar chart with the origin of the chart being at the x
#             and y value supplied. the height of the chart will always be
#             100 units, and the width of each bar in the chart can be
#             computed as 50 units for each value in the 'values' list.
#             draw two black lines to show these axes.
#
#             the height of each bar should be proportionatly scaled so that
#             no bar ever ends up having a height of over 100 units.  for example,
#             with the list [100,200,300] the third bar would be 100 units
#             high, the second would only be 66.6 units high and the first would
#             be 33.3 units high.
#             
#             each value in the 'labels' list indicates the label for each bar
#             in the bar chart.  these should be written below the x-axis
#             using the 'turtle.write' function.  Ensure that these labels are
#             spaced out accordingly (50 pixels for each bar)
#             
#             each bar should be drawn on top of the x-axis with a height defined
#             in the 'values' list.  the color for each bar can be extracted
#             from the 'colors' list.  the value of each bar should also be 
#             written at the top of each bar.
# output:     function returns no value

def bar_chart(x, y, label, value, color):
    # drawing the y and x axis - color black
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.goto(x + 100, y)
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.goto(x, y + (50 * len(label)))
    turtle.pu()

    # label the x axis - color black
    for i in range(0, len(label)):
        turtle.goto(x + (50 * i),y - 5)
        turtle.write(label[i])

    # draw the boxes
    for i in range(0, len(value)):
        
        if max(value) > 100:
            if max(value) % 10 == 0:
                
                turtle.pu()
                turtle.goto(x + (50 * i), y)
                turtle.color(color[i])
                turtle.begin_fill()
                turtle.pd()
                turtle.goto(x + (50 * i), int(value[i]) / 10 )
                turtle.goto(x + (50 * (i+1)), int(value[i]) / 10)
                turtle.goto(x + (50 * (i+1), y))
                turtle.goto(x + (50 * i), y)
                turtle.end_fill()
            elif max(value) % len(value) == 0:
                turtle.pu()
                turtle.goto(x + (50 * i), y)
                turtle.color(color[i])
                turtle.begin_fill()
                turtle.pd()
                turtle.goto(x + (50 * i), int(value[i]) / len(value))
                turtle.goto(x + (50 * (i+1)), int(value[i]) / len(value))
                turtle.goto(x + (50 * (i+1), y))
                turtle.goto(x + (50 * i), y)
                turtle.end_fill()
            else:
                turtle.pu()
                turtle.goto(x + (50 * i), y)
                turtle.color(color[i])
                turtle.begin_fill()
                turtle.pd()
                if max(value) > 100:
                    turtle.goto(x + (50 * i), 100)
                    turtle.goto(x + (50 * i + 1), 100)
                turtle.goto(x + (50 * i), value[i])
                turtle.goto(x + (50 * (i+1)), value[i])
                turtle.goto(x + (50 * (i+1), y))
                turtle.goto(x + (50 * i), y)
                turtle.end_fill()

        else:
            
            turtle.pu()
            turtle.goto(x + (50 * i), y)
            turtle.color(color[i])
            turtle.begin_fill()
            turtle.pd()
            turtle.goto(x + (50 * i), value[i])
            turtle.goto(x + (50 * (i+1)), value[i])
            turtle.goto(x + (50 * (i+1), y))
            turtle.goto(x + (50 * i), y)
            turtle.end_fill() 





#bar_chart(-200,-200,["pikachu"], [99999], ['yellow'])
#bar_chart(0,-200,["x","y","hello","world"], [1000,900,800,700], ['grey','pink','black','purple'])

bar_chart(-200,0,["apple", "pear", "orange"], [100,200,300], ['red', 'green', 'orange'])
#bar_chart(0,0,["a","b","c","d","e"], [50,70,90,10,30], ['blue','pink','red','green','yellow'])

