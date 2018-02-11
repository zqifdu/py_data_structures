'''
test file for dynamic programming functions
'''
import unittest
from dynamic_programming.rod_cutting import *
from dynamic_programming.matrix_chain_multiplication import *
from dynamic_programming.longest_common_subsequence import *

class dpTests(unittest.TestCase):
    def test_buttom_up_cut_rod(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual(bottom_up_cut_rod(p, 1), 1)
        self.assertEqual(bottom_up_cut_rod(p, 2), 5)
        self.assertEqual(bottom_up_cut_rod(p, 3), 8)
        self.assertEqual(bottom_up_cut_rod(p, 4), 10)
        self.assertEqual(bottom_up_cut_rod(p, 5), 13)
        self.assertEqual(bottom_up_cut_rod(p, 6), 17)
        self.assertEqual(bottom_up_cut_rod(p, 7), 18)
        self.assertEqual(bottom_up_cut_rod(p, 8), 22)
        self.assertEqual(bottom_up_cut_rod(p, 9), 25)
        self.assertEqual(bottom_up_cut_rod(p, 10), 30)


    def test_buttom_up_cut_rod_solution(self):
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual(bottom_up_cut_rod_solution(p, 10), [0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10])


    def test_matrix_chain(self):
        p = [30, 35, 15, 5, 10, 20, 25]
        self.assertEqual(matrix_chain_multi(p), 15125)


    def test_lcs(self):
        '''
        test for longest_common_subsequence
        '''
        s1 = 'abcbdab'
        s2 = 'bdcaba'
        s, len_lcs = longest_common_subsequence(s1, s2)
        self.assertEqual(len_lcs[7][6], 4)
        self.assertEqual(len_lcs[6][5], 3)
        self.assertEqual(len_lcs[2][5], 2)
        self.assertEqual(len_lcs[5][2], 2)

        self.assertEqual(s[7][6], 'up')
        self.assertEqual(s[6][5], 'up')
        self.assertEqual(s[6][6], 'ul')


if __name__ == '__main__':
    unittest.main()