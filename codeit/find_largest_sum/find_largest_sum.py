def find_largest_sum(list1, list2):
    # 코드를 작성하세요
    largest_sum = list1[0] + list2[0]
    for i in list1:
        for j in list2:
            if i + j > largest_sum:
                largest_sum = i+j
	return largest_sum
print(find_largest_sum([1, 2, 3], [4, 3, 1]))
print(find_largest_sum([10, 6, 8], [4, 3, 6]))
print(find_largest_sum([10, 16, 20], [20, 23, 4]))
