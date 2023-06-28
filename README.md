# Union of Two Linked Lists Python

The provided code demonstrates a solution to merge and sort two linked lists. It consists of several classes and functions that work together to achieve the desired outcome.

The Solution class contains a single method called union. This method takes two linked lists, head1 and head2, as input and returns a new linked list that contains all the unique elements from both input lists, sorted in ascending order.

The union method first creates a dummy node and sets the current and seen variables to keep track of the merged list and the values encountered so far, respectively. It then iterates through the nodes of the first linked list (head1) and checks if each node's data is not present in the seen set. If the data is unique, a new node is created and added to the merged list. The value is also added to the seen set. The process is repeated for the second linked list (head2).

After merging the two lists, the union method calls the sortList method to sort the merged list. The sortList method uses the merge sort algorithm to recursively split the list into two halves, sort each half separately, and then merge the sorted halves using the merge method.

The findMiddle method is a helper function used by sortList to find the middle node of a linked list. It uses the slow and fast pointer approach, where the slow pointer moves one step at a time and the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer points to the middle node.

The merge method is another helper function used by sortList to merge two sorted linked lists into a single sorted list. It compares the data values of the nodes in the two lists and adds them to the new merged list in ascending order. The method also ensures that any remaining nodes from either list are properly connected to the merged list.

The Node class represents a single node in the linked list. Each node contains a data attribute to store the value and a next attribute to point to the next node in the list.

The LinkedList class is responsible for managing the linked list. It has a head attribute that points to the first node in the list and a tail attribute that points to the last node. The class provides an insert method to add new nodes to the end of the list.

In the main part of the code, two input arrays (arr1 and arr2) are provided, and the elements from these arrays are inserted into separate linked lists (ll1 and ll2) using the LinkedList class. An instance of the Solution class (ob) is created, and the union method is called with the heads of the two linked lists as arguments. Finally, the resulting merged and sorted linked list is printed using the printList function.

In summary, the code takes two linked lists, merges them into a single list while removing duplicates, sorts the merged list using merge sort, and returns the sorted list as the union of the two input lists..
