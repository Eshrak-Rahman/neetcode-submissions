class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        
        for index,number in enumerate(nums):
            
            needed=target-number
            if needed in my_dict:
                first=my_dict[needed]
                second=index
                return [first,second]
            my_dict[number]=index
                
