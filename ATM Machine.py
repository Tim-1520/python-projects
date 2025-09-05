Bank_balance=1000
min_withdrawal=50
max_withdrawal=900
max_deposit=1000
#a list of the basic operations of an ATM
options=['Check Balance','Withdraw','Deposit']
#the enumerate method makes it easy to loop through the options list by creating a new iterable
for i,x in enumerate(options):
    print(i+1,x)
# the functions below handles what each options should do
def check_balance():
    return (f'${Bank_balance}')
def withdraw():
    amount=int(input('Enter an amount to withdraw:'))
    if amount > max_withdrawal:
        print('insufficient balance')
    elif amount < min_withdrawal:
        print('unable to process')
    elif amount < Bank_balance:
        Bank_balance1 = Bank_balance - amount
        return (f'you withdrew ${amount} you have ${Bank_balance1} left')
def deposit():
    amount1=int(input('Enter amount to deposit:'))
    if amount1 > max_deposit:
        print('deposit limit exceeded')
    elif amount1 <= Bank_balance:   
        Bank_balance2 = Bank_balance + amount1
        return (f'you deposited ${amount1} you have ${Bank_balance2} left')
#conditional statements to handle how to execute the above functions
for i in range(3):
    operation = input('Select an option: ')
    if operation == '1':
        print(check_balance())
    elif operation == '2':
        print(withdraw())
    elif operation == '3':
        print(deposit())
    else:
        print('invalid selection')

