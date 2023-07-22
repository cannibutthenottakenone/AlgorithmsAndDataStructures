# Compute the Pascal's Triangle using recursion
#
#         1           n = 0
#       1   1         n = 1
#     1   2   1       n = 2
#   1   3   3   1     n = 3
# 1   4   6   4   1   n = 4
# ...
#
# You can print the triangle like this:
#
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# ...
#

def pascal(n):

    if n == 0:
        return [1]

    previous_line = pascal(n-1)

    line = [1]

    size = len(previous_line)-1

    for i in range(size):
        current = previous_line[i] + previous_line[i + 1]
        line.append(current)

    line.append(1)

    return line


if __name__ == "__main__":
    n = 4

    for i in range(n + 1):
        print(pascal(i))

