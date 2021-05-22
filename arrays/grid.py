from array_class import Array
import random


class Grid:
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)

        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def get_item(self, index):
        return self.data[index]

    def __str__(self):
        result = ''

        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + " "

            result += '\n'

        return str(result)

    def random_fill(self, lower, upper):
        """Fill Grid whi random integer whit upper and lower items

        Args:
            lower (int): min number of random
            upper (int): max number of random
        """
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                self.data[row][column] = random.randint(lower, upper)


class Cube:
    def __init__(self, block_size, row_size, column_size, fill_value=None):
        self.data = Array(row_size, fill_value)

        for row in range(row_size):
            self.data[row] = Array(column_size, fill_value)

        for row in range(row_size):
            for column in range(column_size):
                self.data[row][column] = Array(block_size, fill_value)

    def get_item(self, index):
        return self.data[index]

    def row_size(self):
        return len(self.data)

    def column_size(self):
        return len(self.data[0])

    def block_size(self):
        return len(self.data[0][0])

    def __str__(self):
        result = ''
        for row in range(self.row_size()):
            for column in range(self.column_size()):
                for block in range(self.block_size()):
                    result += str(self.data[row][column][block]) + " "
            result += '\n'
        return result

    def fill_random(self, min, max):
        for row in range(self.row_size()):
            for col in range(self.column_size()):
                for block in range(self.block_size()):
                    self.data[row][col][block] = random.randint(min, max)


if __name__ == "__main__":
    matrix = Grid(3, 3)
    print(matrix)
    matrix.random_fill(4, 15)
    print(matrix)

    cube = Cube(3, 4, 4)
    print(cube.row_size())
    print(cube.column_size())
    print(cube.block_size())
    cube.fill_random(0, 255)
    print(cube)
