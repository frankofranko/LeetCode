__author__ = 'HsinYeh Lin'

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        string_list = s.split()
        if len(string_list) == 0:
            return ""
        elif len(string_list) == 1:
            return string_list[0]
        else:
            answer = string_list[-1]
            for index in range(len(string_list)-2,-1,-1):
                answer += " " + string_list[index]
            return answer

string = "My name is Vicki"
print string

test = Solution()
print test.reverseWords(string)