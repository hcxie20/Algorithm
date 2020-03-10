# 在第 7 道题我们写了倒置 int 的算法，这里当然可以用到了，只需要判断倒置前后相不相等就可以了。
# 记不记得，当倒置后的数字超出 int 的范围时，我们返回的是 0 ，那么它一定不等于原数，此时一定返回 false 了，这正不正确呢？
# 我们只需证明，如果倒置后超出 int 的范围，那么它一定不是回文数字就好了。
# 反证法，我们假设存在这么一个数，倒置后是超出 int 范围的，并且它是回文数字。
# int 最大为 2147483647 ,
# 让我们来讨论这个数可能是多少。
# 有没有可能是最高位大于 2 导致的溢出，比如最高位是 3 ，因为是回文串，所以最低位是 3 ，这就将导致转置前最高位也会是 3 ，所以不可能是这种情况。
# 有没有可能是第 2 高位大于 1 导致的溢出，此时保持最高位不变，假如第 2 高位是 2，因为是回文串，所以个位是 2，十位是 2 ，同样的会导致倒置前超出了 int 的最大值，所以也不可能是这种情况。
# 同理，第 3 高位，第 4，第 5，直线左边的都是上述的情况，所以不可能是前边的位数过大。
# 为了保证这个数是溢出的，前边 5 位必须固定不变了，因为它是回文串，所以直线后的灰色数字就一定是 4 ，而此时不管后边的数字取多少，都不可能是溢出的了。
# 综上，不存在这样一个数

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        if x == self.reverse(x):
            return True
        else:
            return False

    def reverse(self, x):
        rst = 0
        r = 0 # remainder

        while x != 0:
            x, r = divmod(x, 10)
            rst = rst * 10 + r
        
        if rst > 2 ** 31 - 1 or rst < -2 ** 31:
            return 0
        else:
            return rst

