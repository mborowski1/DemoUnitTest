import pytest

@pytest_fixture()
def setup():
    print(" Trial Trial ")

def testmethod1(setup):
    print(" Trial Trial ")

def testmethod1(setup):
    print(" Trial Trial ")