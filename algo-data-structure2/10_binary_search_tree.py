# 二分探索木は、タプルで表現する場合とクラスで表現する場合がある

# (1) BinarySearchTreeクラスを作成し、接点を挿入するinsert()メソッドを定義せよ
# BinarySearchTreeクラスは、インスタンス生成の際に根の値を渡すことで、
# 二分探索木を表現するインスタンスを生成できるクラスで、insert()メソッドは、
# インスタンス.insert(5)というように、その二分探索木に5が挿入されるようなメソッドであるとする。
# (2) (1)で作成した二分探索木をinorder()メソッドを定義し中間順巡回により昇順出力せよ。
# (3) 二分探索木を探索するメソッドであるsearch()メソッドを定義せよ。
# ただし、searchメソッドは、インスタンス.search(5)と実行した場合、
# 5が二分探索木に含まれる場合は「yes」、含まれない場合は「no」と出力するメソッドであるとする。
# (4) 二分探索木を削除するメソッドであるdelete()メソッドを定義せよ。
# ただし、deleteメソッドは、インスタンス.delete(5)と実行した場合、
# 5を二分探索木から削除するメソッドであるとする

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 解答をここから
class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def insert(self, key):
        node = self.root
        while True: #挿入位置が決定するまで
            if node.value > key:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left
            elif node.value <= key:
                if node.right is None:
                    node.right = Node(key)
                    return
                node = node.right
                
    def inorder(self, node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
    def search(self, key):
        node = self.root
        while True:
            if node.value == key:
                print("yes")
                return
            elif node.value > key:
                node = node.left
            else:
                node = node.right
            if node is None:
                print("no")
                return
    # 削除は「削除対象のノードがいくつ子を持つか」で場合分けする
    # 子を持たない場合、子を左に一つ持つ場合、子を右に一つ持つ場合、子を2つもつ場合の4つである
    
    

# 解答ここまで

t = BinarySearchTree(7)
t.insert(3)
t.insert(9)
t.insert(1)
t.insert(5)
t.inorder(t.root)
t.search(5)
t.search(4)
t.search(9)