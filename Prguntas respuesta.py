respuesta_nombre= input("¿Cómo te llamas?")

print("Hola " + respuesta_nombre)

pregunta1= input("¿Te ceunto un chiste?")

if pregunta1 == "si":
    
    print("el pepe")

else:
    
    pregunta2= input("¿Cúal es tu color favorito?")
    
    print("Odio el " + pregunta2)
    

pregunta3= input("Cúal es tu comida favorita?")

print("Me encnata esa comida: " + pregunta3)


pregunta4= input("¿Te cuento la historia de España?")

if pregunta4 == "si":
    
    print("""Los primeros homínidos llegaron al territorio de la actual España hace 1,2 millones de años aproximadamente.""")
else:
    
    print("Adiós")