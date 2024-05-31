from ps4.src.ps4 import *
import pytest

def test_NestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    assert pytest.approx(savingsRecord) == [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

def test_NestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    assert pytest.approx(savingsRecord) == [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    assert pytest.approx(savingsRecord) == [80000.000000000015, 54000.000000000015, 24000.000000000015, -4799.9999999999854, -34847.999999999985]

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    assert pytest.approx(expenses, abs = epsilon) == 1229.95548986