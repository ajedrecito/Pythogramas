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
    
    print("""Los primeros homínidos llegaron al territorio de la actual España hace 1,2 millones de años aproximadamente. Se sucedieron varias especies, como Homo antecessor, los preneandertales de la Sima de los Huesos (identificados en un principio como Homo heidelbergensis) y los neandertales (Homo neanderthalensis), hasta que hace unos 35 000 años los humanos modernos (Homo sapiens) entraron en la península ibérica y fueron desplazando a estos últimos, con los que aún coexistirían durante cerca de 10 000 años. Hace unos 27 000 años se extinguieron las últimas poblaciones neandertales en el sur. Durante los milenios siguientes el territorio fue lugar del asentamiento de pueblos íberos, celtas, fenicios, cartagineses, tartessos y griegos y hacia el 200 a. C. la península comenzó a formar parte de la República romana, constituyendo la Hispania romana. Tras la caída de Roma, se estableció el reino visigodo. Dicha monarquía visigótica se inició en el siglo V y se mantuvo hasta comienzos del siglo VIII. En el año 711 se produjo la primera conquista musulmana desde el norte de África y en pocos años el islam dominaba gran parte de la península ibérica. Durante los 750 años siguientes, el reino dominado por musulmanes sería conocido como al-Ándalus, y mientras que gran parte del resto de Europa permanecía en los años oscuros, Al-Ándalus experimentaba un esplendoroso florecimiento multicultural, científico y artístico.1​""")

else:
    
    print("Adiós")