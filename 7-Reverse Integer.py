__author__ = 'HsinYeh Lin'

class Solution:
    # @return an integer
    def reverse(self, x):
        number_list = list(str(x))
        if number_list[0] == "-":
            number_list.remove("-")
            number_list.append("-")
        while number_list[-1] == "0" and len(number_list) != 1:
            number_list.pop()
        answer = ""
        for index in range(len(number_list)-1,-1,-1):
            answer += number_list[index]
        answer = int(answer)
        return answer

number = -0
print list(str(number))

test = Solution()
print test.reverse(number)