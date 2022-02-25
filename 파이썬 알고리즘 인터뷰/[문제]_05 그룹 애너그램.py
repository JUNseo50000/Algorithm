'''
문제
리트코드 49.ㅎ개ㅕㅔ 뭄ㅎㄱ믄

문자열 배열을 받아 애너그램 단위로 그룹핑하라.

* Example 1
- input
["eat", "tea", "tan", "ate", "nat", "bat"]
- output
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]
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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # IDEA : 딕셔너리안에 딕셔너리를 넣는다.
        # outer dict -> key : 단어, value : 그 단어를 이루는 letter 숫자들
        # inner dict -> key : letter, value : frequency
        word_dict_list = dict()
        for word in strs:
            # use collections.defaultdict
            word_dict = collections.defaultdict(int)
            for letter in word:
                word_dict[letter] += 1

            word_dict_list[word] = word_dict

        # IDEA : 딕셔너리 비교 연산자를 사용한다. loop 돌린다.
        anagrams = list()
        while len(word_dict_list) > 0:
            anagram = list()
            pop_word = word_dict_list.popitem()
            anagram.append(pop_word[0])
            for word in word_dict_list.keys():
                if pop_word[1] == word_dict_list[word]:
                    anagram.append(word)
                    # word_dict_list를 이용해 loop를 돌고 있는데, word_dict_list element를 변경하니 이상해짐
                    # word_dict_list.remove(word)
            # 따라서, loop가 끝난후 제거하기
            for word in anagram:
                if word != pop_word[0]:
                    del word_dict_list[word]

            anagrams.append(anagram)

        return anagrams

    '''
    Solution 1
    Add to dict after sorting
    '''
    # IDEA : 문자들을 정렬하면, 같은 값을 가진다. -> 사실 아이디어 자체는 내꺼와 동일한데..
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        # 존재하지 않는 key 넣어도 에러가 나지 않도록 항상 default로 생성하는 습관
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가 <- 잘 살펴보자
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


