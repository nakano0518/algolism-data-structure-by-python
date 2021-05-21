# 挿入ソート
# 先頭要素をソート済みとする
# 未ソート部分がなくなるまで下記処理を繰り返す
# 1. 未ソート部分の先頭から要素を取り出しtmpに記録
# 2. ソート済み部分において、tmpよりも大きい要素を後方へ1つずつ移動させる
# 3. 最後に空いた位置にtmpを挿入する

def insert_sort(arr):
    for i in range(1, len(arr)):
        insert(arr, i)

def insert(arr, i):
    tmp = arr[i]
    for j in range(i-1, -1, -1):
        if tmp < arr[j]:
            arr[j+1] = arr[j]
        else:
            arr[j+1] = tmp
            break
    else:
        arr[0] = tmp

if __name__ == '__main__':
    org_list = [17 ,11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    insert_sort(org_list)
    print(org_list)