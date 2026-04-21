class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        

        for c1, c2 in zip(s_sorted, t_sorted):
            if c1 != c2:
                return False

        return True