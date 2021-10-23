resistor_colors = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey': 8,
    'white': 9,
}
def color_code(color):
    return resistor_colors[color]


def colors():
    color_list = ([color for color, value in resistor_colors.items() if value == resistor_colors[color]])
    return color_list
    
