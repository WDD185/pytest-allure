import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./report/temp -o ./report/html --clean')

    # -vs,详细信息的展示
    # -n,增加并发数
    # --reruns,失败的用例重新跑
    # -x,只要有一个用例失败则终止运行
    # --maxfail,出现用例失败则停止
    # -k,根据测试用例的部分字符串去执行用例
    # -m,执行标记的用例
    # --html=./report/report.html，生成测试报告的html
