while True:
    userSal = int(input("Enter Which method you would like to use to calculate your earnings: \n 1. Hourly \n 2. Monthly \n 3. Quit \n Choice- "))

    if userSal == 1:
        hourly_rate = int(input("Enter Hourly Rate: "))
        print("The hours worked entered should be a total of the whole month of Hours Worked.")
        hours_worked = int(input("Enter Hours Worked: "))
        if hours_worked <= 672:
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
                tax = (18250 * 0.10) + ((salary - 18250) * 0.12)
                finalsal = salary - tax
                print("Your Final Salary after tax is: $", finalsal)

            elif 69651 <= salary <= 109100:
                print("Your Tax percent is 22%")
                tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((salary - 69650) * 0.22)
                finalsal = salary - tax
                print("Your Final Salary after tax is: $", finalsal)

            elif 109101 <= salary <= 208300:
                print("Your Tax percent is 24%")
                tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((salary - 69650) * 0.22) + ((salary - 109100) * 0.24)
                finalsal = salary - tax
                print("Your Final Salary after tax is: $", finalsal)

            elif 208301 <= salary <= 264550:
                print("Your Tax percent is 32%")
                tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((salary - 69650) * 0.22) + ((salary - 109100) * 0.24) + ((salary - 208300) * 0.32)
                finalsal = salary - tax
                print("Your Final Salary after tax is: $", finalsal)

            elif 264551 <= salary <= 661350:
                print("Your Tax percent is 35%")
                tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((salary - 69650) * 0.22) + ( (salary - 109100) * 0.24) + ((salary - 208300) * 0.32) + ((salary - 264551) * 0.35)
                finalsal = salary - tax
                print("Your Final Salary after tax is: $", finalsal)

            elif salary >= 661351:
                print("Your Tax percent is 37%")
                tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((salary - 69650) * 0.22) + ( (salary - 109100) * 0.24) + ((salary - 208300) * 0.32) + ((salary - 264551) * 0.35) + ((salary - 661350) * 0.37)
                finalsal = salary - tax
                print("Your Final Salary after tax is: $", finalsal)
        else:
            print("You Can't work more than 672 A month")





    elif userSal == 2:
        monthly_sal = int(input("Enter Monthly Salary: "))
        print("Your Monthly Salary is: $", monthly_sal)
        # tax
        if monthly_sal <= 18250:
            print("Your Tax percent is 10%")
            saltax = (0.10 * monthly_sal)
            finalsal = monthly_sal - saltax
            print("Your Final Salary after tax is: $", finalsal)

        elif 18251 <= monthly_sal <= 69650:
            print("Your Tax percent is 12%")
            tax = (18250 * 0.10) + ((monthly_sal - 18250) * 0.12)
            finalsal = monthly_sal - tax
            print("Your Final Salary after tax is: $", finalsal)

        elif 69651 <= monthly_sal <= 109100:
            print("Your Tax percent is 22%")
            tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((monthly_sal - 69650) * 0.22)
            finalsal = monthly_sal - tax
            print("Your Final Salary after tax is: $", finalsal)

        elif 109101 <= monthly_sal <= 208300:
             print("Your Tax percent is 24%")
             tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((monthly_sal - 69650) * 0.22) + ((monthly_sal - 109100) * 0.24)
             finalsal = monthly_sal - tax
             print("Your Final Salary after tax is: $", finalsal)

        elif 208301 <= monthly_sal <= 264550:
            print("Your Tax percent is 32%")
            tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((monthly_sal - 69650) * 0.22) + ((monthly_sal - 109100) * 0.24) + ((monthly_sal - 208300) * 0.32)
            finalsal = monthly_sal - tax
            print("Your Final Salary after tax is: $", finalsal)

        elif 264551 <= monthly_sal <= 661350:
            print("Your Tax percent is 35%")
            tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((monthly_sal - 69650) * 0.22) + ( (monthly_sal - 109100) * 0.24) + ((monthly_sal - 208300) * 0.32) + ((monthly_sal - 264551) * 0.35)
            finalsal = monthly_sal - tax
            print("Your Final Salary after tax is: $", finalsal)

        elif monthly_sal >= 661351:
            print("Your Tax percent is 37%")
            tax = (18250 * 0.10) + ((69650 - 18250) * 0.12) + ((monthly_sal - 69650) * 0.22) + ( (monthly_sal - 109100) * 0.24) + ((monthly_sal - 208300) * 0.32) + ((monthly_sal - 264551) * 0.35) + ((monthly_sal - 661350) * 0.37)
            finalsal = monthly_sal - tax
            print("Your Final Salary after tax is: $", finalsal)

    elif userSal == 3:
        quit()



