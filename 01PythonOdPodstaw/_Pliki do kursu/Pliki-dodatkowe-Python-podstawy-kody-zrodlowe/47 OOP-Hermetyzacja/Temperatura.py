from Thermometer import Thermometer

temp = float(input("Podaj temperaturę: "))
unit = input("Podaj jednostkę \"C\" dla Celsjusza, \"K\" - Kelwina i \"F\" - Fahrenheita: ")

term = Thermometer()
term.setTemperature(temp,unit)

while True:
    choice = int(input("Wpisz \"0\" jeżeli chcesz otrzymać temperaturę w jakiejś jednostce lub \"1\" jeżeli chcesz nadać inną temperaturę. \"9\" Jeżeli chcesz zakończyć: "))
    if choice == 9:
        break
    elif choice == 0:
        unit = input("Podaj jednostkę \"C\" dla Celsjusza, \"K\" - Kelwina i \"F\" - Fahrenheita: ")
        print(term.getTemperature(unit))
    elif choice == 1:
        temp = float(input("Podaj temperaturę: "))
        unit = input("Podaj jednostkę \"C\" dla Celsjusza, \"K\" - Kelwina i \"F\" - Fahrenheita: ")
        term.setTemperature(temp, unit)
    else:
        pass