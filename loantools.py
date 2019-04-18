'''
Created on Apr 18, 2019

@author: tom
'''



'''
This method takes in the beginning principal of a loan, the annual percentage rate (aka APR), and the number
of payment periods.  The annual_percentage_rate should be entered in standard format and the method will convert 
to decimal.  So if the annual percentage is 7.5 then enter it that way and the function will /100.
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



