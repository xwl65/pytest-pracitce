#!/usr/bin/env python
# -*- coding;utf-8 -*-
import pytest
import  yaml
import pytest
import os
#测试文件
from pthoncode.calc import calculator
import os
import allure
import yaml
def test_case (cmdoption):
    env,datas=cmdoption
    ip=datas['env']['ip']
    port = datas ['env']['port']
    url='http://'+ip + ":"+str (port)
    print(url)


with open('data.yaml') as f:
    datas=yaml.safe_load(f)

    mydatas=datas.values()
    adddatas=mydatas.add
    divdatas=mydatas.div
    subdatas=mydatas.sub
    multdatas=mydatas.mult
    myids=datas.add.keys()


#如下两步结合起来当有效果，相当于把数据里面的add读写出来。效果相当的好
def get_steps():
    with open("sub.yaml") as f:
        steps = yaml.safe_load(f)
        return steps

cal=calculator()
def steps(a,b,result):
    steps = get_steps()
        if steps.add:
            steps1=steps.add
            for steps1 in steps.add
                if 'add' == steps1:
                    assert result == cal.add(a, b)
                elif 'add1' == steps1:
                    assert result == cal.add1(a, b)
                elif 'add2' == steps1:
                    assert result == cal.add2(a, b)


        if steps.div:
            steps1 = steps.div
            for steps1 in steps.div
                if 'div' == steps1:
                    assert result == cal.div(a, b)
                elif 'div1' == steps1:
                    assert result == cal.div1(a, b)
                elif 'div2' == steps1:
                    assert result == cal.div2(a, b)


        if steps.sub:
            steps1 = steps.sub
            for steps1 in steps.sub
                if 'sub' == steps1:
                    assert result == cal.div(a, b)
                elif 'sub1' == steps1:
                    assert result == cal.div1(a, b)
                elif 'sub2' == steps1:
                    assert result == cal.div2(a, b)


        if steps.mult:
            steps1 = steps.mult
            for steps1 in steps.mult
                if 'mult' == steps1:
                    assert result == cal.div(a, b)
                elif 'mult1' == steps1:
                    assert result == cal.div1(a, b)
                elif 'mult2' == steps1:
                    assert result == cal.div2(a, b)

class TestCalc:

    @pytest.mark.dependency()
    #@pytest.mark.flaky(rerurns=5)
    def test_add(self,"param.add"):
        steps("param.add")

    @pytest.mark.flaky(rerurns=10)
    @pytest.mark.dependency(depends=["test_add"])
    def test_subtract(self, "param.sub"):
        steps("param.sub")


    @pytest.mark.parametrize('a,b,result', "param.sub", ids="myids")
    # 如果test_subtract1执行成功，那么subtract2就会被执行，如果失败，那么不会被执行。
    @pytest.mark.dependency()
    def test_mult(self,  "param.mult"):
        steps("param.mult")

    @pytest.mark.dependency(depends=["test_subtract1"])
    def test_div(self, "param.div"):
        steps("param.div")









