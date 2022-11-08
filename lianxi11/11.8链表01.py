# 链表算法

"""
定义Node类
创建一个数据域-存储每个结点的值
创建一个指针域-存储下一个结点的地址
"""


# 初始化结点函数的实现
class Node:
    # 初始化结点函数
    def __init__(self, data):
        self.data = data
        self.next = None


"""
创建单链表的头结点
"""


# 初始化头结点函数的实现
class SingleLinkedList:
    def __init__(self):
        self.head = Node(None)

    # 创建单链表函数的实现
    def CreateSingleLinkedList(self):
        print("***********")
        print("请输入数据后按回车键确认，若想结束请输入#。")
        print("***********")
        cNode = self.head
        Element = input('请输入当前结点的值：')
        while Element != '#':
            nNode = Node(int(Element))
            cNode.next = nNode
            cNode = cNode.next
            Element = input("请输入当前结点的值：")

    # 尾端插入元素函数的实现
    def InsertElementInTail(self):
        Element = (input("请输入待插入结点的值："))
        if Element == '#':
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != None:
            cNode = cNode.next
        cNode.next = nNode                  # 时间复杂度  O(n)

    # 首端插入元素函数的实现
    def InsertElementInhead(self):
        Element = input("请输入待插入结点的值：")
        if Element == '#':
            return
        cNode = self.head
        nNode = Node(int(Element))
        nNode.next = cNode.next
        cNode.next = nNode                  # 时间复杂度   O(1)

    # 查找指定元素并返回其位置函数的实现
    def FindElement(self):
        Pos = 0
        cNode = self.head
        key = int(input("请输入想要查找的元素值："))
        if self.IsEmpty():
            print("当前单链表为空")
            return
        while cNode.next != None and cNode.data != key:
            cNode = cNode.next
            Pos = Pos+1
        if cNode.data == key:
            print("查找成功，值为：", key, "所在的结点位置于该单链表的第", Pos, "个位置")
        else:
            print("查找失败，当前该链表中不存在值为", key, "的元素")

    # 判断单链表是否为空函数
    def IsEmpty(self):
        if self.GetLength() == 0:
            return True
        else:
            return False

    # 获取的单链表长度函数
    def GetLength(self):
        cNode = self.head
        length = 0
        while cNode.next != None:
            length = length+1
            cNode = cNode.next
        return length

    # 删除元素函数的实现
    def DeleteElement(self):
        dElement = int(input("请输入待删除结点的值："))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print("当前单链表为空")
            return
        while cNode.next != None and cNode.data != dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            pNode.next = cNode.next
            del cNode
            print("成功删除含有元素", dElement, "的结点")
        else:
            print("删除失败，当前单链表中不存在含有元素", dElement, "的结点")

    # 遍历单链表函数的实现
    def TraverseElement(self):
        cNode = self.head
        if cNode.next == None:
            print("当前单链表为空")
            return
        print("您当前的单链表为：")
        while cNode != None:
            cNode = cNode.next
            self.VisitElement(cNode)

    # 输出单链表某一元素函数
    def VisitElement(self, tNode):
        if tNode != None:
            print(tNode.data, "->", end=" ")
        else:
            print("None")