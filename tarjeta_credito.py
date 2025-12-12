class TarjetaCredito:
    # Bonus: Lista para guardar instancias
    lista_tarjetas = []

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.lista_tarjetas.append(self)

    def compra(self, monto):
        if (self.saldo_pagar + monto) <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada: has alcanzado tu límite de crédito.")
        return self # Permite encadenación

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += (self.saldo_pagar * self.intereses)
        return self

    # Método de clase (Bonus)
    @classmethod
    def imprimir_reporte(cls):
        print("\n--- Reporte General ---")
        for i, tarjeta in enumerate(cls.lista_tarjetas, 1):
            print(f"Tarjeta {i}:")
            tarjeta.mostrar_info_tarjeta()

# --- EJECUCIÓN ---

# 1. Crear instancias
t1 = TarjetaCredito(20000, 0.02) 
t2 = TarjetaCredito(10000, 0.05)
t3 = TarjetaCredito(5000, 0.03)

# 2. Operaciones encadenadas
print("--- Tarjeta 1 ---")
t1.compra(500).compra(1000).pago(200).cobrar_interes().mostrar_info_tarjeta()

print("\n--- Tarjeta 2 ---")
t2.compra(100).compra(200).compra(300).pago(50).pago(50).cobrar_interes().mostrar_info_tarjeta()

print("\n--- Tarjeta 3 ---")
# Intentamos exceder el límite (5 compras de 1100 = 5500 > 5000)
t3.compra(1100).compra(1100).compra(1100).compra(1100).compra(1100).mostrar_info_tarjeta()

# 3. Bonus
TarjetaCredito.imprimir_reporte()