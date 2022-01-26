def calculatePay():
    # Implement your solution in between the two comment blocks
    hrs = 0.0
    rate = 0.0
    pay = 0.0 #predefining variable default

    try:
        hrs = float(input("Enter Hours:"))
        rate = float(input("Enter Hourly Rate:"))
        print("calculating pay")

        if(hrs > 40):
            OTpay = (rate*0.5)*(hrs-40)
        else:
            OTpay = 0.0

        pay = rate*hrs + OTpay

        print(str(pay))
    except: print("Error, please enter numeric input")
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()