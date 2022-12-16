class ReturnOnInvestment():

    def __init__(self, four_sq_method):
        self.four_sq_method = four_sq_method


    def total_income(self):
        income = []
        while True:
            print('\nYou may enter Done at any time if you are finished.')
            value = input('\nPlease enter your income from your Rental property: ')
            if value.lower() == 'done':
                self.four_sq_method['income'] = sum(income)
                break
            else:
                try:
                    value = int(float(value))
                    income.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your income from your Laundry services: ')
            if value.lower() == 'done':
                self.four_sq_method['income'] = sum(income)
                break
            else:
                try:
                    value = int(float(value))
                    income.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your income from your Storage services: ')
            if value.lower() == 'done':
                self.four_sq_method['income'] = sum(income)
                break
            else:
                try:
                    value = int(float(value))
                    income.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter any Miscellaneous income: ')
            if value.lower() == 'done':
                self.four_sq_method['income'] = sum(income)
                break
            else:
                try:
                    value = int(float(value))
                    income.append(value)
                    self.four_sq_method['income'] = sum(income)
                    break
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
    
    def total_expenses(self):
        expenses = []
        while True:
            value = input('\nPlease enter your Tax expenses: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Insurance expenses: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Utility expenses: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your HOA expenses: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Lawncare/Snow Removal expenses: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Vacancy expenses: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Repair expenses: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Capital Expenditure: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Property Management expenses: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Mortgage Payment: ')
            if value.lower() == 'done':
                self.four_sq_method['expenses'] = sum(expenses)
                break
            else:
                try:
                    value = int(float(value))
                    expenses.append(value)
                    self.four_sq_method['expenses'] = sum(expenses)
                    break
                except:
                    print('Invalid input. You must enter a whole number or decimal.')

    def total_cash_flow(self):
        cash_flow = (self.four_sq_method['income'] - self.four_sq_method['expenses']) * 12
        print(f'\nYour Annual Cash Flow from this property is ${cash_flow}.')
        self.four_sq_method['cash flow'] = cash_flow

    def total_investment(self):
        investment = []
        while True:
            value = input('\nPlease enter your Down Payment on this property: ')
            if value.lower() == 'done':
                self.four_sq_method['investment'] = sum(investment)
                break
            else:
                try:
                    value = int(float(value))
                    investment.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter the Closing Costs for this property: ')
            if value.lower() == 'done':
                self.four_sq_method['investment'] = sum(investment)
                break
            else:
                try:
                    value = int(float(value))
                    investment.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter your Rennovation Budget for this property: ')
            if value.lower() == 'done':
                self.four_sq_method['investment'] = sum(investment)
                break
            else:
                try:
                    value = int(float(value))
                    investment.append(value)
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
            
            value = input('\nPlease enter any other miscellaneous investments for this property: ')
            if value.lower() == 'done':
                self.four_sq_method['investment'] = sum(investment)
                break
            else:
                try:
                    value = int(float(value))
                    investment.append(value)
                    self.four_sq_method['investment'] = sum(investment)
                    break
                except:
                    print('Invalid input. You must enter a whole number or decimal.')
    
    def total_roi(self):
        try:
            total = self.four_sq_method['cash flow'] / self.four_sq_method['investment']
            print('\nYour total return on investment is ' + '{:.2%}'.format(total))
        except:
            print('No information was given, or only 0 was entered.') 

roi = ReturnOnInvestment({})

def run():
    while True:
        response = input('Would you like to calculate your Return on Investment? Yes or No. ')

        if response.lower() == 'no':
            print('Thank you.')
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