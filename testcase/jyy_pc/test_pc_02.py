import pytest


class TestApi:

    @pytest.mark.parametrize('name', param=['王1', '王2'])
    def test_go(self, name):
        print(name)
