carrito = [
    {"item": "Manzanas", "price": 1.50},
    {"item": "Pan", "price": 2.00},
    {"item": "Leche", "price": 1.20},
    {"item": "Huevos", "price": 3.50},
    {"item": "Queso", "price": 4.75}
]

total = 0

print("--- Carrito de Compras ---")
for producto in carrito:
    total += producto["price"]
    print(f"{producto['item']}: ${producto['price']} | Total acumulado: ${total:.2f}")

print(f"\nTOTAL A PAGAR: ${total:.2f}")
