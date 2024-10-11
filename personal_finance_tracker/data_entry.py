from datetime import datetime

date_format = '%d-%m-%Y'
categories = {'I': 'income', 'E': 'expense'}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    
    except ValueError:
        print('invalid date format.')
        return get_date(prompt, allow_default)
    
def get_amount():
    try:
        amount = float(input('enter amount: '))
        if amount <= 0:
            raise ValueError('must be a positive number')
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
        

def get_category():
    category = input('enter the category for (I for income or E for expense): ').upper()
    if category in categories:
        return categories[category]
    print('invalid category please enter I or E')

def get_description():
    return input('enter description')