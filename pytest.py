"""
Unit tests for stack.py
"""

from hw_4.py import hw_4
import pytest

from evo import Evo
import pandas as pd
import numpy as np
import random as rnd
import csv

# read the given files and turn them into dataframes
sections_df = pd.read_csv("sections.csv")
tas_df = pd.read_csv("tas.csv")



@pytest.fixture
def read_files():
    test1 = pd.read_csv("test1.csv", header=None)
    test2 = pd.read_csv("test2.csv", header=None)
    test3 = pd.read_csv("test3.csv", header=None)

    return test1, test2, test3


def test_overallocations(read_files):

    test1, test2, test3 = read_files

    assert overallo(test1) == 37, 'Overallocation for test1 did not equal 37'
    assert overallo(test2) == 41, 'Overallocation for test1 did not equal 41'
    assert overallo(test3) == 23, 'Overallocation for test1 did not equal 41'


def test_time_conflict():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    return s


def under_supp():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    return s


def unwilling_obj():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    return s


def test_constructor():
    s = Stack()
    assert isinstance(s, Stack), "Did not construct a stack"
    assert s.size() == 0, "Stack is not empty"
    assert len(s) == 0, "Stack is not empty"

def test_push(stack):

    stack.push(3)
    stack.push(4)
    assert len(stack) == 2
    assert stack.top() == 4


def test_pop(stack):
    stack.push('a')
    stack.push('b')

    assert stack.pop() == 'b', 'wrong value popped'
    assert stack.pop() == 'a', 'wrong value popped'
    assert stack.pop() is None, 'wrong value popped'
    assert stack.top() is None, 'Stack should be empty but its not'


def test_top(stack3):
    assert stack3.top() == 3, 'wrong value on top'
    stack3.pop()
    stack3.pop()
    assert stack3.top() == 1, 'wrong value on top'
    stack3.pop()
    assert stack3.top() is None, 'Stack should be empty'


