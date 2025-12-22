class Solution(object):
    def majorityElement(self, nums):
        dic={}
        key=0
        value=0
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for a,b in dic.items():
            if b>=value:
                value=b
                key=a
        return key

        