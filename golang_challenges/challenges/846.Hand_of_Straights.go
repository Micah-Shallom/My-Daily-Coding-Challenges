// Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

// Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
 

// Example 1:

// Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
// Output: true
// Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
// Example 2:

// Input: hand = [1,2,3,4,5], groupSize = 4
// Output: false
// Explanation: Alice's hand can not be rearranged into groups of 4.

 

// Constraints:

// 1 <= hand.length <= 104
// 0 <= hand[i] <= 109
// 1 <= groupSize <= hand.length

package challenges


func isNStraightHand(hand []int, groupSize int) bool {
	if len(hand) % groupSize != 0 {
		return false
	}
	
	//create a hashmap to store the frequency of each card
	cardMap := map[int]int{}
	for _, card := range hand {
		cardMap[card]++
	}
	
	//loop through the cardMap and for each card, check if the card is in the cardMap and if the card is in the cardMap, reduce the frequency of the card by 1 and check if the next card is in the cardMap and if it is, reduce the frequency of the next card by 1 and continue this process until the groupSize is exhausted.
	for len(cardMap) > 0 {
		var start int
		for k := range cardMap {
			start = k
			break
		}
		
		for i := 0; i < groupSize; i++ {
			if cardMap[start + i] == 0 {
				return false
			}
			cardMap[start + i]--
			if cardMap[start + i] == 0 {
				delete(cardMap, start + i)
			}
		}
	}
	
	return true
}