class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dic={}
        for k in s:
            if k in dic:
                dic[k]+=1
            else:
                dic[k]=1
        for k in t:
            if k not in dic:
                return False
            dic[k]-=1
            if dic[k]<0:
                return False
        return True