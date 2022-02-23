'''
문제
리트코드 125. Valid Palindrome

주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며,
영문자와 숫자만을 대상으로 한다.

* Example 1
- input
"A man, a plan, a canal: Panama"
- output
true

* Example 2
- input
"race a car"
- output
true

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
    풀이 1
    리스트로 변환
    '''
    def isPalindrome_1(self, s: str) -> bool:
        strs = []
        # IDEA : 입력받은 문자열에서, isalnum을 이용해 영문과 숫자만 걸러낸 배열을 이용하기
        for char in s:
            # isalnum() : 영문자, 숫자 여부를 판별하는 함수
            if char.isalnum():
                strs.append(char.lower())

        # print(strs)

        # IDEA : pop 함수를 이용하여 앞뒤를 간편하게 차례대로 비교하기
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    '''
    풀이2
    데크 자료형을 이용한 최적화
    '''
    def isPalindrome_2(selfself, s:str) -> bool:
        # Deque : 양방향 Q
        # strs: <- from typing 가져옴(타입 명시)
        strs: Deque = collections.deque()

        # IDEA : 알고리즘 자체는 같으나 list의 앞뒤에서 자료를 빼오고 있으니까 이럴꺼면 Deque를 쓰자는 아이디어
        # pop(0) : O(n) & popleft() : O(1)
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

    '''
    풀이3
    슬라이싱 사용
    '''
    def isPalindrome_3(self, s: str) -> bool:
        s = s.lower()
        # IDEA : 정규식을 통해 원하는 얘들만 사용 (isalnum으로 하나하나 점검보다 빠름)
        # 정규식
        s = re.sub('[^a-z0-9]', '', s)

        # slicing
        # IDEA : 문자열을 조작할 때는 슬라이싱 유념하기
        return s == s[::-기]




string = "ab,cdcba"
solution = Solution()
print(solution.isPalindrome(string))