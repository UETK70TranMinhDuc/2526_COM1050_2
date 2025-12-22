class Solution(object):
    def containsDuplicate(self, nums):
        dic={}
        a=0
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                 dic[i]=1
        for k in dic.values():
            if k>1:
                a+=1
        if a==0 :
            return False
        else:
            return True