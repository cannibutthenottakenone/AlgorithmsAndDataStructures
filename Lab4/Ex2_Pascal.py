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
# NOTE: You can use iterative loop(s) inside recursion


def pascal(n):
    if n == 0:
        return [1]

    above=pascal(n-1)
    below=[1]

    for i in range(len(above)-1):
        below.append(above[i]+above[i+1])
    
    below.append(1)

    return below

if __name__ == "__main__":
    n = 8
    for i in range(n+1):
        print(pascal(i))

