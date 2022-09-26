class Solution:
    def isValid(self, s: str) -> bool:
        correct = [('(','()'),('[','[]'),('{','{}')]
        # correct = [('(','()'),('[','[]'),('{','{}'),(')','()'),(']','[]'),('}','{}')]
        
        if len(s) % 2 != 0:
            return False
        
        steps = len(s) // 2
        z = 0
        for x in range(0, steps):
            for y in range(x+z, x+1+z):
                for idx,each in enumerate(correct):
                    if s[y] in correct[idx][0]:
                        if s[y+1] in correct[idx][1]:
                            return True
                        else:
                            return False
            z += 1
            # for y in range(0,len(s)):
                

if __name__=='__main__':
    fire = Solution()
    print(fire.isValid('()[)()'))