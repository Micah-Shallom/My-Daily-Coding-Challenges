// You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

// difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
// worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
// Every worker can be assigned at most one job, but one job can be completed multiple times.

// For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
// Return the maximum profit we can achieve after assigning the workers to the jobs.

// Example 1:

// Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
// Output: 100
// Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
// Example 2:

// Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
// Output: 0

package challenges

import "sort"


type mapping struct {
    diff int
    prof int
}

func maxProfitAssignment(difficulty []int, profit []int, worker []int) (res int ){

    pdMap := []mapping{}

    for i, val := range difficulty {
        pdMap = append(pdMap, mapping{ val, profit[i] })
    }

    sort.Slice(pdMap, func(i, j int)bool {
        return pdMap[i].diff < pdMap[j].diff
    })

    sort.Ints(worker)

    maxwork, j := 0, 0

    for i := 0; i < len(worker); i++ {
        // get max in loop range
        for j < len(difficulty) && worker[i] >= pdMap[j].diff {
            maxwork = max(maxwork, pdMap[j].prof)
            j++
        }
        res += maxwork
    }

    return
}