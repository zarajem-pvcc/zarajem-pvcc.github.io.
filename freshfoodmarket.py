# Name: Balthazar Ajemian
# Prog Purpose: This program creates payroll report

import datetime

############## Lists of data ###########
emp = [
    "Smith, James      ",
    "Johnson, Patricia ",
    "Williams, John    ",
    "Brown, Micheal    ",
    "Jones, Elizabeth  ",
    "Garcia, Brian     ",
    "Miller, Deborah   ",
    "Davis, Timothy    ",
    "Rodriguez, Ronald ",
    "Martinez, Karen   ",
    "Hernandex, Lisa   ",
    "Lopez, Nancy      ",
    "Gonzales, Betty   ",
    "Wilson, Sandra    ",
    "Anderson, Margie  ",
    "Thomas, Daniel    ",
    "Taylor, Steven    ",
    "Moore, Andrew     ",
    "Jackson, Donna    ",
    "Martin, Yolanda   ",
    "Lee, Carolina     ",
    "Perez, Kevin      ",
    "Thomson, Brian    ",
    "White, Deborah    ",]

job = ["C", "S", "J", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 29, 21, 31]

num_emps = len(emp)

######### NEW LISTS for calculated amounts #####

gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medi = []
retrment = []
net_pay = []

total_gross = 0
total_net = 0

############## TUPLES of constants #############
#           C       S       J       M
# indexes   0       1       3       4
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

#           fed  state  ss   med    ret
# indexes    0     1    3     4      5
DED_RATE = (.12, .03, .062, .0145, .04 )

############## define program functions ###############
def main():
    get_user_data()
    perform_calculations()
    display_results()
def get_user_data():
    global job, hours

    for i in range(num_emps):
        hours.append(int(input(f"How many hours did {emp[i]} work? : ")))
        job.append(input(f"What is {emp[i]}'s assigned job? Cashier (C), Stocker (S), Janitorial (J), or Maintenance (M)? : "))

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):
        # calc gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[3]

        # calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        soc = pay * DED_RATE[2]
        medicare = pay * DED_RATE[3]
        retirement = pay * DED_RATE[4]

        total_net = pay - fed - state - medicare - retirement - soc
        total_deductions = fed + state + medicare + retirement + soc
        total_gross += pay

        # append amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(soc)
        medi.append(medicare)
        retrment.append(retirement)
            

def display_results():
    currency = '8,.2f'
    line = '-----------------------------------------------'
    tab = "\t"

    print(line)
    print('************** FRESH FOODS MARKET **************')
    print('------------ WEEKLY PAYROLL REPORT -------------')
    print(tab + str(datetime.datetime.now()))
    print(line)
    titles1 = "Emp Name" + tab + "Code" + tab + "Hours" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Retirement" + tab + "Net"
    print(titles1 + titles2)

    for i in range(num_emps):
        data = f"{emp[i]} {job[i]} {hours[i]} {format(gross_pay[i], currency)} {format(fed_tax[i], currency)} {format(state_tax[i], currency)} {format(soc_sec[i], currency)} {format(medicare[i], currency)} {format(retrment[i], currency)} {format(total_net, currency)}"
        print(data)

    print(line)
    print("******************** TOTAL GROSS: $" + format(total_gross, currency))
    print("******************** TOTAL NET  : $" + format(total_net, currency))
    print(line)

main()





    
