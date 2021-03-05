import pytest


class TestApi:

    @pytest.mark.parametrize('name, age', [['王1', '18'], ['王2', '20']])
    def test_go(self, name, age):
        print(name, age)


