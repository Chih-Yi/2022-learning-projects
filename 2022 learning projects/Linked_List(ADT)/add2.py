"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    l3 = ListNode(0, None)
    cur_lst = l3
    cur_lst.val = (l1.val + l2.val) % 10
    add_num = 0
    if (l1.val + l2.val) // 10 == 1:
        add_num = 1
    l1 = l1.next
    l2 = l2.next
    while l1 is not None and l2 is not None:
        add_node = ListNode((l1.val + l2.val + add_num) % 10, None)
        cur_lst.next = add_node
        cur_lst = cur_lst.next
        if (l1.val + l2.val + add_num) // 10 == 1:
            add_num = 1
        else:
            add_num = 0
        l1 = l1.next
        l2 = l2.next
    if l1 is not None:
        while l1 is not None:
            add_node = ListNode((l1.val + add_num) % 10, None)
            cur_lst.next = add_node
            cur_lst = cur_lst.next
            if (l1.val + add_num) // 10 == 1:
                add_num = 1
            else:
                add_num = 0
            l1 = l1.next
    if l2 is not None:
        while l2 is not None:
            add_node = ListNode((l2.val + add_num) % 10, None)
            cur_lst.next = add_node
            cur_lst = cur_lst.next
            if (l2.val + add_num) // 10 == 1:
                add_num = 1
            else:
                add_num = 0
            l2 = l2.next
    if add_num == 1:
        cur_lst.next = ListNode(1, None)
    return l3


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
