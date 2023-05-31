def convert_weight(Pkg):
    if Pkg.lower() == "kg":
        amount = input("how many kgs")
        lbs = float(amount) / 0.45359237
        print(f"{amount} kilograms is equal to {lbs} pounds.")
    elif Pkg.lower() == "lbs":
        amount = input("how many lbs")
        kg = amount * 0.45359237
        print(f"{amount} pounds is equal to {kg} kilograms.")

def convert_temp(Fc):
    if Fc.lower() == "f":
        amount = input("Whats the Current Tempreture?")
        Cel = (float(amount) - 32 ) * 5 / 9
        print(f"{amount} Fahrenheit is equal to {Cel} Celsius")
    elif Fc.lower()== "c":
        amount = input("Whats the Current Tempreture?")
        Far = (float(amount)) * 9 / 5 + 32 
        print(f"{amount} degrees Celsius is equal to {Far} degrees Fahrenheit.")


Wt = input("Are you intrested in converting Weight(W) or Tempreture?(T)")
if Wt == "W":
    Pkg = input ("Would you like to change Kilograms to Pounds (Kg) Or Pounds to Kilograms (lbs)?")
    converted_weight = convert_weight(Pkg)
elif Wt == "T":
    Fc = input ("Would you like to convert Fahrenheit to Celsius(F) or Celsius to Fahrenheit (C) ?")
    converted_temp = convert_temp(Fc)
 
