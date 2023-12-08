"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter


def frequencies(items):
    frequencies = {}
    # Your code goes here

    positive_list = [int(abs(number)) if isinstance(number, (int, float)) else number for number in items]

    string_list = [str(item) for item in positive_list]

    frequencies = dict(Counter(string_list))

    return frequencies
