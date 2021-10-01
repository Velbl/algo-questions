class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        letters = {}
        head = 0
        tail = -1
        result = 0

        while head < len(s):
            if s[head] in letters:
                tail = max(tail, letters[s[head]])
            letters[s[head]] = head
            result = max(result, head - tail)
            head += 1
        return result


s = "abcaba"
sol = Solution()
length = sol.length_of_longest_substring(s)

print(length)
