'''
Created on Apr 18, 2019

@author: tom
'''



'''
This method takes in the beginning principal of a loan, the annual percentage rate (aka APR), and the number
of payment periods.  The annual_percentage_rate should be entered in standard format and the method will convert 
to decimal.  So if the annual percentage is 7.5 then enter it that way and the function will /100.
The formula is broken into steps here but could be written as principal * ((r(1+r)^number_of_payments)/((1+r)^number_of_payments -1)).
'''
def calculate_payment(beginning_principal,annual_percentage_rate,payment_periods):
    payment = 0.00
    

    '''  This is the rate per payment period.  
         Since the rate is annual (aka APR) we divide by 12.'''
    r = (annual_percentage_rate/100)/12

    numerator = r*(1+r)**payment_periods
    denominator = ((1+r)**payment_periods)-1
    
    payment = beginning_principal*(numerator/denominator) 
    
    return payment



def calculate_interest_portion_of_payment(previous_balance,annual_percentage_rate):
    return previous_balance * ((annual_percentage_rate/100)/12)
    

def calculate_principal_portion_of_payment(interest_payment,total_payment):
    return total_payment - interest_payment    

def generate_amortization_schedule(beginning_principal,annual_percentage_rate,payment_periods):
    total_payment = calculate_payment(beginning_principal, annual_percentage_rate, payment_periods)
    principal_balance = beginning_principal
    amortization_schedule = []
    for payment_number in range(payment_periods):
        interest_payment = calculate_interest_portion_of_payment(principal_balance, annual_percentage_rate)
        principal_payment = calculate_principal_portion_of_payment(interest_payment,total_payment)
        principal_balance = principal_balance - principal_payment
        amortization_schedule.append([total_payment,interest_payment,principal_payment,principal_balance])
        
    return amortization_schedule
                                      
                                      
schedule = generate_amortization_schedule(20000, 7.5, 60)
 
print("Total Payment\tInterest Payment\tPrincipal Payment\tPrincipal Balance") 
for payment in schedule:
    print(round(payment[0],2), "\t\t",round(payment[1],2),"\t\t\t",round(payment[2],2),"\t",round(payment[3],2))
    
    
    
    
    