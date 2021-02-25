import pytest


@pytest.fixture(scope='function', params=['王2'], ids=['w2'])
# scope在哪个之前执行（ function、class、moudle），params是参数化支持list,tuple等, autouse是默认为false不执行, ids, name
def app_fixture(request):
    print('\n这是app前置的方法')
    yield request.param  # return和yield都是表示返回的意思，但是return后面不能跟代码，yield可以
    print('\n这是app后置的方法')
