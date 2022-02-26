'''
문제
리트코드 5.Longest Palindrome Substring

가장 긴 팰린드롬 부분 문자열을 출력하라.

* Example 1
- input
"babad"
- output
"bab"

- input
"cbbd"
- output
"bb"

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
    가장 큰 범위의 팰린드롬부터 역순으로 추적해가는 방식 -> time out (28ms)
    '''
    def longestPalindrome(self, s: str) -> str:
        # IDEA1 : 정말 앞뒤로 모든 loop를 도는 방법. O(n^2)보다 간단한 방법이 생각이 안났다 (일종의 투포인터)
        # 물론, 이미 길이 2의 팰린드롬이 나오면 그보다 짧은 범위로 안가게 한다던가 하는 스킬이 있기야하겠지만.. 큰 의미는 없을 듯
        # for start_letter in s:
        #     for end_letter in reversed(s):
        # if문으로 조건을 줘도 for문을 계속 중첩하여 설정해야할 거 같아 포기함. + 문자열은 slicing으로 하는 것이 빠르다는 것도 까먹음

        # IDEA2 : 가장큰 글자수의 팰린드롬부터 역순으로 찾아본다.
        longest_palindrome = ""
        str_length = len(s)
        for length in reversed(range(str_length)):
            for i in range(str_length - length):
                sliced_str = s[i:length+i+1]
                if sliced_str == sliced_str[::-1]:
                    longest_palindrome = sliced_str
                    break
            if len(longest_palindrome) > 0:
                break

        return longest_palindrome

    '''
    Solution
    focusing on the center
    '''
    # Longes Common Substring -> 전형적인 DP 문제
    # 하지만 이문제의 경우, DP가 더 비직관적이고 느리다.
    def longestPalindrome_1(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        # 이해는 가지만, 이걸 즉석에서 떠올릴 수 있을까?
        # 스피드의 핵심은, 아닌 부분은 빠르게 통과하고,(3칸짜리 2칸짜리로 빠르게 확인하면서)
        # 맞는 부분에서 효율적으로 팰린드롬을 확장해나가는 것(왼쪽 오른쪽 동시 확장)
        return result

Solution = Solution()
print(Solution.longestPalindrome("cbbdbbc"))