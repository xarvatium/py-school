def FToC(F = int):
    C = (float(F) - 32) / 1.8
    print(f'The temperature is {C}°C')


def FToK(F = float):
    K = ((float(F) -32) / 1.8) + 273.15
    print(f'The temperature is {K}K')


def CToF(C = float):
    F = (float(C) * 1.8) + 32
    print(f'The temperature is {F}°F')


def CToK(C = float):
    K = float(C) + 273.15
    print(f'The temperature is {K}K')


def KToF(K = float):
    F = (float(K) * 1.8) + 32
    print(f'The temperature is {F}°F')


def KToC(K = float):
    C = float(K) - 273.15
    print(f'The temperature is {C}°C')


while True:
    userinput = input("What unit do you have? (C/F/K, or 'z' to exit) ").lower()

    if userinput == "c":
        toconvert = input("What unit do you wish to convert that to? ").lower()
        C = input("What is the temperature? ")
        if toconvert == "f":
            CToF(C)

        elif toconvert == "k":
            CToK(C)

        else:
            print("Invalid input. (Did you try to convert C to C?)")

    elif userinput == "f":
        toconvert = input("What unit do you wish to convert that to? ").lower()
        F = input("What is the temperature? ")
        if toconvert == "c":
            FToC(F)

        elif toconvert == "k":
            FToK(F)

        else:
            print("Invalid input. (Did you try to convert F to F?)")

    elif userinput == "k":
        toconvert = input("What unit do you wish to convert that to? ").lower()
        K = input("What is the temperature? ")
        if toconvert == "c":
            KToC(K)

        elif toconvert == "f":
            KToF(K)

        else:
            print("Invalid input (Did you try to convert K to K?)")

    elif userinput == "z":
        print("Exiting...")
        quit()

    else:
        print("Invalid input.")