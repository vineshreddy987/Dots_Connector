from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
next_dot = 0

# Create 10 dots with random positions
for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    screen.fill("black")
    
    # Draw the dots and their numbers
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12), color="white")
        dot.draw()
        number += 1
    
    # Draw lines connecting the dots
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

def on_mouse_down(pos):
    global next_dot

    # Check if the clicked dot is the next correct dot
    if dots[next_dot].collidepoint(pos):
        if next_dot > 0:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))  # Add a line between the dots
        next_dot += 1
    else:
        print("Wrong dot!")
        quit()

    # End the game when all dots are connected
    if next_dot == len(dots):
        print("You connected all the dots!")
