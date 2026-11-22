"""
Simple file with tests for the module arrays.py
"""
import arrays
import array as arr
import pytest

def test_insert():
    assert arr.array('i', [1,2,3]) == arrays.insert_element(arr.array('i', [1,2]),2,3)

def test_insert_wrong_type():
    a = arr.array('i', [1,2])
    with pytest.raises(Exception):
        arrays.insert_elements(a,-1,'s')
