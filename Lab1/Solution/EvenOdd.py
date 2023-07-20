import random


# Create a list of random integers
def createRandomList(N, R):
    numbers = [random.randint(0, R) for i in range(N)]
    return numbers


# Return the number of even and odd numbers
def countEvenOdd(num_list):
    tot_even = 0
    tot_odd = 0

    for num in num_list:
        if num % 2 == 0:
            tot_even += 1
        else:
            tot_odd += 1

    # Alternative using indexes
    #
    # for i in range(len(num_list)):
    #     if num_list[i] % 2 == 0:
    #         tot_even += 1
    #     else:
    #         tot_odd += 1

    return tot_even, tot_odd  # return two elements


# Separate even and odd numbers
def splitEvenOdd(num_list):
    even_list = []
    odd_list = []

    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    # Alternative using indexes
    #
    # for i in range(len(num_list)):
    #     current_num = num_list[i]
    #     if current_num % 2 == 0:
    #         even_list.append(current_num)
    #     else:
    #         odd_list.append(current_num)

    return even_list, odd_list


if __name__ == "__main__":
    N = 100
    R = 100
    numbers_list = createRandomList(N, R)
    print(numbers_list)

    even, odd = countEvenOdd(numbers_list)
    print("There are %d even numbers and %d odd numbers" % (even, odd))

    even_l, odd_l = splitEvenOdd(numbers_list)
    print("Even numbers are", even_l)
    print("Odd numbers are", odd_l)
