# 選択ソート
# 先頭の要素、それ以降の要素の中から最小値を見つけ先頭要素と交換
# 先頭の要素の次の要素、それ以降の要素の中から最小値を見つけ先頭の要素の次の要素と交換
# 繰り返す

def selection_sort(arr):
    for i in range(len(arr)):
        select_min(arr, i)

def select_min(arr, i):
    min = i
    for j in range(i+1,len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[min], arr[i] = arr[i], arr[min]

if __name__ == '__main__':
    org_list = [17 ,11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    selection_sort(org_list)
    print(org_list)