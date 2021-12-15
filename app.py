import turtle
import random
import time

t = turtle.Turtle()

t.hideturtle()
t.speed(0)
turtle.tracer(0)

is_first_box_clicked = False
first_box = None

n = 2

randoms = [k for k in range(n**2 // 2)] * 2

box_size = 70
boxes = []

def draw_box(x, y, text, color="black"):
    t.up()
    t.goto(x, y)
    t.down()
    t.color(color) 
    t.begin_fill()
    for i in range(4):
        t.forward(box_size)
        t.left(90)
    t.end_fill()
    t.up()
    t.goto(x + box_size/2 - 10, y + box_size/2 - 5)
    t.down()
    t.color("white")
    t.write(text, font=('Arial', 14, 'normal'))
    t.up()
    t.goto(x, y)

def get_random():
    choice = random.choice(randoms)
    randoms.remove(choice)
    return choice


def get_clicked_box(mouse_x, mouse_y):
    for i, box in enumerate(boxes):
        value, x, y = box
        if x <= mouse_x <= x + box_size and y <= mouse_y <= y + box_size:
            return i

def redraw_all_boxes():
    t.clear()
    for value, x, y in boxes:
        draw_box(x, y, "")

def box_clicked(mouse_x, mouse_y):
    global is_first_box_clicked, first_box
    i = get_clicked_box(mouse_x, mouse_y)
    if i is None or i == first_box:
        return
    value, x, y = boxes[i]
    if not is_first_box_clicked: # Première case cliqué
        is_first_box_clicked = True
        first_box = i
    else: # Deuxième case cliquée
        is_first_box_clicked = False
        value_bis, x_bis, y_bis = boxes[first_box]
        draw_box(x_bis, y_bis, value_bis, "red")
        draw_box(x, y, value, "red")
        time.sleep(3)
        if value == value_bis:
            boxes.remove((value, x, y))
            boxes.remove((value_bis, x_bis, y_bis))
            if not boxes:
                print("C'est fini")
        redraw_all_boxes()

turtle.onscreenclick(box_clicked)


x = -400
y = 300
for _ in range(n):
    for _ in range(n):
        draw_box(x, y, "")
        boxes.append((get_random(), x, y))
        x += box_size + box_size / 2
    y -= box_size + box_size / 2
    x = -400

# turtle.done()
turtle.mainloop()
