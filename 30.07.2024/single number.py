class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        j={}

        for i  in nums :
            if i not in j :
                j[i]=1
            else :
                j[i]+=1

        for i in j:
            if j[i]==1:
                return i