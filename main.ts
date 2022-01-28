function bewege_Pupille () {
    while (true) {
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
    }
}
input.onButtonPressed(Button.A, function () {
    seite = 0
    images.createImage(`
        . . # # #
        . # . . #
        # . . . #
        # . . . #
        # # # # #
        `).showImage(0)
    bewege_Pupille()
})
function bewegeLid () {
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
    if (seite == 1) {
        led.unplot(1, 1)
    } else {
        led.unplot(3, 1)
    }
    led.unplot(2, 1)
    basic.pause(500)
}
input.onButtonPressed(Button.B, function () {
    seite = 1
    images.createImage(`
        # # # . .
        # . . # .
        # . . . #
        # . . . #
        # # # # #
        `).showImage(0)
    bewege_Pupille()
})
let seite = 0
seite = -1
/**
 * Hack zur Synchronisation der Lider
 */
basic.forever(function () {
    if (seite != -1) {
        bewegeLid()
    }
})
