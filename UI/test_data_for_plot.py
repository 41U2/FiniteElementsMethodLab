class Point:

    def __init__(self, x_input, y_input, value_input):
        self.x = x_input
        self.y = y_input
        self.value = value_input


class TestDataForPlot:

    def __init__(self):
        self.test_data = [Point(1, 1, 70), Point(2, 1, 100), Point(3, 1, 30), Point(4, 1, 70),
                          Point(1, 2, 150), Point(2, 2, 150), Point(3, 2, 120), Point(4, 2, 120),
                          Point(1, 3, 170), Point(2, 3, 170), Point(3, 3, 170), Point(4, 3, 170)]
