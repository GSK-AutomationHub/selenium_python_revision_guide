import pytest


@pytest.mark.smoke
def test_register_with_mandatory_fields():
    print("verify registration with mandatory fields")

@pytest.mark.sanity
def test_register_with_all_fields():
    print("verify registration with all fields")