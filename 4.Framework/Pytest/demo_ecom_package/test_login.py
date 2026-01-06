import pytest


@pytest.mark.parametrize("username,password",[("admin","admin123")])
def test_login_with_valid_credentials(username,password):
    print("verify login with valid credentials")
    print(f"{username}:{password}")


def test_login_with_invalid_credentials():
    print("verify login with invalid credentials")
    assert 1 == 0

data_provider = [("admin","admin123"),("hr","hr123"),("engg","engg123")]
@pytest.mark.parametrize("username,password",data_provider)
@pytest.mark.ddt
def test_login_ddt(username,password):
    print("verify login with multiple set of credentials")
    print(f"{username}:{password}")