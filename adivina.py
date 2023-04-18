while True:
    numero=int(input("Adivine el numero: "))
    if numero<50:
        print("Demasiado bajo intente de nuevo")
    elif numero<154:
        print("Casi,intenta con un numero un poco mas alto")  
    elif numero>=156:
        print("Se paso un poco") 
    elif numero==155:
        print("Felicidades es el 155")
        break            

