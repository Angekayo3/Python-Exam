import turtle  # Import the turtle module for drawing
import time  # Import the time module to get the current time

# Set up the screen
screen = turtle.Screen()  # Create a screen object
screen.title("Digital Clock")  # Set the title of the window
screen.bgcolor("black")  # Set the background color to black
screen.setup(width=600, height=300)  # Set the size of the window

# Create the turtle object
clock_turtle = turtle.Turtle()  # Create a turtle object for drawing
clock_turtle.color("white")  # Set the color of the turtle to white
clock_turtle.hideturtle()  # Hide the turtle icon
clock_turtle.speed(0)  # Set the speed of the turtle to the fastest
clock_turtle.penup()  # Lift the pen to avoid drawing lines when moving
clock_turtle.goto(0, 0)  # Move the turtle to the center of the screen


# Function to draw the clock
def draw_clock(h, m, s, clock_turtle):
    clock_turtle.clear()  # Clear the previous time
    # Write the current time in HH:MM:SS format at the center of the screen
    clock_turtle.write(f"{h:02d}:{m:02d}:{s:02d}", align="center", font=("Courier", 48, "normal"))


# Update the clock continuously
while True:
    h = int(time.strftime("%H"))  # Get the current hour
    m = int(time.strftime("%M"))  # Get the current minute
    s = int(time.strftime("%S"))  # Get the current second

    draw_clock(h, m, s, clock_turtle)  # Draw the clock with the current time
    time.sleep(1)  # Wait for 1 second
    screen.update()  # Update the screen

# Keep the window open
screen.mainloop()  # Start the main loop to keep the window open
