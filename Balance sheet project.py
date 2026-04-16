
while True:    
    current_assets = float(input('Enter the total current assets amount: '))

    longterm_assets = float(input('Enter the total longterm assets amount: '))

    current_liabilities = float(input('Enter the total current liabilities: '))

    longterm_liabilities = float(input('Enter the total longterm liabilities: '))

    shareholders_equity = float(input('Enter the total share shareholders_equity: '))
    


    choise = input('Choose total assets total liabilities overall assets): ')

    if choise == 'total assets':
        
        result = current_assets + longterm_assets
        print("Your total assets is",result)

    elif choise == 'total liabilities':
        result = current_liabilitis + longterm_liabilities
        print("Your total liabilities is",result)
        
    elif choise == "overall assets":
        result = current_liabilities + longterm_liabilities + shareholders_equity
        print("Your overall assets is",result)
        
            
        
