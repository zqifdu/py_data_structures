'''
---
Author:         Zhenyi Qi
Date created:   2018-02-11
'''



def longest_common_subsequence(s1, s2):
    '''
    Find the longest common subsequence of s1 and s2

    Parameters
    ----------
    s1: The first sequence
    s2  The second sequence

    Returns
    -------
    1. s:
        a table of points which indicates where the optimal subproblem solution comes from
    2. len_lcs:
        the length of the longest subsequence of prefixs of s1 and s2

    '''
    m = len(s1)
    n = len(s2)
    s = [[0]*(n+1) for count in range(m+1)]
    len_lcs = [[0]*(n+1) for count in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                len_lcs[i][j] = len_lcs[i-1][j-1]+1
                s[i][j] = 'ul'
            elif len_lcs[i-1][j]>= len_lcs[i][j-1]:
                len_lcs[i][j] = len_lcs[i-1][j]
                s[i][j] = 'up'
            elif len_lcs[i-1][j] < len_lcs[i][j-1]:
                len_lcs[i][j] = len_lcs[i][j-1]
                s[i][j] = 'left'

    print_lcs(s1, s, m, n)
    return s, len_lcs



def print_lcs(s1, s, i, j):
    '''
    Recursively print the longest common subsequence

    Parameters
    ----------
    s1  : one of the string
    s   : solution table
    i   : row index of subproblem solution table
    j   : column index of subproblem solution table

    Returns
    -------

    '''
    if i == 0 or j == 0:
        return

    elif s[i][j] == 'ul':
        print_lcs(s1, s, i-1, j-1)
        print(s1[i-1], end = '')

    elif s[i][j] == 'up':
        print_lcs(s1, s, i-1, j)

    elif s[i][j] =='left':
        print_lcs(s1, s, i, j-1)









