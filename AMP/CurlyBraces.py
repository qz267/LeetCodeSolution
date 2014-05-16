__author__ = 'zhengqin'


class Solution(object):
    """
    Question: Curly braces can be used in programming to provide scope-limit. Write a function to print
    all valid( properly opened and closed) combinations of n-pairs of curly braces.
    Example:
    input: 1 output: {}
    input: 2 output: {}{}, {{}}
    input: 3 output: {}{}{}, {}{{}}, {{}}{}, {{}{}}, {{{}}}
    input: 4 output: {}{}{}{}, {}{}{{}}, {}{{}}{}, {}{{}{}}, {}{{{}}},
    {{}}{}{}, {{}}{{}}, {{}{}}{}, {{}{}{}}, {{}{{}}}, {{{}}}{}, {{{}}{}}, {{{}{}}}, {{{{}}}}
    """