# Created BY Mj Parastar

Continuation_Request = 'A'


def Print_Line():
    print("--------------------------")


def Print_Pivot(Pivot):
    print(f"Pivot is {Pivot}")


def Print_Support(Support1, Support2, Support3, Support4, Support_Average):
    print(f"Support : \n \
 Support1 is {Support1}\n \
 Support2 is {Support2}\n \
 Support3 is {Support3}\n \
 Support4 is {Support4}\n \
 Support Average is {Support_Average}")


def Print_Resistance(Resistance1, Resistance2, Resistance3, Resistance4, Resistance_Average):
    print(f"Resistance : \n \
 Resistance1 is {Resistance1} \n \
 Resistance2 is {Resistance2} \n \
 Resistance3 is {Resistance3} \n \
 Resistance4 is {Resistance4} \n \
 Resistance Average is {Resistance_Average}")


while (Continuation_Request == 'A'):

    print("Please Enter Close, High and Low of The Candle:")

    Close = float(input("Close: "))
    High = float(input("High: "))
    Low = float(input("Low: "))

    Pivot = (Close + High + Low) / 3

    Resistance1 = 2 * Pivot - Low
    Resistance2 = Pivot + (High - Low)
    Resistance3 = Resistance1 + (High - Low)
    Resistance4 = Resistance2 + (High - Low)

    Resistance_Average = (Resistance1 + Resistance2) / 2

    Support1 = 2 * Pivot - High
    Support2 = Pivot - (High - Low)
    Support3 = Support1 - (High - Low)
    Support4 = Support2 - (High - Low)

    Support_Average = (Support1 + Support2) / 2

    Request_User = input("Which one do you want ? \n \
        A : Pivot \n \
        B : Pivot , Resistance \n \
        C : Pivot , Support \n \
        D : Resistance , Support \n \
        E : all of them \n ")

    if Request_User == 'A' or Request_User == 'a':
        Print_Line()
        Print_Pivot(Pivot)
        Print_Line()

    elif Request_User == 'B' or Request_User == 'b':
        Print_Line()
        Print_Pivot(Pivot)
        Print_Line()
        Print_Resistance(Resistance1, Resistance2,
                         Resistance3, Resistance4, Resistance_Average)
        Print_Line()

    elif Request_User == 'C' or Request_User == 'c':
        Print_Line()
        Print_Pivot(Pivot)
        Print_Line()
        Print_Support(Support1, Support2, Support3, Support4, Support_Average)
        Print_Line()

    elif Request_User == 'D' or Request_User == 'd':
        Print_Line()
        Print_Resistance(Resistance1, Resistance2,
                         Resistance3, Resistance4, Resistance_Average)
        Print_Line()
        Print_Support(Support1, Support2, Support3, Support4, Support_Average)
        Print_Line()

    elif Request_User == 'E' or Request_User == 'e':
        Print_Line()
        Print_Pivot(Pivot)
        Print_Line()
        Print_Resistance(Resistance1, Resistance2,
                         Resistance3, Resistance4, Resistance_Average)
        Print_Line()
        Print_Support(Support1, Support2, Support3, Support4, Support_Average)
        Print_Line()

    else:
        print("Undefined Request")

    Continuation_Request = input(
        "if you want continue Enter A and for Exit Enter B : \n")
