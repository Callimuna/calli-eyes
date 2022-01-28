def bewege_Pupille():
    while True:
        led.plot(1, 3)
        basic.pause(500)
        led.plot(2, 3)
        led.unplot(1, 3)
        basic.pause(700)
        led.plot(3, 3)
        led.unplot(2, 3)
        basic.pause(400)
        led.plot(2, 3)
        led.unplot(3, 3)
        basic.pause(500)
        led.unplot(2, 3)

def on_button_pressed_a():
    global seite
    seite = 0
    images.create_image("""
        . . # # #
        . # . . #
        # . . . #
        # . . . #
        # # # # #
        """).show_image(0)
    bewege_Pupille()
input.on_button_pressed(Button.A, on_button_pressed_a)

def bewegeLid():
    led.plot(1, 1)
    led.plot(2, 1)
    led.plot(3, 1)
    basic.pause(1400)
    led.plot(1, 2)
    led.plot(2, 2)
    led.plot(3, 2)
    basic.pause(1000)
    led.unplot(1, 2)
    led.unplot(2, 2)
    led.unplot(3, 2)
    basic.pause(2000)
    if seite == 1:
        led.unplot(1, 1)
    else:
        led.unplot(3, 1)
    led.unplot(2, 1)
    basic.pause(500)

def on_button_pressed_b():
    global seite
    seite = 1
    images.create_image("""
        # # # . .
        # . . # .
        # . . . #
        # . . . #
        # # # # #
        """).show_image(0)
    bewege_Pupille()
input.on_button_pressed(Button.B, on_button_pressed_b)

seite = 0
seite = -1
"""

Hack zur Synchronisation der Lider

"""

def on_forever():
    if seite != -1:
        bewegeLid()
basic.forever(on_forever)
