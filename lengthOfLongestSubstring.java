//two different methods

public int lengthOfLongestSubstring(String s){
	int n = s.length();
	Set<Character> set = new HashSet<>();
	int ans = 0, i = 0, j = 0;
	while (i < n && j < n){
		if (!set.contains(s.charAt(j))){
			set.add(s.charAt(j++));
			ans = Math.max(ans, j - i);
		}else{
			set.remove(s.charAt(i++));
		}
	}
	return ans;
}

public int lengthOfLongestSubstring(String s){
	int n = s.length(), ans = 0;
	Map<Character, Integer> map = new HashMap<>();
	for (int i = 0, j = 0; j < n; j++){
		if (map.containsKey(s.charAt(j))){
			i = Math.max(map.get(s.charAt(j)), i);
		}
		ans = Math.max(ans, j - i + 1);
		map.put(s.charAt(j), j + 1);
	}
	return ans;

//int[128] for ASCII
public int lengthOfLongestSubstring(String s){
	int n = s.length(), ans = 0;
	int[] index = new int[128];
	for (int i = 0, j = 0; j < n; j++){
		i = Math.max(index[s.charAt(j)], i);
		ans = Math.max(ans, j - i + 1);
		index[s.charAt(j)] = j + 1;
	}
	return ans;
}