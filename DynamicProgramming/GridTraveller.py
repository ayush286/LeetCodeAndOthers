# O(mn) Time | O(mn) Space, where m and n are inputs
def gridTraveller(m, n):
    table = [[0 for row in range(m + 1)] for col in range(n + 1)]
    table[1][1] = 1
    for row in range(m + 1):
        for col in range(n + 1):
            #  sum to the right
            if col != n:
                table[row][col + 1] += table[row][col]
            #  sum to the down
            if row != m:
                table[row + 1][col] += table[row][col]
    return table[m][n]


if __name__ == '__main__':
    # print(gridTraveller(1, 1))
    # print(gridTraveller(2, 3))
    # print(gridTraveller(3, 2))
    # print(gridTraveller(3, 3))
    print(gridTraveller(18, 18))
