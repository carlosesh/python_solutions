"""
2114. Maximum Number of Words Found in Sentences
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

Example:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
"""


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_max = 0
        for sentence in sentences:
            sentence_max = len(re.findall(r"[a-zA-Z]+", sentence))
            word_max = sentence_max if sentence_max > word_max else word_max

        return word_max