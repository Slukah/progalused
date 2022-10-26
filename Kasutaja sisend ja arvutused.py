nimi = str(input("Sisestage oma nimi: "))
lubatud = int(input("Sisestage lubatud kiirus: "))
tegelik = int(input("Sisestage tegelik kiirus: "))
summa = (int(tegelik) - int(lubatud)) * 3
print(f"{nimi} kiiruse ületamise eest on teie trahv {summa}")
