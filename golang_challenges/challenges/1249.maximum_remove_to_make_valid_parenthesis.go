package challenges

func minRemoveToMakeValid(s string) string {
    stack := []int{} //this will track the index of non-valid parenthesis
    hashMap := map[int]rune{} //this will contain each char of the string s with its index as key so we can use the values in stack to know what parenthesis to remove

    for i, c := range s {
        if c == '('{
            stack = append(stack, i)
        }else if c == ')' && len(stack) > 0{ // if the current char is ) and len of stack is not 0 then it means that we have a ( inside and proceed to remove the index of ( 
            stack = stack[:len(stack) - 1]
        }else if c == ')' { //adding a ) is not allowed at all
            continue
        }
        hashMap[i] = c //add all idx to character mappings into the hashmap
    }

    res := ""
    for i := 0 ; i < len(s);  i++ {
        if len(stack) > 0 && i == stack[0] {
            stack = stack[1:]
            continue
        }
        if c , exists := hashMap[i]; exists {
            res += string(c)
        }
    }
    
    return res
}