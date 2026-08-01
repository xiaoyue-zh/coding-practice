"""
题目: 开发商购买土地
来源: https://kamacoder.com/problempage.php?pid=1044
算法: 前缀和(Prefix Sum)
思路：枚举横向和纵向切分位置，利用前缀和快速计算两部分面积，取最小差值。

时间复杂度: O(n + m)
空间复杂度: O(n + m)
"""

# 核心思路：把二维降为一维
# 题目要求把矩阵分成两部分，且只能按横向或纵向划分。
# 横着切： 不管每一行里面长什么样，我们只关心“这一行总价值是多少”。
# 竖着切： 不管每一列里面长什么样，我们只关心“这一列总价值是多少”。
# 整个矩阵总和 = sum
# 切出来的一边总和 = horizontalCut
# 另一边总和 = sum - horizontalCut
# import sys
#
# input = sys.stdin.read
#
#
# def main():
#     data = input().split()
#     index = 0
#
#     n = int(data[index])
#     index += 1
#     vec = []
#     for i in range(n):
#         vec.append(int(data[index + i]))
#     index += n
#
#     p = [0] * n
#     presum = 0
#     for i in range(n):
#         presum += vec[i]
#         p[i] = presum
#
#     results = []
#     while index < len(data):
#         a, b = int(data[index]), int(data[index + 1])
#         index += 2
#
#         if a == 0:
#             results.append(p[b])
#         else:
#             results.append(p[b] - p[a - 1])
#
#     for result in results:
#         print(result)
#
#
# if __name__ == "__main__":
#     main()

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    sum = 0
    vec = []
    for i in range(n):
        row = []
        for j in range(m):
            num = int(data[idx])
            idx += 1
            row.append(num)
            sum += num
        vec.append(row)

    result = float('inf')

    count = 0
    # 行切分
    for i in range(n):

        for j in range(m):
            count += vec[i][j]
            # 遍历到行末尾时候开始统计
            if j == m - 1:
                result = min(result, abs(sum - 2 * count))

    count = 0
    # 列切分
    for j in range(m):

        for i in range(n):
            count += vec[i][j]
            # 遍历到列末尾时候开始统计
            if i == n - 1:
                result = min(result, abs(sum - 2 * count))

    print(result)


if __name__ == "__main__":
    main()

