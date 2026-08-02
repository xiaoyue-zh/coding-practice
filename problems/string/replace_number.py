"""
题目: 替换数字
来源: https://kamacoder.com/problempage.php?pid=1064
算法: 
思路：遍历字符串，判断每个字符是否为数字，如果是则替换为"number"，否则保持不变。
时间复杂度: O(n^2)
空间复杂度: O(n)
"""
s = input().strip()

result = ""

for char in s:
    if char.isdigit():
        result += "number"
    else:
        result += char

print(result)


"""
算法: 双指针
思路：数组填充类，做法都是先预先给数组扩容带填充后的大小，然后在从后向前进行操作；
从前向后填充是O(n^2)的算法，因为每次添加元素都要将之后的所有元素整体向后移动。
时间复杂度: O(n)
空间复杂度: O(n)
"""
class Solution:
    def replaceDigits(self, s: str) -> str:
        count = sum(1 for char in s if char.isdigit())
        expanded_length = len(s) + count * 5 # # 计算扩充后字符串的大小， x->number， 每有一个数字就要增加五个长度
        result =[''] * expanded_length
        old_right, new_right = len(s) - 1, expanded_length - 1
        while old_right >= 0:
            if s[old_right].isdigit():
                result[new_right-5:new_right+1] = "number"
                new_right -= 6
            else:
                result[new_right] = s[old_right]
                new_right -= 1
            old_right -= 1
        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()

    while True:
        try:
            s = input().strip()
            result = solution.replaceDigits(s)
            print(result)
        except EOFError:
            break


