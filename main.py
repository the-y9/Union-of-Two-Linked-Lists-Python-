# Solution class to define union function
class Solution:
    def union(self, head1, head2):
        # Merge the two linked lists into a single linked list
        curr = dummy = Node(None)
        seen = set()
        # Add nodes from the first linked list
        while head1:
            if head1.data not in seen:
                curr.next = Node(head1.data)
                seen.add(head1.data)
                curr = curr.next
            head1 = head1.next
        
        # Add nodes from the second linked list
        while head2:
            if head2.data not in seen:
                curr.next = Node(head2.data)
                seen.add(head2.data)
                curr = curr.next
            head2 = head2.next
        
        # Sort the linked list in ascending order
        dummy = dummy.next
        sorted_head = self.sortList(dummy)
        
        return sorted_head

    def sortList(self, head):
        if head is None or head.next is None:
            return head
        
        # Split the list into two halves
        mid = self.findMiddle(head)
        mid_next = mid.next
        mid.next = None

        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(mid_next)

        # Merge the sorted halves
        sorted_head = self.merge(left, right)
        
        return sorted_head

    def findMiddle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = Node(None)
        curr = dummy
        while left and right:
            if left.data < right.data:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        if right:
            curr.next = right
        
        return dummy.next



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next

if __name__ == '__main__':
    n1 = 6
    arr1 = [9, 6, 4, 2, 3, 8]
    ll1 = LinkedList()
    for i in arr1:
        ll1.insert(i)

    n2 = 5
    arr2 = [1, 2, 8, 6, 2]
    ll2 = LinkedList()
    for i in arr2:
        ll2.insert(i)

    ob = Solution()
    printList(ob.union(ll1.head, ll2.head))
