unsorted_list = [9,8,3,6,8,9,6,1,4,2]

def bubble_sort(lst):
    length = len(lst) - 1
    while length != -1:
        for i in range(length):
            if lst[i + 1] < lst[i]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
        length -= 1
    return lst

print(bubble_sort(unsorted_list))