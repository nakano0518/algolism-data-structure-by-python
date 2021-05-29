# クイックソート
# ピボット(軸)を選び、ピボットを基準に分割、を再帰的に行うソート

# quick_sort関数を定義
# 1. ソート対象の配列のピボットを基準に2つの部分配列に分割
# 2. 前方の部分配列に対してquick_sortを行う
# 3. 後方の部分配列に対してquick_sortを行う
# 4. 整列済み部分配列とピボットを連結して返す
# 終了条件は、分割した部分配列の要素数が1になったとき

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    p = arr[0]
    arrf, arrb = divide(p, arr[1:])
    return quick_sort(arrf) + [p] + quick_sort(arrb)

def divide(p ,arr):
    left = []
    right = []
    for i in arr:
        if i < p:
            left.append(i)
        else:
            right.append(i)
    return left, right

if __name__ == '__main__':
    org_list = [17 ,11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(quick_sort(org_list))