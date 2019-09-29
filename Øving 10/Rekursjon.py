#a)
def recursive_sum(n):
    print("recursive_sum has been called with n = " + str(n))
    if n == 0:
        return 0
    else:
        res = n + recursive_sum(n-1)
        print("intermediate result for ", n, " + recursive_sum(", n-1, "): ", res)
        return res

print(recursive_sum(5))

#b)
def minst(a, b):
    if a < b:
        return a
    return b


def find_smallest_element(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return minst(numbers[0], find_smallest_element(numbers[1:]))

numbers = [9,5,5,10,6,8,15,5,6]
print(find_smallest_element(numbers))

#c
#sorted_numbers = numbers.sort()
sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("\n\n\n\n\n\n")
def binarySearch(numbers, element):
    midten = len(numbers)//2
    if len(numbers) == 1 and element not in numbers:
        return (-float('inf'))
    if element == numbers[midten]:
        return midten
    elif element > numbers[midten]:
        print(numbers[midten+1:])
        return midten + 1 + binarySearch(numbers[midten+1:], element)
    elif element < numbers[midten]:
        print(numbers[:midten])
        return binarySearch(numbers[:midten], element)

print(binarySearch(sorted_numbers, 9))


