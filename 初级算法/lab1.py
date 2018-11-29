'''
初级算法：数组
从排序数组中删除重复项
'''
class Solution:
	def removeDuplicates(self,nums):
		if len(nums)==0:
			return None
		number=0
		for i in range(len(nums)):
			if nums[i]!=nums[number]:
				number+=1
				nums[number]=nums[i]
		return number+1

s=Solution()
nums=[1,1,2]
res=s.removeDuplicates(nums)
print(res)