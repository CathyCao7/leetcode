#median，head
import heapq
def __init__(self):
	self.small = []
	self.large = []

def addNum(self,num):
	if len(self.small) == len(self.large):
		heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
	else:
		heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

def findMedian(self):
	if len(self.small) == len(self.large):
		return float(self.large[0] - self.small[0]) / 2.0
	else:
		retun float(self.large[0])

#median, not understand
class Solution(object):
	def findMedianSortedArrays(self,nums1,nums2):
		len1, len2 = len(nums1),len(nums2)
		if (len1 +len2) % 2 == 1:
			return self.getKth(nums1, nums2, (len1 + len2)/2 + 1)
		else:
			return (self.getKth(nums1, num2, (len1 + len2)/2) + self.getKth(nums1, nums2, (len1 + len2)/2 + 1)) * 0.5

	def getKth(self, A, B, k):
		m, n = len(A), len(B)
		if m > n:
			return self.getKth(B, A, k)

		left, right = 0, m
		while left < right:
			mid = left +(right - left) / 2
			if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
				right = mid
			else:
				left = mid + 1

		Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
		Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

		return max(Ai_minus_1, Bj)

#another answer of median
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0

#quickselect
import random
class Solution:
	def findKthLargest(self, nums, k):
		pivot = random.choice(nums)
		nums1, nums2 = [],[]
		for num in nums:
			if num > pivot:
				nums1.append(num)
			elif num < pivot:
				nums2.append(num)
		if k <= len(nums1):
			return self.findKthLargest(nums1,k)
		if k > len(nums) - len(nums2):
			return self.findKthLargest(nums2, k - (len(nums)- len(nums2)))
		return pivot

#排序
def findKthLargest(self, nums, k):
	return sorted(nums, reverse = True)[k - 1]

#Minimum Index Sum of Two Lists
def findRestaurant(self, list1, list2):
	dict1 = {v : i for i, v in enumerate(list1)}
	minSum = len(list1) + len(list2)
	ans = []
	for i, r in enumerate(list2):
		if r not in dict1:
			continue
		currSum = i + dict1[r]
		if currSum < minSum:
			ans = [r]
			minSum = currSum
		elif currSum == minSum:
			ans.append(r)
	return ans

def findRestaurant(self, A, B):
	Aindex = {u: i for i,u in enumerate(A)}
	best,ans = 1e9,[]

	for j,v in enumerate(B):
		i = Aindex.get(v, 1e9) #
		if i + j < best:
			best = i + j
			ans = [v]
		elif i + j == best:
			ans.append(v)
	return ans


