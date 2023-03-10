def rectangle(length, width):
    def rect_area():
        return length * width

    def rect_perimeter():
        return (2 * length) + (width * 2)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f'''Rectangle area: {rect_area()}
Rectangle perimeter: {rect_perimeter()}'''

print(rectangle(2, 10))





print(rectangle(2, 10))