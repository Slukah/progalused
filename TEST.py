months = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober",
          "november", "detsember"]
Genders = ["mees", "naine", "mees", "naine", "mees", "naine", "mees", "naine"]

ID = input("Sisestage oma isikukood: ")

if len(ID) == 11:
    esimeneJark = ((int(ID[0]) * 1) + (int(ID[1]) * 2) + (int(ID[2]) * 3) +
                   (int(ID[3]) * 4) + (int(ID[4]) * 5) + (int(ID[5]) * 6) +
                   (int(ID[6]) * 7) + (int(ID[7]) * 8) + (int(ID[8]) * 9) + (
                           int(ID[9]) * 1)) % 11
    if esimeneJark == 10:
        esimeneJark = ((int(ID[0]) * 3) + (int(ID[1]) * 4) + (int(ID[2]) * 5) + (
                int(ID[3]) * 6) +
                       (int(ID[4]) * 7) + (int(ID[5]) * 8) + (int(ID[6]) * 9) + (
                               int(ID[7]) * 1) +
                       (int(ID[8]) * 2) + (int(ID[9]) * 3)) % 11
    if esimeneJark == int(ID[10]):
        for sex in Genders:
            sex = int(ID[0])
            Gender = Genders[sex - 1]
        if 8 >= int(ID[0]) >= 1:
            if int(ID[0]) == 1 or int(ID[0]) == 2:
                aasta = "18" + str(ID[1] + ID[2])
            if int(ID[0]) == 3 or int(ID[0]) == 4:
                aasta = "19" + str(ID[1] + ID[2])
            if int(ID[0]) == 5 or int(ID[0]) == 6:
                aasta = "20" + str(ID[1] + ID[2])
            if int(ID[0]) == 7 or int(ID[0]) == 8:
                aasta = "21" + str(ID[1] + ID[2])
            for MonthName in months:
                month = int(ID[3] + ID[4])
                MonthName = months[month - 1]
            if 1 <= month <= 12:
                day = int(ID[5] + ID[6])
                if 1 <= day <= 31:
                    print("Tervist, oled " + Gender + ". Sündisid aastal " + aasta + ", sünnipäev on " + str(
                        day) + ". " + MonthName)
                else:
                    print("Viga! Proovi uuesti!")
            else:
                print("Viga! Proovi uuesti!")
        else:
            print("Viga! Proovi uuesti!")
    else:
        print("Viga! Proovi uuesti!")
else:
    print("Viga! Proovi uuesti!")
