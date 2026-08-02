Mistakes:
1. Used range(min(i + k, len(s))) instead of range(i, min(i + k, len(s))).
   → Forgot that range() needs the correct starting index.

2. Wrote back with range(i + k) instead of range(i, end).
   → Accidentally overwrote from index 0.

Takeaway:
When processing a subarray, always define:
start = i
end = min(i + k, n)

**Python slicing is safe**
If the end index exceeds the length, Python simply returns everything up to the end.
```
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        1. 使用range(start, end, step)来确定需要调换的初始位置
        2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
        3. 用切片整体替换，而不是一个个替换.
        """
        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text
        
        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])
        
        return ''.join(res)
```

```
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Two pointers. Another is inside the loop.
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s
```
s[:p]: ""
if p2 >= len(s), s[p2:]: ""
Strings are immutable; Immutable does not mean "can't change the variable." It means "the object itself cannot be modified after it is created.";you can slice them and concatenate the pieces to create a new string.

底层实现：切片-生成新字符串-没有任何变量再引用的旧对象变成unreachable object最后被垃圾回收机制释放

```
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        chars = list(s)
        
        while i < len(chars):
            chars[i:i + k] = chars[i:i + k][::-1] # 反转后，更改原值为反转后值
            i += k * 2

        return ''.join(chars)
```
