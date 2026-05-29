class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for num in nums:
            add=0
            while num>0:
                digit=num%10
                add+=digit
                num=num//10
            arr.append(add)
        return min(arr)