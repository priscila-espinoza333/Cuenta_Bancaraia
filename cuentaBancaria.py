class CuentaBancaria:

    ctas_bancarias = []

    def __init__(self, nombre_completo, id_cuenta, balance):
        self.nombre_completo = nombre_completo
        self.id_cuenta = id_cuenta
        self.balance = balance 
        self.tasa_interés = 0,2 

        CuentaBancaria.ctas_bancarias.append(self)


    def depósito(self, valor_incremento)
