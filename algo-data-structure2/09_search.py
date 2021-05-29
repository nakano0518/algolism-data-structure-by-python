# 探索
# 配列[1,2,5,8,10]において、ランダムに選択される数字n(nは1以上10以下の整数)が
# 配列に含まれる場合はその位置(インデックス番号)を、
# 含まれない場合はNoneを出力するプログラムを作成せよ


# 線形探索
def linear_search(arr):
    for i in range(0, len(arr)):
        if key == arr[i]:
            return i
    return None

if __name__ == '__main__':
    import random
    key = random.randint(1, 10)
    print(str(key)+"が含まれるかチェック")
    s_list = [1, 2, 5, 8, 10]
    print(linear_search(s_list))
    

# 二分探索(ソート済みの配列なら二分探索のほうが速い)
def binary_search(arr):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid
        else:
            left = mid + 1
    return None

if __name__ == '__main__':
    import random
    key = random.randint(1, 10)
    print(str(key)+"が含まれるかチェック")
    s_list = [1, 2, 5, 8, 10]
    print(binary_search(s_list))           
        
    