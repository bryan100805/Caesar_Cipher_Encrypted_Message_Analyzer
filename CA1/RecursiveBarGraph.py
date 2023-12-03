# Name: Tan Wen Tao Bryan
# Student ID: 2214449
# Date: 19/11/2023
# File: RecursiveBarGraph.py

# Creating external class to create a recusive bar graph to display word frequency
import turtle

class RecursiveBarGraph:
    def __init__(self):
        # Set up the window and turtle
        self.window = turtle.Screen()
        self.window.bgcolor('white')
        self.t = turtle.Turtle()
        self.t.speed(2)

        # Move the turtle slightly to the right of (0, 0)
        self.t.penup()
        self.t.goto(-65, 0)
        self.t.pendown()

    # Draw a single bar
    def draw_bar(self, height, freq, word):
        # Draw the bar
        self.t.begin_fill()
        self.t.left(90)
        self.t.forward(height)
        self.t.right(90)
        heading = self.t.heading()
        self.t.forward(30)
        self.t.write(' '+freq, align ="right")

        # Write the word above the frequency
        self.t.setheading(90)
        self.t.penup()
        self.t.forward(10)
        self.t.pendown()
        self.t.write(' '+word, align='right')
        
        # Reset the turtle's heading to continue drawing the bar
        self.t.penup()
        self.t.backward(10)
        self.t.setheading(heading)
        self.t.pendown()

        # Draw the rest of the bar
        self.t.forward(30)
        self.t.right(90)
        self.t.forward(height)
        self.t.left(90)
        self.t.end_fill()
        self.t.forward(10)

    # Draw multiple bars recursively
    def draw_bars(self, word_freqs):
        # Stopping Condition
        if not word_freqs:
            return
        word, freq = self.extract_Nodeinfo(word_freqs[0])
        # Scale the frequency for display purpose
        self.draw_bar(freq*20, str(freq), str(word))
        # Recursive call + Change of state
        self.draw_bars(word_freqs[1:])

    # Extract the info from the Node
    def extract_Nodeinfo(self, node_str):
        parts = str(node_str).split(' - ')
        if len(parts) == 2:
            word, freq = parts
            return word, int(freq.split()[0])
        else:
            return '', 0

    # Draw the axis system
    def draw_axis_system(self):
        # Draw the x-axis
        self.t.color('black')
        self.t.goto(-75, 0)
        self.t.setheading(0)
        self.t.forward(1000)

        # Draw the y-axis
        self.t.color('black')
        self.t.goto(-75, 0)
        self.t.setheading(90)
        self.t.forward(1000)

    # Function to draw the bar graph
    def draw_bar_graph(self, word_freqs):
        self.t.color('black', '#03B4C8')
        self.draw_bars(word_freqs)
        self.draw_axis_system()

        # Hide the turtle and finish
        self.t.hideturtle()
        self.window.exitonclick()