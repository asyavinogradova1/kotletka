from pygame import*
WIDTH = 960
HEIGHT = 720 
win = display.set_mode((WIDTH,HEIGHT))

bg = image.load("05.jpg")

win.blit(bg, (0,0))
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            exit()
    display.update()

