def count_matching_elements(matrix, elem):
    n =0

    for row in matrix:
        for cell in row:
            if cell == elem:
                n +=1
    return n

if __name__ == "__main__":
    test_cases = (([[1,2,3],[2,3,1],[4,5,6]], 2), ([[1,5,5,3],[2,5,2,5],[0,0,2,5]], 5), ([[1,2,3,4],[2,3,4,5],[3,4,6,5]], 6))

    for test in test_cases:
        print(count_matching_elements(test[0],test[1]))