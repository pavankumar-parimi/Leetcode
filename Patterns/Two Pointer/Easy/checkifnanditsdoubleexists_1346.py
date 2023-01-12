def checkIfExist(self, arr: List[int]) -> bool:
    for index, each in enumerate(arr):
        if each % 2 == 0:
            if int(each / 2) in arr[:index] or int(each / 2) in arr[index + 1:]:
                return True
    return False