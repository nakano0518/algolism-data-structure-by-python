# バケットソート
# 配列の構成を表現するカウンタ配列を作成し、
# カウンタ配列から得られる位置に要素を移動していくソート
# (メモ)
# カウンタ配列：ソートしたい配列の各要素の値が何回出現するか記録する配列
# 例) 配列A[1,4,2,0,3,2,2,4]のカウンタ配列は[1,1,3,1,2]
# 1. カウンタ配列の要素数は配列Aの最大値により決まる
# 2. カウンタ配列の累積和でカウンタ配列を更新して作成した新たなカウンタ配列は、配列Aの要素の移動すべき先を示す
#    ([1,1,3,1,2] -> 累積和で更新 -> [1,2,5,6,8])
# 3. 配列Aの後ろから見ていくと、最初は4であるので、4の移動先は、累積和で更新したカウンタ配列を見ると、
#    8の位置に移動すべきということがわかるので、ソート済み配列として用意した配列の8の位置に値を入れる
#    (ソート済み配列の位置は1から始まることに注意)
# 4. 移動したら累積和で更新したカウント配列の位置4の値を1減らす必要あり


def bucket_sort(arr):
    arrc = [0]*(max(arr)+1) # カウンタ配列
    # arrの各要素の出現数カウント
    for i in arr:
        arrc[i] += 1
    # 移動先となる累積和の計算
    for j in range(1, len(arrc)):
        arrc[j] = arrc[j] + arrc[j-1]
    # ソート先配列を用意し、代入していく
    arrs = [0]*len(arr)
    for i in reversed(arr): # 配列の後ろから要素をひとつづつ取り出し見ていく
        arrs[arrc[i]-1] = i # カウンタ配列の指定先が1始まりなので、-1して調整
        arrc[i] -= 1
    return arrs

if __name__ == '__main__':
    org_list = [17 ,11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(bucket_sort(org_list))
    