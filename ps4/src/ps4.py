#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    if years == 0:
        return []
    retirement_fund = [salary * save * 0.01]
    for year in range(years - 1):
        retirement_fund.append(retirement_fund[year] * (1 + 0.01 * growthRate) + salary * save * 0.01)
    return retirement_fund


#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRates: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    if len(growthRates) == 0:
        return []
    retirement_fund = [salary * save * 0.01]
    for year in range(len(growthRates) - 1):
        retirement_fund.append(retirement_fund[year] * (1 + 0.01 * growthRates[year + 1]) + salary * save * 0.01)
    return retirement_fund

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    if len(growthRates) == 0:
        return []
    retirement_fund = [savings * (1 + 0.01 * growthRates[0]) - expenses]
    for year in range(len(growthRates) - 1):
        retirement_fund.append(retirement_fund[year] * (1 + 0.01 * growthRates[year + 1]) - expenses)
    return retirement_fund

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    retirement_fund_when_retire = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    lower_limit, upper_limit = 0, retirement_fund_when_retire + epsilon
    while True:
        test_value = (lower_limit + upper_limit) / 2
        retirement_fund_when_pass_on = postRetirement(retirement_fund_when_retire, postRetireGrowthRates, test_value)[-1]
        if retirement_fund_when_pass_on < -epsilon:
            upper_limit = (upper_limit + lower_limit) / 2
        elif retirement_fund_when_pass_on > epsilon:
            lower_limit = (upper_limit + lower_limit) / 2
            print(test_value, lower_limit, upper_limit)
        else:
            return test_value
        test_value = (upper_limit + lower_limit) / 2

findMaxExpenses(10000, 10, [3,4,5,0,3], [10,5,0,5,1], .01)
