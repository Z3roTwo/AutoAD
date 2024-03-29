# Import all the modules needed
import time, subprocess, sys, csv, random, string, platform

# List all the variables
menu = True
option = 0
arraynumber1 = 0
arraynumber2 = 0
chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "1234567890"
chars2 = "!#%&/()="
password = ""
systemOS = platform.system()
userfile = "Users.csv"
amount = 0
amountloop = True
fileloop = True


# Menu
while menu:
    option = input('''[1] Skapa Användare
[2] Ta bort användare
[3] Rensa Password.txt
[4] Stäng programmet
Val: ''')
    if option == "1" or option == "2":
        if option == "1":
            print("Skapa användare")
            while fileloop:
                userfile = input("Välj .csv fil: ")
                try:
                    with open(userfile) as CSVfile:
                        readCSV = csv.reader(CSVfile, delimiter=',')
                        names = []
                        surnames = []
                        passwords = []
                        for row in readCSV:
                            name = row[1]
                            surname = row[2]
                            names.append(name)
                            surnames.append(surname)
                            for yeet in range(2):
                                password += random.choice(chars)
                                password += random.choice(chars.upper())
                                password += random.choice(chars1)
                                password += random.choice(chars2)
                                password = ''.join(random.sample(password, len(password)
                                ))
                            passwords.append(password)
                            password = ""
                        print(f'Filen innehåller {len(names)}st rader')
                        while amountloop:
                            arraynumber1 = int(input("Starta från rad: "))
                            arraynumber2 = int(input("Stoppa på rad: "))
                            if arraynumber2 > len(names) - 1:
                                arraynumber2 = len(names) - 1
                            amount = arraynumber2 - arraynumber1 + 1
                            if input(f"Detta kommer försöka skapa {amount} användare. Välj 'a' för att fortsätta: ") == "a":
                                amountloop = False
                        while arraynumber1 <= arraynumber2:
                            print(names[arraynumber1], surnames[arraynumber1], passwords[arraynumber1])
                            if systemOS == "Windows":
                                cmd = f'New-ADUser -Name "{names[arraynumber1]} {surnames[arraynumber1]}" -GivenName "{names[arraynumber1]}" -Surname "{surnames[arraynumber1]}" -SamAccountName "{names[arraynumber1][0] + "." + surnames[arraynumber1]} " -AccountPassword (ConvertTo-SecureString "{passwords[arraynumber1]}" -AsPlainText -force) -passThru -ChangePasswordAtLogon $True -Enabled $True'
                                cmd2 = f'echo "{passwords[arraynumber1]}" >> Passwords.txt'
                                echothepass = subprocess.call(['powershell', cmd2])
                                returned_value = subprocess.call(['powershell', cmd])
                                print(cmd)
                                print("returned_value: ", returned_value)
                            elif systemOS == "Linux":
                                cmd = f'sudo useradd --password "{passwords[arraynumber1]}" -c "{names[arraynumber1]} {surnames[arraynumber1]}" -m {names[arraynumber1]}.{surnames[arraynumber1]}'
                                returned_value = subprocess.call(cmd, shell=True)
                                print("returned_value: ", returned_value)
                            else:
                                arraynumber1 = arraynumber2 - 1
                                print("This OS is not supported please switch to Windows or Ubuntu")
                            arraynumber1 += 1
                    fileloop = False
                except  Exception as e:
                    print("Filen finns inte, kom ihåg att den är caps känslig och måste sluta med filtillägget.")
                    print(e)
        else:
            while fileloop:
                userfile = input("Välj .csv fil: ")
                try:
                    with open(userfile) as CSVfile:
                        readCSV = csv.reader(CSVfile, delimiter=',')
                        names = []
                        surnames = []
                        for row in readCSV:
                            name = row[1]
                            surname = row[2]
                            names.append(name)
                            surnames.append(surname)
                        while amountloop:
                            arraynumber1 = int(input("Start From Row: "))
                            arraynumber2 = int(input("Stop at Row: "))
                            if arraynumber2 > len(names) - 1:
                                arraynumber2 = len(names) - 1
                            amount = arraynumber2 - arraynumber1 + 1
                            if input(f"Detta kommer ta bort användare #{arraynumber1} till användare #{arraynumber2}. Välj 'a' för att fortsätta: ") == "a":
                                amountloop = False
                        while arraynumber1 <= arraynumber2:
                            print(names[arraynumber1], surnames[arraynumber1])
                            if systemOS == "Windows":
                                cmd = f'Remove-ADUser -Identity {names[arraynumber1][0] + "." + surnames[arraynumber1]}'
                                returned_value = subprocess.call(['powershell', cmd])
                                print(cmd)
                                print("returned_value: ", returned_value)
                            elif systemOS == "Linux":
                                cmd = f'userdel "{names[arraynumber1]} {surnames[arraynumber1]}"'
                                returned_value = subprocess.call(cmd, shell=True)
                                print("returned_value: ", returned_value)
                            else:
                                arraynumber1 = arraynumber2 - 1
                                print("This OS is not supported please switch to Windows or Ubuntu")
                            arraynumber1 += 1
                    fileloop = False
                except Exception as e:
                    print("Filen finns inte, kom ihåg att den är caps känslig och måste sluta med filtillägget.")
                    print(e)
    elif option == "3":
        print("Stänger av..")
        time.sleep(0.5)
        menu = False
    else:
        print("Välj ett av de tre alternativen")

    # Reset all needed Variables
    option = 0
    arraynumber1 = 0
    arraynumber2 = 0
    amount = 0
    amountloop = True
    fileloop = True