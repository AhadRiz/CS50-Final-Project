import pytest
from project import generate_response, preprocess_input, load_data

def test_generate_response():
    data = load_data()
    assert generate_response("Tell me about admissions", data) == data["admission_info"]
    assert generate_response("What are the courses offered?", data) == data["courses_info"]
    assert generate_response("How can I contact the university?", data) == data["contact_info"]
    assert generate_response("What is the fee structure?", data) == data["fee_info"]

def test_preprocess_input():
    assert preprocess_input("Tell me about admissions") == ["tell", "admissions"]
    assert preprocess_input("What courses do you offer?") == ["courses", "offer", "?"]

def test_load_data():
    data = load_data()
    assert "admission_info" in data
    assert "courses_info" in data
    assert "contact_info" in data
    assert "fee_info" in data
