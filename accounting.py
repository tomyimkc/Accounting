import numpy as np
import pandas as pd
from CSV_Creator import add_data
import os.path
from path_dir import path,sep

income_statement_dic={

}

# chapters in a book {}
balance_sheet_dic={
    0:'Asset',
    1:'Capital',
    2:'Liabilities',
    3:'Revenue',
    4:'Expense'
}

asset_dic={
    0:'NCA',
    1:'CA'
}

NCA_dic={
    0:'Office Equipment',
    1:'Office Furniture',
    2:'Machinery'
    #...
}

CA_dic={

}

CA_dic={
    0:'Inventory',
    1:'Account Receivable',
    2:'Deposit Paid',
    3:'Bank',
    4:'Cash'
}

# Current liabilities
CL_dic={
    0:'Accounts Payable',
    1:'Bank Overdraft'
}

NCL_dic={
    0:'Bank Loan'
}

Expense_dic={
    0:'Purchase',
    1:'Return Outwards',
    #... electricity... rent and rates
}

Revenue_dic={
    0:'Sales',
    1:'Return Inwards',
}

#Do something: function mark down investment of captial
def investment(name,value):
    print ('Here is the investment!')
    #to csv
    # to 


def income_statement():
    print('Here is the income statement')
    print(asset_dic[0])

#can be further develop as 

# item to be update

#Dr $ Cr Capital string
def update_capital(money_value,capital):
    Capital_df=pd.read_csv(f'E:\Tom_Utopia\Accounting\Capital\{capital}.csv')
    Asset_df=pd.read_csv(f'E:\Tom_Utopia\Accounting\Asset\{capital}.csv')


    DR_array=[float(money_value),0]
    CR_array=[0,float(money_value)]

    add_data(Capital_df,CR_array,'Capital:'+capital)
    add_data(Asset_df,DR_array,'Capital:'+capital)
    
    # name = Software, folder, T: a=C+L+Reveune-Expense

# further update csv_df


def capital_cash(cash,capital):
    update_capital(cash,capital)
    

def capital_hardware(hardware,capital):
    update_capital(hardware,capital)

# #Dr $ Cr Capital string
def capital_software(software,capital):
    update_capital(software,capital)


def money_choice(capital_name):
    money_choice=input('Assuming there is only one capital source!\n0. NFT\n1. Cash HKD\n2. Hardware\n3. Software\nYour Input:')
    if money_choice=="0":
        print ('Pending to write NFT program...')
    elif money_choice=="1":
        cash_amount=input('What is the cash amount:')
        capital_cash(cash_amount,capital_name)
    elif money_choice=="2":
        # def capital_hardware(hardware,capital):
        hardware_amount=input('What is the hardware amount:')
        print('This is NAS amount:',hardware_amount)
        stop=input('Please check hardware amount')
        capital_hardware(hardware_amount,'capital_name')
    elif money_choice == "3":
        # def capital_software(software,capital):
        software_amount = input('What is the software amount:')
        # print('This is software amount:', software_amount)
        stop = input('Please check software amount')
        capital_software(software_amount, capital_name)
if __name__=='__main__':
    while True:

        # login system
        if os.path.exists(f'{path}Capital{sep}Capital.csv'):
            print('Capital.csv exists')
            df=pd.read_csv(f'{path}Capital{sep}Capital.csv')
            # print(df['name'].tolist())
            capital_list=df['name'].tolist()
            
        else:
            print('Capital.csv does not exist')
        
        # stop=input('Please check above')



        try:
            choice=input('0. Capital Investment\n1. Capital Management pending...\nYour Input')
            if choice=='0':
                
                #show capital name
                print ('This is the capital list:',capital_list)
                capital_choice=input('Please input capital name:')
                if capital_choice in capital_list:
                    print(capital_choice,'is selected')
                    money_choice(capital_choice)

                else:
                    print('A new capital is entered, confirmed?')

                stop=input('Continue?')

                


            elif choice=='1':
                cap_choice=input('0. Hardware\n1. Software\nYour input:')
                if cap_choice=='0':
                    capital_hardware()

                elif cap_choice=='1':
                    capital_software()



            elif choice=='2':
                #Pending update
                #CA or NCA
                investment_choice=input('0. Cash\n1. Equipment')
                if investment_choice=='0':
                    name='Cash'
                elif investment_choice=='1':
                    name=input('')
                value=float(input('Values'))
                investment(name,value)


                # it will update two books, debit/credit
                # debit Asset, credit Capital
                # the Capital as a way of divident distribution
            

        except KeyboardInterrupt:
            break