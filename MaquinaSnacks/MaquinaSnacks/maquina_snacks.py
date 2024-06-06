snacks = [
    {'id': 0, 'nombre': 'Papas', 'precio': 30},
    {'id': 1, 'nombre': 'Refrescos', 'precio': 50},
    {'id': 2, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos (Vacia)
productos = []

print('*** Maquina de Snacks ***')
print('Snacks Disponibles: ')
for snack in snacks:
    print(f"\tId: {snack['id']} -> "
          f"{snack['nombre']} - "
          f"Precio: {snack['precio']}")

def maquina_snacks(snacks, productos):
    salir = False
    while not salir:
        print('''Menu:
        1. Comprar snack
        2. Mostrar ticket
        3. Salir''')
        opcion = int(input('Selecciona una opcion: '))
        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            mostrar_ticket(productos)
        elif opcion == 3:
            print('Regresa pronto!')
            salir = True
        else:
            print('Opcion invalida. Selecciona otra opcion...\n')

def comprar_producto(snacks, productos):
    id_snack = int(input('Que snack quieres (Id)?: '))
    productos.append(snacks[id_snack])
    print(f'OK!, snack agregado. {snacks[id_snack]}')
def mostrar_ticket(productos):
    ticket = f'\t*** Ticket de Venta ***'
    total = 0
    for producto in productos:
        ticket += f"\n\t- {producto['nombre']} - {producto['precio']}€"
        total += producto['precio']
    ticket += f'\n\tTOTAL -> {total}€'
    print(ticket)

# Llamammos o Invocamos la funcion maquina snacks
maquina_snacks(snacks, productos)