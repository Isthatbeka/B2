from graph import *
import math

windowSize(794, 1123)
canvasSize(794, 1123)
# фон
penColor(0, 102, 129)
brushColor(0, 102, 129)
rectangle(0, 416, 794, 1123)

penColor(27, 27, 121)
brushColor(27, 27, 121)
rectangle(0, 0, 794, 84)

penColor(142, 95, 212)
brushColor(142, 95, 212)
rectangle(0, 85, 794, 135)

penColor(206, 136, 223)
brushColor(206, 136, 223)
rectangle(0, 135, 794, 215)

penColor(223, 136, 172)
brushColor(223, 136, 172)
rectangle(0, 215, 794, 315)

penColor(225, 134, 84)
brushColor(225, 134, 84)
rectangle(0, 315, 794, 416)


def kogot(x0, y0, m):
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    ellips(x0, y0, 7, 5)
    u = 2

    penColor(27, 27, 121)
    brushColor(27, 27, 121)
    ellips(x0, y0 + u, 7, 5)


# elipse
def ellips1(x0, y0, a, b, ang):
    x = -a
    h = 0.4
    t = math.radians(ang)
    points1 = []
    points2 = []
    while x < a:
        y = b * math.sqrt(1 - (x ** 2 / a ** 2))
        xe1 = x0 - (x * math.cos(t) - y * math.sin(t))
        xe2 = x0 + (x * math.cos(t) - y * math.sin(t))
        ye1 = y0 + (x * math.sin(t) + y * math.cos(t))
        ye2 = y0 - (x * math.sin(t) + y * math.cos(t))
        points1.append((xe1, ye1))
        points2.append((xe2, ye2))
        x += h
    polygon(points1)
    polygon(points2)


def ellips(x0, y0, a, b):
    x = -a
    h = 0.2
    points = []
    while x <= a:
        y = b * math.sqrt(1 - (x ** 2 / a ** 2))
        xe = x0 + x
        ye1 = y0 - y
        ye2 = y0 + y
        points.append((xe, ye1))
        points.append((xe, ye2))
        x += h
    polygon(points)


def ptichka3(x0, y0, m):
    penColor(255, 255, 255)
    ellips(x0, y0, 30, 15)
    r = 60
    u = 4
    ellips(x0 + r, y0, 30, 15)
    penColor(206, 136, 223)
    ellips(x0, y0 + u, 30, 15)
    ellips(x0 + r, y0 + u, 30, 15)


ptichka3(375, 160, 1.5)


def ptichka1(x0, y0, m):
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    ellips1(x0, y0, 30, 15, 15)
    r = 60
    u = 4
    j = 20
    r1 = 50
    ellips1(x0 + r - u, y0 - j, 30, 15, 15)
    penColor(27, 27, 121)
    brushColor(27, 27, 121)
    ellips1(x0, y0 + u, 30, 15, 15)
    ellips1(x0 + r - u, y0 + u - j, 30, 15, 15)


ptichka1(70, 60, 1)


def pelikan(x0, y0, m):
    penColor(255, 222, 84)
    brushColor(255, 222, 84)

    def kogot(x0, y0, m):
        penColor(255, 222, 84)
        brushColor(255, 222, 84)
        ellips(x0, y0, 10 * m, 5 * m)
        u = 3
        penColor(0, 102, 129)
        brushColor(0, 102, 129)
        ellips(x0, y0 + u * m, 10, 5)

    kogot(x0 + 115, y0 + 95, 1.2)
    kogot(x0 + 112, y0 + 98, 1)
    penColor(255, 222, 84)
    brushColor(255, 222, 84)
    ellips1(x0 + 101, y0 + 104, 7, 4, 90)
    kogot(x0 + 109, y0 + 101, 1)

    kogot(x0 + 85, y0 + 115, 1.2)
    kogot(x0 + 82, y0 + 118, 1)
    penColor(255, 222, 84)
    brushColor(255, 222, 84)
    ellips1(x0 + 76, y0 + 125, 7, 4, 90)
    kogot(x0 + 80, y0 + 121, 1)

    # nogaszadi
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    ellips1(x0 + 20, y0 + 50, 30, 20, 125)
    ellips1(x0 + 70, y0 + 80, 40, 10, 160)

    # noga
    ellips1(x0 - 10, y0 + 60, 40, 25, 120)
    ellips1(x0 + 40, y0 + 100, 40, 10, 160)
    # хвост
    polygon([(x0 - 125, y0 - 50), (x0 - 125, y0 + 10), (x0 - 70, y0 - 10), (x0 - 125, y0 - 50)])
    ellips1(x0 - 124, y0 - 20, 30, 10, 90)

    # cluv
    penColor(255, 222, 84)
    brushColor(255, 222, 84)
    ellips(x0 + 190 * m, y0 - 35 * m, 40 * m, 10 * m)
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    line(x0 + 170, y0 - 35, x0 + 230, y0 - 35)
    # kryliya zadnie
    penColor(0, 0, 0, )
    ellips1(x0 - 10, y0 - 65, 41, 31, 115)
    ellips1(x0 - 60, y0 - 120, 51, 18, 165)
    ellips1(x0 - 105, y0 - 143, 16, 6, 111)
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    ellips1(x0 - 10, y0 - 65, 40, 30, 115)
    ellips1(x0 - 60, y0 - 120, 50, 17, 165)
    ellips1(x0 - 105, y0 - 143, 15, 5, 111)
    # krylya pered
    penColor(0, 0, 0, )
    ellips1(x0 - 70, y0 - 55, 51, 31, 120)
    ellips1(x0 - 120, y0 - 100, 51, 14, 165)
    ellips1(x0 - 170, y0 - 120, 16, 6, 130)
    penColor(255, 255, 255)
    ellips1(x0 - 70, y0 - 55, 50, 30, 120)  # закрывает
    ellips1(x0 - 120, y0 - 100, 50, 13, 165)
    ellips1(x0 - 170, y0 - 120, 15, 5, 130)

    # golova
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    ellips(x0 + 155 * m, y0 - 35 * m, 40 * m, 20 * m)
    # glaz i liniya
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    ellips(x0 + 170 * m, y0 - 45 * m, 5 * m, 4 * m)

    # telo
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    ellips(x0, y0, 90 * m, 40 * m)
    ellips(x0 + 90 * m, y0 - 15, 40 * m, 15 * m)


pelikan(250, 500, 1)
run()
