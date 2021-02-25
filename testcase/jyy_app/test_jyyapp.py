import pytest


class TestLogin:

    @pytest.mark.run(order=2)
    def test_01(self, all_fixture, app_fixture):
        print('王哥大侠')
        print('------' + str(all_fixture)+str(app_fixture))

    @pytest.mark.run(order=1)
    def test_02(self, all_fixture, app_fixture):
        print('王哥大侠1')
        print('------'+str(all_fixture)+str(app_fixture))
