# x are columns
# y are rows
def down(y):
    y += 1
    return y


def up(y):
    y -= 1
    return y


def left(x):
    x -= 1
    return x


def right(x):
    x += 1
    return x


def right_diagnol_up(x, y):
    x -= 1
    y += 1
    return x, y


def right_diagnol_down(x, y):
    x += 1
    y += 1
    return x, y


def left_diagnol_up(x, y):
    x -= 1
    y -= 1
    return x, y


def left_diagnol_down(x, y):
    x += 1
    y -= 1
    return x, y


class Move:
    # array:input
    row_dictionary = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
    # input: array
    col_dictionary = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

    def __init__(self, startsq, endsq):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]

    # converting input, output to iteratable values
    def moving_input_coordinates(self):
        temp_input = list()
        for x, y in self.row_dictionary.items():
            if y == self.startrow:
                temp_input.append(x)

        for x, y in self.col_dictionary.items():
            if x == self.startcol:
                temp_input.append(y)
        return temp_input

    def moving_output_coordinates(self):
        temp_output = list()
        for x, y in self.row_dictionary.items():
            if y == self.endrow:
                temp_output.append(x)

        for x, y in self.col_dictionary.items():
            if x == self.endcol:
                temp_output.append(y)
        return temp_output

    def covert_output_coordinates(self, new_output):
        temp_output = list()
        for x, y in self.row_dictionary.items():
            if x == new_output[0]:
                temp_output.append(y)

        for x, y in self.col_dictionary.items():
            if y == new_output[1]:
                temp_output.append(x)
        return temp_output




