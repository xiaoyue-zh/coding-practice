"""
题目：区间和
来源： https://kamacoder.com/problempage.php?pid=1070

算法：前缀和
思路： 创建一个前缀和数组，p[i]表示从0到i的和，那么区间[a,b]的和就是p[b]-p[a-1]，如果a=0，则直接返回p[b]

时间复杂度： O(n) 预处理前缀和数组，O(1) 查询每个区间和
空间复杂度： O(n)

备注： 注意读取数据的方式，尤其是大数据量的情况下，input()循环读取会很慢，建议使用 sys.stdin.read() 一次性读取所有数据，然后用指针控制进度。
"""


#
# import sys
# input = sys.stdin.read # 这里没加 ()，因为你不是要现在就读数据，你只是想把 sys.stdin.read 这个“员工”改名叫 input
# def main():
#     # 使用 sys.stdin.read().split() 一次性读取，防止 input() 循环读取太慢
#     data = input().split()
#     index = 0
#
#     # read array
#     n = int(data[index])
#     index += 1
#     vec = []
#     for i in range(n):
#         vec.append(int(data[index+i]))
#     # 为什么要用 index += n,这道题最麻烦的地方在于：后面还有数据！读完这n个数后，你还要读后面的 a b 区间对，所以这边用指针便宜量
#     index += n
#
#     # build presum array
#     p = [0] * n
#     presum = 0
#     for i in range(n):
#         presum += vec[i]
#         p[i] = presum
#
# read the interval in a loop
#     results = []
#     while index < len(data):
#         a = int(data[index])
#         b = int(data[index+1])
#         index += 2
#
#         if a == 0:
#             sum_value = p[b]
#         else:
#             sum_value = p[b] - p[a-1]   # 可以看示例自己算下
#
#         results.append(sum_value)
#
#     for result in results:
#         print(result)


# 加上这行代码后：你既可以把这个文件当成程序直接跑，又可以把它当成一个“库”安全地被别人引用，而不会触发任何意外的副作用。
# It prevents unintended execution when the file is imported as a module.
# 因为被别人import的时候这个属性等于另一个文件名
# 只放“只在直接运行时才需要执行的代码”，比如测试代码，demo，main逻辑。比如print(add(1, 2))
# if __name__ == "__main__":
#     main()

import sys
# 本地调试，改成普通的input()
def main():
    n = int(input())
    vec = []
    for _ in range(n):
        vec.append(int(input()))

    p = [0] * n
    presum = 0
    for i in range(n):
        presum += vec[i]
        p[i] = presum

    while True:
        try:
            a, b = map(int, input().split())
            if a == 0:
                print(p[b])
            else:
                print(p[b] - p[a - 1])
        except EOFError:
            break


if __name__ == "__main__":
    main()





