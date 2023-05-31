# Conversion_calculator
Purpose: 
Changes pounds to kg and vise versa , as well as Fahrenheit to Celsius and vice versa 
The program is useful for users who need quick conversion, or something quickly converted, this can be helpful for school, work, or daily life. For example, if you needed to know the weight in pounds of yourself for school, but you dont know you weight in pounds, this converter would be able to help 


Functionality: 
The program is a simple conversion program that allows users to convert between different units of weight and temperature. 
Two functions are specified by the programme: convert_weight(Pkg) and convert_temp(Fc). The logic for weight and temperature conversions is handled by these routines.

To convert between kilogrammes (kg) and pounds (lbs), use the convert_weight(Pkg) function. It requires the parameter Pkg, which stands for the weight unit the user wants to convert.

a. The user is prompted to input the weight in kilogrammes if Pkg is "kg". The programme then uses the conversion factor of 0.45359237 to determine the equivalent weight in pounds and publishes the result.

b. The user is requested to input the weight in pounds if Pkg is "lbs". The programme then multiplies the input by the conversion factor, which is 0.45359237, to determine the equivalent weight in kilogrammes, and prints the result.


The conversion of temperature between Fahrenheit (F) and Celsius (C) is handled by the convert_temp(Fc) function. It requires a parameter called Fc, which stands for the temperature unit the user wants to convert.

a. The user is prompted to specify the temperature in Fahrenheit if Fc is "F". The programme then uses the conversion formula (amount - 32) * 5/9 to determine the corresponding temperature in Celsius and prints the result.

b. The user is prompted to specify the temperature in Celsius if Fc is "C". The programme then uses the conversion formula quantity * 9/5 + 32 to determine the corresponding temperature in Fahrenheit and prints the result.

The central portion of the programme begins by asking the user which unit they want to convert: temperature (T) or weight (W). The variable Wt holds the user's input.

When converting weight (Wt is "W" or "w"), the user is given the option of doing it in either kilogramme (Kg) or pounds (lbs). The variable Pkg contains the user's input. The conversion is then carried out using the selected choice by calling the convert_weight(Pkg) function.

The user is given the option to convert between Fahrenheit and Celsius (F) or Celsius and Fahrenheit (C) if they want to change the temperature (Wt is "T" or "t"). The variable Fc holds the user's input. The conversion is then carried out using the selected option by calling the convert_temp(Fc) function.




