package challenges

import "fmt"

func maxprofit(prices []int) int {
	minPrice := prices[0]
	maxProfit := 0
	for _, current_price := range prices {
		if current_price < minPrice {
			minPrice = current_price
		} else {
			maxProfit = max(maxProfit, current_price-minPrice)
		}
	}
	return maxProfit
}

func MaxProfit() {
	prices := []int{7, 1, 3, 4, 3, 4, 5}
	fmt.Println(maxprofit(prices))
}
