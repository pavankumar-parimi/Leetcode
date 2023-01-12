class TwoSum:

    def __init__(self):
        self.arr_map = {}

    def add(self, number: int) -> None:
        if number in self.arr_map:
            self.arr_map[number] += 1
        else:
            self.arr_map[number] = 1

    def find(self, value: int) -> bool:

        for index, num in enumerate(self.arr_map):
            val = value - num
            if val != num and val in self.arr_map:
                return True
            else:
                if val == num:
                    if self.arr_map[val] > 1:
                        return True
        return False