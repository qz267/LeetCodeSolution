# Reverse Nodes in k-Group
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.

# If the number of nodes is not a multiple of k then left-out nodes in the
# end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

'''
Created on 2013-5-20
@author: Yubin Bai
'''


class ListNode:

    def __init__(self, value):
        self.next = None
        self.value = value


def generateList(data):
    if len(data) == 0:
        return None
    head = ListNode(data[0])
    curr = head
    for i in range(1, len(data)):
        curr.next = ListNode(data[i])
        curr = curr.next
    return head


def printList(head):
    curr = head
    result = []
    while curr != None:
        result.append(curr.value)
        curr = curr.next
    print(result)


def reverseKgroup(head, k):
    if head == None:
        return None

    newList = head
    newListTail = None

    currHead = head
    currTail = head
    counter = 1
    while currHead != None:
        currTemp = currHead
        currHead = currHead.next

        if counter == k:
            nextHead, nextTail = reverse(currTail, currTemp)
            if newList == head:
                newList = nextHead
                newListTail = nextTail
                nextTail.next = None
            else:
                newListTail.next = nextHead
                newListTail = nextTail
                newListTail.next = None
            currTail = currHead
            counter = 0

        counter += 1
    if newListTail != None:
        newListTail.next = currTail
    return newList


def reverse(head, tail):
    if head == None:
        return None
    if head == tail:
        return head
    oldList = head.next
    newList = head
    newList.next = None

    while oldList != tail:
        curr = oldList
        oldList = curr.next
        curr.next = newList
        newList = curr
    tail.next = newList
    return tail, head

if __name__ == '__main__':
    data = list(range(10))
    linked = generateList(data)
    printList(linked)
    linked2 = reverseKgroup(linked, 5)
    printList(linked2)
    linked2 = reverseKgroup(linked2, 5)
    printList(linked2)
