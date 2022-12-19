class Point:

    def __init__(self, x_input, y_input, value_input):
        self.x = x_input
        self.y = y_input
        self.value = value_input


class TestDataForPlot:

    def __init__(self):
        self.test_data = [Point(1, 1, 0.2), Point(2, 1, 0.3), Point(3, 1, 0.2), Point(4, 1, 0.7),
                          Point(1, 2, 0.45), Point(2, 2, 0.8), Point(3, 2, 0.7), Point(4, 2, 0.3),
                          Point(1, 3, 0.9), Point(2, 3, 0.5), Point(3, 3, 0.2), Point(4, 3, 0.8)]
