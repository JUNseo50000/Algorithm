'''
문제
리트코드 810.Most Common Word

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

* Example 1
- input
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
- output
"ball"
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
    mySolution
    '''
    def mostCommonWord(self, s: str, banned: List[str]) -> str:
        words = list()

        # IDEA : 받은 문자열을 쪼개고, loop에서 필요한 과정(소문자화, 온점과 반점 무시)을 거침
        for word in s.split():
            word = word.lower()
            # 문제 1에서 사용한 정규표현식 사용
            word = re.sub('[^a-z0-9]', '', word)
            # 일단 추가한 후, 후에 금지어일시 제거하는 방식
            words.append(word)

            for ban_word in banned:
                if word == ban_word:
                    words.remove(word)
                    continue

        # collections.Counter() 활용 <- Notion에서 딕셔너리 훑어보다 발견함
        word_frequency = collections.Counter(words)
        return word_frequency.most_common(1)[0][0]

    '''
    Solution 1
    use List Comprehension and Couter object
    '''
    def mostCommonWord_1(self, paragraph: str, banned: List[str]) -> str:
        '''
        정규표현식
        \w : Word Character
        ^ not

        r'[^\w]', ' ', paragraph -> Substitute all the letters, not the words to the blank.
        '''
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            # 깨끗한 paragraph를 얻고, 이를 split한다. (data cleansing)
            .lower().split()
                 # 이 또한 list comprehension을 통해 조건을 줄 수 있음.
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]


solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))