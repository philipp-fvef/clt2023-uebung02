# -*-coding:utf-8 -*-
# Author: Eileen Kammel
# Date: 2022-11-04 11:58:57

from perrin import perrin_i, perrin_r
import pytest


class TestPerrin():

    def test_basecase_recursive_0(self):
        assert perrin_r(0) == 3

    def test_basecase_iterative_0(self):
        assert perrin_i(0) == 3

    def test_basecase_recursive_1(self):
        assert perrin_r(1) == 0

    def test_basecase_iterative_1(self):
        assert perrin_i(1) == 0

    def test_basecase_recursive_2(self):
        assert perrin_r(2) == 2

    def test_basecase_iterative_2(self):
        assert perrin_i(2) == 2

    def test_non_base_recursive_5(self):
        assert perrin_r(5) == 5

    def test_non_base_iterative_5(self):
        assert perrin_i(5) == 5

    def test_non_base_recursive_15(self):
        assert perrin_r(15) == 68

    def test_non_base_iterative_15(self):
        assert perrin_i(15) == 68
