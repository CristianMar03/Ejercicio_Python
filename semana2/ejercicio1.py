print("Bienvenidos a la mejor pizzería: Bella Napoli. \nTipos de pizzas:\n\t1- Vegetariana\n\t2- No Vegetariana")
tipo= input("Introduce el número de correspondiente a la pizza que deseas pedir: ")
if tipo=="1":
    print("Ingredientes de pizzas vegetarianas\n\t1- Pimiento\n\t2- Tofu\n ")
    ingrediente= input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente=="1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón ")
    ingrediente= input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente=="1":
        print("peperoni")
    elif ingrediente=="2":
        print("jamón")
    else:
        print("salmón")