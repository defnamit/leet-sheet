class Solution(object):
    def shortestBeautifulSubstring(self, s, k):

        s_list = list(map(int, str(s)))
        out = s_list

        for i in range(len(s_list)):
            for j in range(i + 1, len(s_list) + 1):

                if sum(s_list[i:j]) == k:
                    current = s_list[i:j]

                    if (len(current) < len(out)) or \
                       (len(current) == len(out) and current < out):
                        out = current

        if out == s_list:
            return ""

        return "".join(map(str, out))
