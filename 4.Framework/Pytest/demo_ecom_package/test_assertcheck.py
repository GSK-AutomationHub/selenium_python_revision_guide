
def setup_module(module):
    print("this is module setup hook test")

def teardown_module(module):
    print("this is module teardown hook test")

def setup_function(function):
    print("this is function setup hook test")

def teardown_function(function):
    print("this is function teardown hook test")

def test_sample_validation_1():
    assert 1 ==1
    assert 5 < 3

def test_sample_validation_2():
    assert 2**2 == 4


def test_sample_validation_3():
    assert 10%2 == 0


