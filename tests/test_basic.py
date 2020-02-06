# coding: aheui

from aheuithon import aheui
import unittest

@aheui
def aheui_three():
    받망희

@aheui
def aheui_three_newline():
    붇
    망희

@aheui
def aheui_ord(ch):
    밯망희

def a():
    return aheui_test("a")
    @aheui
    def aheui_test(ch):
        밯망희

class BasicTestSuite(unittest.TestCase):
    def test_three(self):
        self.assertEqual(3, aheui_three())
        self.assertEqual(3, aheui_three_newline())

    def test_ord(self):
        self.assertEqual(ord('a'), aheui_ord('a'))