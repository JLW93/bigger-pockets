class ReturnOnInvestment():

    def __init__(self, four_sq_method):
        self.four_sq_method = four_sq_method


    def total_income(self):
        income = []
        while True:
            value = input('\nPlease enter any income that you have, or enter Done if you are finished: ')
            if value.lower() == 'done':
                self.four_sq_method['income'] = sum(income)
                break
            else:
                try:
                    value = int(float(value))
                    income.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
    
    def total_expenses(self):
        expenses = []
        while True:
            value = input('\nPlease enter any expenses that you have, or enter Done if you are finished: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')

    def total_cash_flow(self):
        cash_flow = (self.four_sq_method['income'] - self.four_sq_method['expenses']) * 12
        self.four_sq_method['cash flow'] = cash_flow

    def total_investment(self):
        investment = []
        while True:
            value = input('\nPlease enter any additional costs that you have (Down Payment, Closting Costs, etc.), or enter Done if you are finished: ')
            if value.lower() == 'done':
                self.four_sq_method['investment'] = sum(investment)
                break
            else:
                try:
                    value = int(float(value))
                    investment.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
    
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