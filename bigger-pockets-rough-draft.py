# four square method

#------------------------------------------------------------
#| income                   | cash flow                      |
#|                          |                                |
#| rental income = $2k      | income - expenses              |
#| laundry = 0              | 2000 - 1610                    |
#| storage = 0              | total = 390                    |
#| misc = 0                 |                                |
#| total = 2k               |                                |
#|--------------------------|--------------------------------|
#| expenses                 | cash on cash - ROI             |
#|                          |                                |
#| tax = 150                | down payment = 40k             |
#| insurance = 100          | closing cost = 3k              |
#| utilities = 0            | rehab budget = 7k              |
#|    electric              | misc = 0                       |
#|    water                 |                                |
#|    sewer                 | total investment = 50k         |
#|    garbage               |                                |
#|    gas                   |                                |
#| HOA = 0                  |                                |
#| lawn = 0                 |                                |
#| vacancy = 100            |                                |
#| repairs = 100            |                                |
#| CapEx = 100              |                                |
#| property management = 200|                                |
#| mortgage = 860           |                                |
#| total = 1610             |                                |
#------------------------------------------------------------

# monthly cash flow * 12 = annual cash flow ------------- 390 * 12 = 4680
# annual cash flow / total investment = ROI ------------------- 4680 / 50000 = 9.36(%)



class ReturnOnInvestment():

    def __init__(self, four_sq_method):
        self.four_sq_method = four_sq_method

    def total_income(self):
        income = []
        while True:
            start = input('\nWould you like to enter your income? Enter Yes, or No if you are finished. ')
            if start.lower() == 'no':
                self.four_sq_method['income'] = sum(income)
                break
            elif start.lower() == 'yes':
                value = int(float(input('Please enter any income that you have: ')))
                income.append(value)
            else:
                print('Pleae enter a valid option.')

    def total_expenses(self):
        expenses = []
        while True:
            start = input('\nWould you like to enter your expenses? Enter Yes, or No if you are finished. ')
            if start.lower() == 'no':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            elif start.lower() == 'yes':
                value = int(float(input('Please enter any expenses that you have: ')))
                expenses.append(value)
            else:
                print('Pleae enter a valid option.')

    def total_cash_flow(self):
        cash_flow = (self.four_sq_method['income'] - self.four_sq_method['expenses']) * 12
        self.four_sq_method['cash flow'] = cash_flow

    def total_investment(self):
        investment = []
        while True:
            start = input('\nWould you like to enter any additional costs, such as a Down Payment, Closing Cost, or Rennovation Budget? Enter Yes, or No if you are finished. ')
            if start.lower() == 'no':
                self.four_sq_method['investment'] = sum(investment)
                break
            elif start.lower() == 'yes':
                value = int(float(input('Please enter any additional costs: ')))
                investment.append(value)
            else:
                print('Please enter a valid option.')
    
    def total_roi(self):
        total = self.four_sq_method['cash flow'] / self.four_sq_method['investment']
        print('Your total return on investment is ' + '{:.2%}'.format(total))

roi = ReturnOnInvestment({})

def run():
    while True:
        response = input('Would you like to calculate your Return on Investment? Yes or No. ')

        if response.lower() == 'no':
            break
        elif response.lower() == 'yes':
            roi.total_income()
            roi.total_expenses()
            roi.total_cash_flow()
            roi.total_investment()
            roi.total_roi()
            break
        else:
            print('Please enter a valid option.')

run()
