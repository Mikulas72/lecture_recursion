def Fibonnaciho_posloupnost(cislo):
    if cislo < 2:
        if cislo == 0:
            return 0
        else:
            return 1

    return Fibonnaciho_posloupnost(cislo - 1) + Fibonnaciho_posloupnost(cislo - 2)



def main():
    vstup = int(input("Vstupní číslo:"))
    sekvence = [Fibonnaciho_posloupnost(cislo=vstup) for vstup in range(vstup + 1)]

    print(sekvence)

    pass


if __name__ == "__main__":
    main()
