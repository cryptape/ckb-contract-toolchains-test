import matplotlib.pyplot as plt

def paint():
    data = [
        { "x": 1, "y": 161639 },   { "x": 2, "y": 38361 },  { "x": 3, "y": 32001 },
        { "x": 4, "y": 39999 },    { "x": 5, "y": 35252 },  { "x": 6, "y": 36748 },
        { "x": 7, "y": 40001 },    { "x": 8, "y": 40105 },  { "x": 9, "y": 33162 },
        { "x": 10, "y": 1622733 }, { "x": 11, "y": 40746 }, { "x": 12, "y": 34601 },
        { "x": 13, "y": 44653 },   { "x": 14, "y": 33033 }, { "x": 15, "y": 38967 },
        { "x": 16, "y": 40000 },   { "x": 17, "y": 32434 }, { "x": 18, "y": 34010 },
        { "x": 19, "y": 33404 },   { "x": 20, "y": 36151 }, { "x": 21, "y": 44055 },
        { "x": 22, "y": 35946 },   { "x": 23, "y": 33081 }, { "x": 24, "y": 41543 },
        { "x": 25, "y": 37376 },   { "x": 26, "y": 39999 }, { "x": 27, "y": 32001 },
        { "x": 28, "y": 31999 },   { "x": 29, "y": 32000 }, { "x": 30, "y": 33522 },
        { "x": 31, "y": 38478 },   { "x": 32, "y": 32001 }, { "x": 33, "y": 34514 },
        { "x": 34, "y": 37486 },   { "x": 35, "y": 32000 }, { "x": 36, "y": 31999 },
        { "x": 37, "y": 33424 },   { "x": 38, "y": 42041 }, { "x": 39, "y": 36772 },
        { "x": 40, "y": 33964 },   { "x": 41, "y": 37800 }, { "x": 42, "y": 40000 },
        { "x": 43, "y": 32824 },   { "x": 44, "y": 34512 }, { "x": 45, "y": 36664 },
        { "x": 46, "y": 40000 },   { "x": 47, "y": 33682 }, { "x": 48, "y": 34330 },
        { "x": 49, "y": 35987 },   { "x": 50, "y": 32000 }
    ]

    x_values = [d['x'] for d in data]
    y_values = [d['y'] for d in data]

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Coordinate Graph')
    plt.show()

if __name__ == '__main__':
    paint()