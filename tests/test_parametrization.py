import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_number(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1,1),(2,4),(3,9)])
def test_several_number(number:int, expected:int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os:str, browser:str):
    assert len(os + browser) > 0

# Фикстуры, параметрищация
@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request:SubRequest):
    return request.param

def test_open_browser(browser:str):
    print(f'Running test on browser: {browser}')

# Параметризация класса
@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:

    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account:str):
        ...

    def test_user_without_operations(self, user: str):
        ...

#идентификаторы
@pytest.mark.parametrize(
    'phone_number',
    ['88005553535', '42347879849', '423478453435'],
    ids=[
        'User with money on bank account',
        'User without money on bank account',
        'User with operation on bank account'
    ])

def test_indentifiers(phone_number: str):
    ...