def sum_of_range(start, end):
    # 코드를 작성하세요
    # base case
    if start == end:
        return end
    # recursion case    
    return start + sum_of_range(start+1, end)

print(sum_of_range(2, 10)) 
print(sum_of_range(11, 16)) 
print(sum_of_range(1, 5))
