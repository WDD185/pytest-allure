import pytest


class TestLogin:

    # 在每个类执行前的初始化工作
    def setup_class(self):
        print('创建日志，数据库连接，接口请求对象')

    # setup和teardown在每个用例前都会执行
    def setup(self):
        print('\n开始测试')

    # @pytest.mark.skipif(condition=1 + 1 == 2, reason='年纪太大')  # condition的条件为true时则跳过
    @pytest.mark.run(order=2)  # mark方法来指定用例的执行顺序
    def test_03(self, pc_fixture):
        print('王哥大侠222')

    @pytest.mark.run(order=3)
    @pytest.mark.smoke  # 将用例标记为smoke，在python.ini中注册自定义标记即可单独执行该标记用例
    def test_equal(self, pc_fixture):
        assert 1 + 1 == 2

    # @pytest.mark.skip(reason='跳过该用例')  # 将用例标记为跳过
    @pytest.mark.run(order=1)
    def test_04(self, pc_fixture):
        print('hello')

    @pytest.mark.run(order=4)
    def test_05(self):
        print('你是好人')

    def teardown(self):
        print('\n结束测试')
