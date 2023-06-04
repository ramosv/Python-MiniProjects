
def matrix_sum():
    row = row_sums()
    result = 0
    for num in row:
        result +=num
    return result


def matrix_max():
    matrix = reading_file("matrix.txt")
    result = 0
    for row in matrix:
        for num in row:
            if int(num) > result:
                result = int(num)

    return result


def row_sums():
    matrix = reading_file("matrix.txt")
    result = []
    for lists in matrix:
        to_add = 0
        for num in lists:
            to_add += int(num)
        result.append(to_add)
    return result

def reading_file(file):
    func = []
    with open(file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            num = line.split(",")
            func.append(num)
    return func


if __name__ == "__main__":
    #reading_file("matrix.txt")
    row_sums()