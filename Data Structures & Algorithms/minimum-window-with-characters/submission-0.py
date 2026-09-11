class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = Counter(t)
        l = 0
        min_window = ""
        target_len = len(t)
        for r in range(len(s)):
            if target_count[s[r]] > 0:
                target_len -= 1
            target_count[s[r]] -= 1

            while target_len == 0:
                cur_window = s[l : r + 1]
                if not min_window or len(cur_window) < len(min_window):
                    min_window = cur_window
                target_count[s[l]] += 1
                if target_count[s[l]] > 0:
                    target_len += 1
                l += 1
        return min_window