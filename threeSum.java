public List<List<Integer>> threeSum(int[] nums) {
	List<List<Integer>> result = new ArrayList<> ();
	if (nums == null || nums.length < 3) return result;
	Arrays.sort(nums);

	int len = nums.length;
	for (int i = 0; i < len; i++){
		if (i > 0 && nums[i] == nums[i - 1]) continue;
		int target = 0 - nums[i];
		int j = i + 1, k = len - 1;
		while (j < k){
			if (nums[j] + nums[k] == target){
				result.add(Arrays.asList(nums[i], nums[j], nums[k]));
				while (j < k && nums[j] == nums[j + 1]) j++;
				while (j < k && nums[k] == nums[k - 1]) k--;
				j++; k--;
			} else if(nums[j] + nums[k] < target){
				j++;
			} else {
				k--;
			}
		}
	}
	return result;
}