
def main():
    Zahl1 = float(input("Gib eine Zahl ein"))
    Zahl2 = float(input("Gib eine weiter Zahl ein"))
    Operator = str(input("gib bitte ein Rechen operator ein +, -, //, **, * "))

    if Operator == "*":
        print(f"{Zahl1}{Operator}{Zahl2} = {Zahl1*Zahl2}")
    elif Operator == "**":
        print(f"{Zahl1}{Operator}{Zahl2} = {Zahl1**Zahl2}")
    elif Operator == "//":
        print(f"{Zahl1}{Operator}{Zahl2} = {Zahl1//Zahl2}")
    elif Operator == "+":
        print(f"{Zahl1}{Operator}{Zahl2} = {Zahl1+Zahl2}")
    elif Operator == "-":
        print(f"{Zahl1}{Operator}{Zahl2} = {Zahl1-Zahl2}")
    else :
        print("Operator ungueltig")


main()










