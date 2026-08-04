import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("AUTOUSE")


@pytest.fixture(scope="session")
def settings():
    print("session")


@pytest.fixture(scope="class")
def user():
    print("CLASS")

@pytest.fixture(scope="function")
def browser():
    print("FUNCTION")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
     ...



class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
     ...
