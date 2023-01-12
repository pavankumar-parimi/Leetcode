def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
    l = len(sensor1)
    i = 0
    j = 0
    Flag = False

    while i < l and j < l:
        if l - 1 == i and l - 1 == j and sensor1[i] != sensor2[j]:
            Flag = True
            break

        if sensor1[i] == sensor2[j]:
            i += 1
            j += 1
        else:
            pos_i = i
            pos_j = j

            while pos_i < l and j < l:
                if pos_i + 1 < l and sensor1[pos_i + 1] == sensor2[j]:
                    pos_i += 1
                    j += 1
                else:
                    if pos_i + 1 < l:
                        return 1
                    else:
                        if pos_i + 1 >= l:
                            break
                        else:
                            return 2

            while i < l and pos_j < l:
                if pos_j + 1 < l and sensor1[i] == sensor2[pos_j + 1]:
                    i += 1
                    pos_j += 1
                else:
                    if pos_j + 1 < l:
                        return 2
                    else:
                        if pos_j + 1 >= l:
                            break
                        else:
                            return 1

            return -1

    if Flag or (i == l and j == l):
        return -1