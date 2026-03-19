# -*- coding: utf-8 -*-
# @Time    : 2026/3/19
# @Author  : 你的名字
# @File    : 01_linked_list_basic.py
# @Desc    : 单向链表的基础实现（增、删、查、遍历）


# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点存储的值
        self.next = next  # 指向下一个节点的指针


# 定义单向链表类
class LinkedList:
    def __init__(self):
        self.head = None  # 链表头节点，初始为空

    # 在链表尾部添加节点
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:  # 如果链表为空，新节点就是头节点
            self.head = new_node
            return
        current = self.head
        while current.next:  # 遍历到最后一个节点
            current = current.next
        current.next = new_node  # 把新节点挂在最后

    # 在链表头部添加节点
    def prepend(self, val):
        new_node = ListNode(val)
        new_node.next = self.head  # 新节点的 next 指向原头节点
        self.head = new_node  # 新节点成为新的头节点

    # 删除指定值的节点
    def delete(self, val):
        if not self.head:  # 链表为空，直接返回
            return
        # 如果要删除的是头节点
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # 跳过要删除的节点
                return
            current = current.next

    # 查找指定值的节点
    def search(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    # 遍历打印链表所有节点
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


# 测试代码
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print("链表初始状态：")
    ll.print_list()  # 输出: 0 -> 1 -> 2 -> 3 -> None

    ll.delete(2)
    print("删除值为 2 的节点后：")
    ll.print_list()  # 输出: 0 -> 1 -> 3 -> None

    print("查找值为 3 的节点：", ll.search(3))  # 输出: True
    print("查找值为 5 的节点：", ll.search(5))  # 输出: False
