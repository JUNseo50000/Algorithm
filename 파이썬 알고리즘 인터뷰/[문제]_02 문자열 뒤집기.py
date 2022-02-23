'''
문제
리트코드 344. Reverse String

문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

* Example 1
- input
["h", "e", "l", "l", "o"]
- output
["o", "l", "l", "e", "h"]

* Example 2
["H", "a", "n", "n", "a", "h"]
"race a car"
- output
["h", "a", "n", "n", "a", "H"]

'''

# LeetCode Default import
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    '''
    my Solution
    '''
    def reverseString(self, s: list):
        length = len(s)
        # IDEA : C의 ptr change 사용
        for i in range(length//2):
            temp_char = s[length-1-i]
            s[length-1-i] = s[i]
            s[i] = temp_char

    '''
    Solution 1
    Swap using two pointer
    '''
    # List[str] & -> None 사용 참고
    def reverseString_1(self, s:List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            # IDEA : Python swap is easier than C
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    '''
    Solution 2
    Pythonic Way
    '''
    # List[str] & -> None 사용 참고
    def reverseString_1(self, s:List[str]) -> None:
        # reverse()는 List에만 제공된다.
        s.reverse()
        # 만약 문자열일 경우
        s = s[::-1]
        # 리트코드 자체 공간복잡도 설정 때문에 에러가 날 경우
        s[:] = s[::-1]


string = ["H", "a", "n", "n", "a", "h"]
solution = Solution()
solution.reverseString(string)
print(string)