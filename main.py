from pygame import *

WIDTH = 1280
HEIGHT = 720

FPS = 60

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Доганялки")

background = transform.scale(image.load("images/bg.png"), (WIDTH, HEIGHT))

sprite_1 = transform.scale(image.load("images/c_1.png"), (100, 100))
sprite_2 = transform.scale(image.load("images/c_2.png"), (100, 100))

sprite_1_x = 100
sprite_1_y = (HEIGHT - 100) // 2

sprite_2_x = WIDTH - 100 - 100
sprite_2_y = (HEIGHT - 100) // 2

clock = time.Clock()

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

    window.blit(background, (0, 0))

    keys = key.get_pressed()

    if keys[K_a] and sprite_1_x >= 0:
        sprite_1_x -= 10
    if keys[K_d] and sprite_1_x <= WIDTH - 100:
        sprite_1_x += 10
    if keys[K_w] and sprite_1_y >= 0:
        sprite_1_y -= 10
    if keys[K_s] and sprite_1_y <= HEIGHT - 100:
        sprite_1_y += 10

    if keys[K_LEFT] and sprite_2_x >= 0:
        sprite_2_x -= 10
    if keys[K_RIGHT] and sprite_2_x <= WIDTH - 100:
        sprite_2_x += 10
    if keys[K_UP] and sprite_2_y >= 0:
        sprite_2_y -= 10
    if keys[K_DOWN] and sprite_2_y <= HEIGHT - 100:
        sprite_2_y += 10

    window.blit(sprite_1, (sprite_1_x, sprite_1_y))
    window.blit(sprite_2, (sprite_2_x, sprite_2_y))

    clock.tick(FPS)
    display.update()