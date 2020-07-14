from typing import List
import yaml
import pytest
import os
import sys
sys.path.append('..')
@pytest.fixture(scope='function')
def cacl_begin_over():
    print("计算开始")
    yield
    print('计算结束')


#命令行添加参数 必须得使用addoption
def pytest_addoption(parser):
    mygroup = parser.getgroup("homework") #group 将下面所有的option都展示最这个group下
    mygroup.addoption("--env",
                        default ='test',
                        dest='env',
                        help='set your run env')
#cmdoption名字随便取 #按照request的方法，默认这样写就好了

@pytest.fixture(scope='session')
def cmdoption(request):

    myenv = request.config.getoption("--env",default='test')
    if myenv == 'test':
        datapath= 'test.yaml'
        print("这是测试环境")

    if myenv == 'dev':
        datapath= 'dev.yaml'
        print("这是开发环境")

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return myenv, datas

#通过方法动态的生成测试用例
def pytest_generate_tests(metafunc:"Metafunc") ->None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function')
