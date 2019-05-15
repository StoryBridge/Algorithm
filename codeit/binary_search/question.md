이진 탐색 알고리즘을 이미 반복문으로는 구현해 보셨죠? 이번에는 재귀적으로 문제를 해결해 보세요.

반드시 재귀(recursion)의 개념을 사용하셔야 합니다. 코드 구현이 꽤 어려우니, 천천히 고민해 보시기 바랍니다. 다른 재귀 문제를 풀 때와 마찬가지로 base case와 recursive case를 생각해 내는 것이 핵심입니다!

def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
0
None
2
1
4
