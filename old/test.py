a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
b = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "z"]


def joining_lists(*lists):
    answer = []
    max_len = 0
    for i in lists:
        if len(i) > max_len:
            max_len = len(i)
    for i in range(max_len):
        for l in lists:
            try:
                answer.append(l[i])
            except:
                pass
    return answer


joining_lists(a, b, a)