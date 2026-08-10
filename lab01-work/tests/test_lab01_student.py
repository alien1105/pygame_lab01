"""Add at least four focused student-authored tests below."""
from src.lab01 import classify_score, format_student_record
import pytest
# Begin with one normal case, two threshold boundaries, and one exception.
def test_classify_score_rejects_string():
    with pytest.raises(TypeError):
        classify_score("pla")

def test_classify_score_rejects_float():
    with pytest.raises(TypeError):
        classify_score(1.5)

def test_classify_score_rejects_bool():
    with pytest.raises(TypeError):
        classify_score(True)

def test_classify_score_rejects_none():
    with pytest.raises(TypeError):
        classify_score(None)    

def test_classify_score_correct():
    assert classify_score(95) == "green"   
    assert classify_score(75) == "amber"   
    assert classify_score(45) == "red" 
    assert classify_score(0)  == "red"
    assert classify_score(59) == "red"
    assert classify_score(60) == "amber"
    assert classify_score(79) == "amber"
    assert classify_score(80) == "green"
    assert classify_score(100) == "green"

def test_format_student_record_rejects_blank_name():
    with pytest.raises(ValueError):
        format_student_record("   ", 70)

def test_format_student_record_correct():
    assert format_student_record("  Ada  ", 80) == "Ada | 80 | green"
    assert format_student_record("  Allen  ", 60) == "Allen | 60 | amber"

    