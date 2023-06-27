# Union of Two Linked Lists Python
- The union() function takes two linked lists, head1 and head2, as input and returns the head of the resulting union list.

- Inside the union() function, we define a dummy node (dummy) and a current node (curr) to keep track of the current position in the resulting union list. We also define a set (seen) to keep track of the distinct elements we have encountered so far.

- We iterate over the two input linked lists, head1 and head2, simultaneously until we reach the end of either list.

- For each iteration, we compare the values at the current positions of head1 and head2. If the value in head1 is less than the value in head2, we check if the value is already in the set seen. If it is not in the set, we add it to the union list by creating a new node with the value and updating the curr pointer. We also add the value to the seen set. Finally, we move the head1 pointer to the next node in the first list.

- Similarly, if the value in head2 is less than the value in head1, we perform the same steps as above, but with the head2 pointer and the second list.

- If the values in both head1 and head2 are equal, we follow the same steps as above, but we also move both head1 and head2 pointers to the next nodes in their respective lists.

- After reaching the end of either list, we add the remaining elements from the other list to the union list. We check if each value is already in the seen set before adding it to avoid duplicates.

- Now, we have the union list with all the distinct elements, but it may not be sorted in ascending order. To sort the list, we call the sortList() function, passing the dummy.next node (the first node in the union list) as the head.

- The sortList() function implements the merge sort algorithm to sort the linked list. It recursively splits the list into two halves, sorts each half separately using recursive calls, and then merges the sorted halves.

- The findMiddle() function is used to find the middle node of the list by using the slow and fast pointer technique.

- The merge() function merges two sorted linked lists into a single sorted linked list. It compares the values of the nodes from both lists and adds them to the result list in ascending order.

- Finally, the sortList() function returns the head of the sorted union list.

- The union() function returns the head of the sorted union list as the final output.

It merges the two linked lists into a single linked list, keeps track of distinct elements using a set, and then sorts the resulting list in ascending order using the merge sort algorithm.
