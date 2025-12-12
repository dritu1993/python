color_table = pd.DataFrame({color : [black, brown, red, orange, yellow, green, blue, violet, grey, white],
                            values : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    )

def label(colors):
    R = 0
    for color in colors:
        v = color_table.loc['color']
        R+= 10
