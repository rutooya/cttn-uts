# game snake sangat sederhana 
# dibuat dengan menggunakan Turtle

# Imports library
import turtle
import time
import random

# Score and delay
score = 0
high_score = 0
delay = 0.1

# persiapkan screen permainan
wn = turtle.Screen()
wn.title('Permainan Ular')
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)  # matikan screen updates

# persiapkan game world
pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape('circle')
pencil.color('white')
pencil.penup()
pencil.hideturtle()
pencil.goto(310,310)
pencil.pendown()
pencil.goto(-310,310)
pencil.goto(-310,-310)
pencil.goto(310,-310)
pencil.goto(310,310)
pencil.penup()

# kepala Ular
head = turtle.Turtle()
# 0 adalah maksimum kecepatan animasi module turtle
head.speed(0) 
head.shape("circle")
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# Makanan Ular
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color('red')
food.penup()
# setup makanan awal
food.goto(0,100)

# berisi informasi tentang badan ular. 
# badan ular terdiri dari banyak segement dan akan bertambah jika 
# ular memakan makanan
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('Score: 0 High Score: 0', align = 'center', font = ('Courier', 24, 'normal'))

### Functions
# Fungsi untuk mengupdate score
def update_score():
    pen.clear()
    pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font = ('Courier', 24, 'normal'))

# Fungsi untuk menggerakan ular berdasarkan tombol keyboard yg ditekan
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# Fungsi untuk menggerakan Ular
def move():
    # pergerakan dimulai dari akhir segement 
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    # pindahkan segment 0 menjadi head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    # Pastikan semua segemen Ular berjalan ke arah yg sama
    if head.direction == 'up':
        head.sety(head.ycor() + 10)
    if head.direction == 'down':
        head.sety(head.ycor() - 10)
    if head.direction == 'left':
        head.setx(head.xcor() - 10)
    if head.direction == 'right':
        head.setx(head.xcor() + 10)

# fungsi yang dijalan jika collusion terjadi
def collision():
    time.sleep(0.5)
    head.goto(0,0)
    head.direction = 'stop'
    # sembunyikan segments
    for segment in segments:
        segment.hideturtle()
    # bersihkan segments list
    segments.clear()
    score = 0
    update_score()
    # Reset delay
    delay = 0.1

### Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

### Game Loop yang menjalankan game code
### Game loop bagian penting dari program Game yang khusus digunakan untuk me-runing program
while True:
    # Updates window berkali-kali
    wn.update()

    # pengecekan apakah ular menabrak batas permainan atau tidak
    # collision detection
    if (head.xcor()>290 
    or head.xcor()<-290 
    or head.ycor()>290 
    or head.ycor()<-290):
        collision()

    # pengecekan apakah ular memakan makanan
    if head.distance(food) < 20:
        # generate makanan pada tempat yang random
        food.goto(random.randint(-290,290),random.randint(-290,290))
        
        # Hint 1
    
        # kurangi delay - menambah kecepatan ular jika segement bertambah panjang
        delay -= 0.001
        # tambahkan score
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # Gerakan Ular
    move()

    # Hint 2
   
    # FPS controller (agar semua obyek game dapat terlihat)
    time.sleep(delay)

# Tampilkan window dan jalankan semuanya
wn.mainloop()