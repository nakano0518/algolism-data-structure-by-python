# マージソート

# n個の要素を含む配列を、それぞれn/2個の要素を含む2つの部分配列に分割するプロセスを再帰的に繰り返す
# 上記の終了条件は、分割により一つの要素の配列になったとき
# 分割とともに統合のプロセスを再帰的に実施する
# 分割した配列の先頭同士を比較し小さい方を先頭要素に採用、その要素を除いた残りの分割した配列同士をさらに比較し小さい方を先頭要素に採用をマージするのを再帰的に繰り返す
# 上記の終了条件は、分割した配列のいずれかが空になるとき(にそのもうひとつの配列は要素数1なのでそれをreturnする)

# 分割プロセス
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# 統合プロセス
def merge(arrf, arrb):
    if len(arrf) < 1:
        return arrb
    if len(arrb) < 1:
        return arrf
    if arrf[0] <= arrb[0]:
        return [arrf[0]] + merge(arrf[1:], arrb) # (参考) +演算子は新しいリストを作成する。元のリストの状態は保たれる
    else:
        return [arrb[0]] + merge(arrf, arrb[1:])


if __name__ == '__main__':
    org_list = [17 ,11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(merge_sort(org_list))