
import turtle
import time

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Beautiful Analog Clock")
screen.bgcolor("indigo")
screen.tracer(0)  # Turn off the screen updates

# Create the drawing turtle
clock = turtle.Turtle()
clock.hideturtle()
clock.speed(0)

# Create the hands turtles
second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.color("red")
second_hand.shapesize(stretch_wid=0.2, stretch_len=12)
second_hand.speed(0)

minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.color("blue")
minute_hand.shapesize(stretch_wid=0.4, stretch_len=10)
minute_hand.speed(0)

hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.color("green")
hour_hand.shapesize(stretch_wid=0.5, stretch_len=8)
hour_hand.speed(0)

# Create the text turtle for AM/PM and day
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.speed(0)
text_turtle.color('white')

# Create the clock face
def draw_clock_face(radius):
    clock.penup()
    clock.goto(0, -radius)
    clock.pendown()
    clock.pensize(5)  # Increase border width
    clock.circle(radius)
    clock.penup()
    clock.goto(0, 0)
    clock.fillcolor("white")
    clock.begin_fill()
    clock.goto(0, -radius + 5)  # Inner border position
    clock.pendown()
    clock.circle(radius - 5)
    clock.end_fill()
    clock.penup()
    clock.goto(0, 0)

    # Draw the hour markers
    for hour in range(12):
        clock.penup()
        clock.goto(0, 0)
        clock.setheading(-30 * hour + 60)
        clock.forward(radius - 20)
        clock.pendown()
        clock.forward(20)
        clock.penup()
        clock.goto(0, 0)
        clock.forward(radius - 40)
        clock.pendown()
        clock.write(str(hour + 1) + ":", align="center", font=("Arial", 14, "bold"))
        clock.penup()
        clock.goto(0, 0)

    # Draw the center circle
    clock.penup()
    clock.goto(0, 0)
    clock.dot(20, "black")

# Update the hands and text of the clock
def update_hands():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour
    am_pm = "AM" if hours < 12 else "PM"
    hours = hours % 12
    hours = 12 if hours == 0 else hours
    day = time.strftime("%A")

    # Calculate the angles for each hand
    second_angle = 6 * seconds
    minute_angle = 6 * minutes + 0.1 * seconds
    hour_angle = 30 * hours + 0.5 * minutes

    # Update the hand positions
    second_hand.setheading(90 - second_angle)
    minute_hand.setheading(90 - minute_angle)
    hour_hand.setheading(90 - hour_angle)

    # Update the AM/PM and day display
    text_turtle.clear()
    text_turtle.penup()
    text_turtle.goto(0, 260)
    text_turtle.write(f"{day} {hours}:{minutes:02d} {am_pm}", align="center", font=("Arial", 16, "bold"))

    screen.update()
    screen.ontimer(update_hands, 1000)

# Draw the clock face
draw_clock_face(200)

# Start updating the hands
update_hands()

# Keep the window open
turtle.done()
