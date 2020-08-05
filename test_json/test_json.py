from json2 import StudentDB
import pytest
import json

def test_scott_data():
    db = StudentDB()
    db.connect('data.json')
    scott_data = db.get_data('scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'scott'
    assert scott_data['result'] == 'pass'

def test_lucas_data():
    db = StudentDB()
    db.connect('data.json')
    lucas_data = db.get_data('lucas')
    assert lucas_data['id'] == 2
    assert lucas_data['name'] == 'lucas'
    assert lucas_data['result'] == 'fail'
