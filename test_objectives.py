"""
Unit tests for hw_4.py
"""
import pytest

from hw_4 import overallo, time_conflict, under_supp, unwilling, unpreferred
import evo
import test_objectives

from evo import Evo
import pandas as pd
import numpy as np
import random as rnd
import csv


@pytest.fixture
def read_files():
    test1 = pd.read_csv("test1.csv", header=None)
    test2 = pd.read_csv("test2.csv", header=None)
    test3 = pd.read_csv("test3.csv", header=None)

    return test1, test2, test3


def test_overallocations(read_files):

    test1, test2, test3 = read_files

    assert overallo(test1) == 37, 'Overallocation for test1 did not equal 37'
    assert overallo(test2) == 41, 'Overallocation for test2 did not equal 41'
    assert overallo(test3) == 23, 'Overallocation for test3 did not equal 23'


def test_time_conflict(read_files):

    test1, test2, test3 = read_files

    assert time_conflict(test1) == 8, 'Time conflict for test1 did not equal 8'
    assert time_conflict(test2) == 5, 'Time conflict for test2 did not equal 5'
    assert time_conflict(test3) == 2, 'Time conflict for test3 did not equal 2'

def test_under_support(read_files):

    test1, test2, test3 = read_files

    assert under_supp(test1) == 1, 'Under Support for test1 did not equal 1'
    assert under_supp(test2) == 0, 'Under Support for test2 did not equal 0'
    assert under_supp(test3) == 7, 'Under Support for test3 did not equal 7'

def test_unwilling(read_files):

    test1, test2, test3 = read_files

    assert unwilling(test1) == 53, 'Unwilling for test1 did not equal 53'
    assert unwilling(test2) == 58, 'Unwilling for test2 did not equal 58'
    assert unwilling(test3) == 43, 'Unwilling for test3 did not equal 43'

def test_unpreferred(read_files):

    test1, test2, test3 = read_files

    assert unpreferred(test1) == 15, 'Unpreferred for test1 did not equal 15'
    assert unpreferred(test2) == 19, 'Unpreferred for test2 did not equal 19'
    assert unpreferred(test3) == 10, 'Unpreferred for test3 did not equal 10'





