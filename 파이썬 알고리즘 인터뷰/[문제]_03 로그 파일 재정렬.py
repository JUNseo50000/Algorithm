'''
문제
리트코드 937.Reorder Log Files

로그를 재정렬하라. 기준은 다음과 같다.
    1. 로그의 가장 앞 부분은 식별자다.
    2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
    3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
    4. 숫자 로그는 입력 순서대로 한다.

* Example 1
- input
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
- output
["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

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
    def ReorderLogFiles(self, s: List[str]) -> List[str]:
        # IDEA : letter_logs와 digit_logs를 분리하고 향후에 합치자
        letter_logs = []
        digit_logs = []
        for log in s:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # print(letter_logs)
        # print(digit_logs)

        # IDEA : sort key lambda를 이용해서, 원하는 조건으로 정렬하자
        letter_logs.sort(key=lambda x: x.split()[1:])
        # 숫자로그는 입력순으로 한다.
        # digit_logs.sort(key=lambda x: x.split()[1:])
        return letter_logs + digit_logs

    '''
    Solutoin 1
    use lambda and '+' operator
    '''
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 한줄로 예쁘게 표현하기 참고
        letters, digits = [], []
        # 내 풀이와 동일
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 나는 문자가 동일한 경우, 식별자 순 조건을 추가하지 않았음.
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits


logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
solution = Solution()
print(solution.ReorderLogFiles(logs))