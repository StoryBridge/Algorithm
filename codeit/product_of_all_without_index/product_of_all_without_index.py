def product_of_all_without_index(some_list):
    # 코드를 쓰세요
    return_list = []    
    for i in range(0, len(some_list)):        
        temp = 1
        for j in range(0, len(some_list)):
            if i != j:
                temp = temp * some_list[j]
        return_list.append(temp) 
	return return_list
print(product_of_all_without_index([1, 7, 3, 4])) 
print(product_of_all_without_index([1, 8, 2, 3])) 
print(product_of_all_without_index([2, 6, 2, 2])) 
