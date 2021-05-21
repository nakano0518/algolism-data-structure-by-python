# バブルソート
# リストの末尾から隣接要素を見ていき(終点は1ずつ増える)、大小関係が逆なら交換する

def buble_sort(arr):
    for i in range(0, len(arr)-1): # 末尾から見ていくときの終点
        for j in range(len(arr)-1, i, -1): # 末尾から見ていく
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

if __name__ == '__main__':
    org_list = [17 ,11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    buble_sort(org_list)
    print(org_list)