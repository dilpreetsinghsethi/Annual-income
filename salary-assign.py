from datetime import date

def main():
    #entering data from user
    company=input("enter your company name=")
    today=date.today()
    name=input("enter your name=")
    position=input("enter your position in the company=")
    annual_sal=int(input("enter your annual salary = $"))
    print()

    #calculating bonus and gross_annual_income
    if(annual_sal<=25000):
        bonus=10.5/100*annual_sal
    elif(annual_sal>25000 and annual_sal<=50000):
        bonus=11.5/100*annual_sal
    elif(annual_sal>50000 and annual_sal<=55000):
        bonus=0
    else:
        bonus=12.5/100*annual_sal

    gross_sal=annual_sal + bonus

    #calculating net_annual_income
    taxes=15.5/100*gross_sal
    benefits=6.5/100*gross_sal
    deductibles= taxes + benefits
    net_income = gross_sal - deductibles

    #Printing Pay Stub
    print()
    print("----PAY STUB----")
    print("Company Name: ",company)
    print("Date Of Pay-Stub: ",today)
    print("Employee: ",name)
    print("Position: ",position)
    print("Salary: $",annual_sal)
    print("Bonus: $",bonus)
    print("Gross Annual Income: $",gross_sal)
    print("Deductibles: $",deductibles)
    print("Deductibles (Taxes): $",taxes)
    print("Deductibles (Benefits): $",benefits)
    print("Net Annual Income: $",net_income)
    print()
    print()


if __name__=="__main__":

    #number of employees for which pay stub is to be calculated
    lst=[]
    n=int(input("Enter the number of elements : "))
    for i in range(0,n):
        main()
    
    


    
