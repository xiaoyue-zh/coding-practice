n = int(input()) 这种写法在笔试中同样受欢迎，且更易读
arr = [int(x) for x in input().split()] 或者 arr = list(map(int, input().split()))[:n] 也可以
下面的写法本质上是把整个输入文件当作一个巨大的字符串流（Stream），然后通过一个指针（index）手动控制进度。
这种方式在处理海量数据（比如 10^5 以上）时，比 input() 循环快得不止一点点。
这种方法避免了多次调用 input() 产生的系统调用开销。在 Python 这种解释型语言里，减少系统调用次数是提速的关键