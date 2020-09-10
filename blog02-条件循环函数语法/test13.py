def bubble_sort(list):
    count = len(list)
    for i in range(count):
        for j in range(i + 1, count):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

#排序算法
list = [3, 91, 23, 14, 56, 9]
print("排序前:", list)
res = bubble_sort(list)
print("排序后:", res)
