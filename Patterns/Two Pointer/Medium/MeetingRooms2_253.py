def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    j = 1
    l = len(intervals)
    temp_arr = []
    temp_arr.append(intervals[0])
    t_l = 1
    Flag = False

    while j < l:
        i = 0
        while i < t_l:
            if temp_arr[i][0] <= intervals[j][0] < temp_arr[i][1]:
                i += 1
            else:
                temp_arr[i] = intervals[j]
                Flag = True
                i += 1
                break

        if not Flag:
            temp_arr.append(intervals[j])
            t_l += 1
        Flag = False
        j += 1

    return t_l