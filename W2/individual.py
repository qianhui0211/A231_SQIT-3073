def monthly_instalment(loan,interest_rate, year): # calculate the monlthly instalment
    n=year*12
    r=(interest_rate/100)/12
    Monpayment= (r*loan*((1+r)**n))/(((1+r)**n)-1)
    return Monpayment

def total_amount_payable(monthly_payment, year): # calculate the total amount paybale
    n = year*12
    total_amount_payable= monthly_payment*n
    return total_amount_payable

def calculate_dsr (loan, interest_rate, year, monthly_income, other_commitments): # calculate the DSR
    monthly_payment= monthly_instalment(loan, interest_rate, year)
    total_commitments=  other_commitments+monthly_payment
    dsr=(total_commitments/ monthly_income)*100
    return dsr

def check_eligibility(dsr, dsr_ratio=70): # Function to check eligible
    if dsr<= dsr_ratio:
        return "It this DSR eligible: Eligible."
    else:
        return "It this DSR eligible: Not Eligible."

def previous_calculation(loan_calculation): # show all previous calculation

    if not loan_calculation:
        print("No previous Loan Calculation")
    else:
        print("Previous Loan Calculation:")
        

        for idx, calculation in enumerate(loan_calculation, start=1):
            print(f"\nCalculation {idx}:")
            print(f"Monthly Payment: RM{calculation['Monthly Payment']:.2f}")
            print(f"Total Amount Payable: RM{calculation['Total Amount Payable']:.2f}")
            print(f"DSR: {calculation['DSR']:.2f}%")
            print(f"{calculation['Eligibility']}")
       
       
def Main(): # Sat a Main Menu

    loan_calculation=[]
    selection = ''

    while selection != '4':
        print("------Main Menu------")
        print("1. Calculate Your New Loan")
        print("2. View Your Loan")
        print("3. Delete")
        print("4. Exit")
        
        selection=input("Please Enter Your Choice (1,2,3 or 4):")
        if selection=="1":
            loan=int(input("Please input amount of loan :RM "))
            interest_rate=float(input("Please enter Annual interest rate :"))
            year= int(input("Please input year of loan :"))
            other_commitments= int(input("Please input of other commitments :RM "))
            monthly_income= int(input("Please input amount of monthly income :RM "))

            monthly_payment= monthly_instalment(loan, interest_rate, year)
            total_payable=total_amount_payable(monthly_payment, year)
            dsr= calculate_dsr(loan, interest_rate, year, monthly_income, other_commitments)
            eligibility= check_eligibility(dsr, dsr_ratio=70)

            print("Monthly payment : RM{0:2f}". format(monthly_instalment(loan,interest_rate, year)))
            print("total amount payable :RM{0:2f}". format (total_payable))
            print("Total DSR:{0:2f}%". format (calculate_dsr(loan, interest_rate, year, monthly_income, other_commitments)))
            print(eligibility)
             
            loan_calculation.append ({"Principal":loan,
                              "Annual Interest Rate":interest_rate,
                              "Long Term":year,
                              "Monthly Income":monthly_income,
                              "Monthly Commitments":other_commitments,
                              "Monthly Payment":monthly_payment,
                              "Total Amount Payable": total_payable,
                              "DSR":dsr,
                              "Eligibility":eligibility})
        
        elif selection == "2": 
            previous_calculation(loan_calculation)
            
        
        elif selection == "3": # detele the selected calculation
            detele=int (input("If there are any typing erros, please detele your previous calculation")) -1
            if 0<=detele < len(loan_calculation):
                detele= loan_calculation.pop (detele)
                print ("Delete Succesful")
            else:
                print("Please Try Again")
        
        else:
            print("Please enter 1,2  or 3.")
    print("Exiting the Loan Calculator") # exit the program


if __name__== "__main__":
    Main()
