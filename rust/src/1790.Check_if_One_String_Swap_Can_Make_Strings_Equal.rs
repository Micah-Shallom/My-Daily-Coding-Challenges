impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        if s1.len() != s2.len(){
            return false;
        }

        let mut diff = Vec::new();
        let s1: Vec<char> = s1.chars().collect();
        let s2: Vec<char> = s2.chars().collect();

        for i in 0..s1.len() {
            if s1[i] != s2[i] {
                diff.push(i);
            }

            if diff.len() > 2 {
                return false;
            }
        }

        if diff.len() == 0{
            return true;
        }

        if diff.len() == 2 {
            return s1[diff[0]] == s2[diff[1]] && s1[diff[1]] == s2[diff[0]];
        }

        return false;
    }
}
