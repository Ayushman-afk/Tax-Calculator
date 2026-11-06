import math
while True:
    userSal = int(input("Enter Which method you would like to use to calculate your earnings: \n 1. Hourly \n 2. Monthly \n 3. Quit \n Choice- "))

    if userSal == 1:
        hourly_rate = int(input("Enter Hourly Rate: "))
        hours_worked = int(input("Enter Hours Worked: "))
        if hours_worked <= 168:
            salary = (hourly_rate * hours_worked)
            print("Your Salary is: $", salary)
        # tax
            if salary <= 18250:
                print("Your Tax percent is 10%")
                saltax = (0.10 * salary)
                finalsal = salary - saltax
                print("Your Final Salary after tax is: $", finalsal)

            elif 18251 <= salary <= 69650:
                print("Your Tax percent is 12%")
                deduction = 1825
                taxable = salary - deduction
                if taxable >= 18250:
                    finalsal = 0.12 * taxable
                    print("Your Final Salary after tax is: $", finalsal)
                else:
                    print("Your Final Salary is $", taxable)

            elif 69651 <= salary <= 109100:
                print("Your Tax percent is 22%")
                deduction =  7993
                taxable = salary - deduction
                if taxable >= 109100:
                    finalsal = 0.22 * taxable
                    print("Your Final Salary after tax is: $", finalsal)
                else:
                    print("Your Final Salary is $", taxable)

            elif 109101 <= salary <= 208300:
                print("Your Tax percent is 24%")
                deduction = 16672
                taxable = salary - deduction
                if taxable >= 69650:
                    finalsal = 0.24 * taxable
                    print("Your Final Salary after tax is: $", finalsal)
                else:
                    print("Your Final Salary is $", taxable)

            elif 208301 <= salary <= 264550:
                print("Your Tax percent is 32%")
                deduction = 40480
                taxable = salary - deduction
                print("Your Taxable income is: $", taxable)
                finalsal = 0.32 * taxable
                print("Your Final Salary after tax is: $", finalsal)
            elif 264551 <= salary <= 661350:
                print("Your Tax percent is 35%")
                deduction = 58480
                taxable = salary - deduction
                print("Your Taxable income is: $", taxable)
                finalsal = 0.35 * taxable
                print("Your Final Salary after tax is: $", finalsal)
            elif salary >= 661351:
                print("Your Tax percent is 37%")
                deduction = 58480
                taxable = salary - deduction




    elif userSal == 2:
        monthly_sal = int(input("Enter Monthly Salary: "))
        print("Your Monthly Salary is: $", monthly_sal)



