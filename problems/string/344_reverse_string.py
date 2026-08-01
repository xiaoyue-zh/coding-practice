"""
题目: reverse string
来源: Leetcode 344
算法: double pointer

时间复杂度: O(n/2) = O(n)
空间复杂度: O(1), 空间复杂度只计算算法"额外申请"的空间，不计算输入本身占用的空间。
"""
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return 

# def main():
#     s = ["h", "e", "l", "l", "o"]

#     print("调用前:", s)

#     solution = Solution()
#     solution.reverseString(s)

#     print("调用后:", s)


# if __name__ == "__main__":
#     main()
