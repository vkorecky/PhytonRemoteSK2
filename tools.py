class API:
    @classmethod
    def get_data(cls):
        with open("nums.txt", 'r') as file:
            lines = file.read().splitlines()
        return lines  # ['1, 1', '1.5, 0.5', '10, 100']


def load_nums_from_file():
    nums = []
    lines = API.get_data()
    for line in lines:
        # line = '1, 1'
        pair = line.split(",")  # ["1", " 1"]
        if len(pair) == 2:
            x = float(pair[0].strip())
            y = float(pair[1].strip())
            nums.append((x, y))
    return nums  # [(1, 1), (1.5, 0.5), (10, 100)]
