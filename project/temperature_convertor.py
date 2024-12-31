print("what you want to do?\n01.celsius to fahrenheit\n02.celsius to kelvin\n03.celsius to rankine\n04.fahrenheit to celsius\n05.fahrenheit to kelvin\n06.fehrenheit to rankine\n07.kelvin to celsius\n08.kelvin to fahrenheit\n09.kelvin to rankine\n10.rankine to celsius\n11.rankine to fahrenheit\n12.rankine to kelvin")
choice=str(input("enter your choice\n"))
initial_temperature = float(input("enter the temperature\n"))
if (choice == "celsius to fahrenheit"):
    final_temperature = initial_temperature*(9/5)+32
    print("temperature in fahrenheit is",final_temperature)
elif (choice == "celsius to kelvin"):
    final_temperature = initial_temperature + 273.15
    print("temperature in kelvine is",final_temperature)
elif (choice == "celsius to rankine"):
    final_temperature = initial_temperature*(9/5)+491.67
    print("temperature in rankine is",final_temperature)
elif (choice == "fahrenheit to celsius"):
    final_temperature = (initial_temperature - 32)*(5/9)
    print("temperature in calsius is",final_temperature)
elif (choice == "fahrenheit to kelvin"):
    final_temperature = ((initial_temperature - 32)*5/9)+273.15
    print("temperature in kelvin is",final_temperature)
elif (choice == "fahrenheit to rankine"):
    final_temperature = initial_temperature + 459.67
    print("temperature in rankine is",final_temperature)
elif (choice == "kelvin to celsius"):
    final_temperature = initial_temperature - 273.15
    print("temperature in celsius is",final_temperature)
elif (choice == "kelvin to fahrenheit"):
    final_temperature = ((initial_temperature - 273.15)*9/5)+32
    print("temperature in fahrenheit is",final_temperature)
elif (choice == "kelvin to rankine"):
    final_temperature = initial_temperature*9/5
    print("temperature in rankine is",final_temperature)
elif (choice == "rankine to celsius"):
    final_temperature = (initial_temperature - 491.67)*5/9
    print("temperature in celsius is",final_temperature)
elif (choice == "rankine to fahrenheit"):
    final_temperature = initial_temperature - 459.67
    print("tempreture in fahrenheit is",final_temperature)
elif (choice == "rankine to kelvin"):
    final_temperature = initial_temperature *5/9
    print("temperature in kelvin is",final_temperature)
else:
    print("wrong choice")