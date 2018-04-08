class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        l = num[0] 
        ans = 1
        tmp = 1
        for n in num:
            if(n - l == 0):
                continue;
            elif(n - l == 1):
                tmp += 1
            else:
                if tmp > ans:
                    ans = tmp
                tmp = 1
            l = n
        if tmp > ans:
            ans = tmp
        return ans

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in xrange(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    print Solution().longestCommonPrefix(["hello", "heaven", "heavy"])


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")