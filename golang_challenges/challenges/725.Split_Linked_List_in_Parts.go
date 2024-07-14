// Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

// The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

// The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

// Return an array of the k parts.

 

// Example 1:

// Input: head = [1,2,3], k = 5
// Output: [[1],[2],[3],[],[]]
// Explanation:
// The first element output[0] has output[0].val = 1, output[0].next = null.
// The last element output[4] is null, but its string representation as a ListNode is [].

// Example 2:

// Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
// Output: [[1,2,3,4],[5,6,7],[8,9,10]]
// Explanation:
// The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.


package challenges


/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 func llSize(head *ListNode) (res int) {
    p := head 
    for p != nil {
        res++
        p = p.Next
    }
    return
}

func splitListToParts(head *ListNode, k int) []*ListNode {
    llst := []*ListNode{}
    size := llSize(head)

    // Determine the base size and the remainder
    div := size / k
    rem := size % k

    curr := head

    for cnt := 0; cnt < k; cnt++ {
        var new_head, prev *ListNode
        part_size := div
        
        if rem > 0 {
            part_size++
            rem--
        }

        for i := 0; i < part_size; i++ {
            if curr == nil {
                break
            }

            // Create a new node for this part
            new_node := &ListNode{Val: curr.Val}
            
            if new_head == nil {
                new_head = new_node // Set the head for the new part
            } else {
                prev.Next = new_node // Link the new node to the previous one
            }
            
            prev = new_node // Move the prev pointer

            curr = curr.Next // Move the curr pointer in the original list
        }

        llst = append(llst, new_head) // Append the new part to the result list
    }

    return llst
}
