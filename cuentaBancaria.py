class BancoDojo:

    ctas_bancarias = []

    def __init__(self, nombre_completo, id_cuenta, balance):
        self.nombre_completo = nombre_completo
        self.id_cuenta = id_cuenta
        self.balance = balance 
        self.tasa_interés = 0,2 

        BancoDojo.ctas_bancarias.append(self)


    def depósito(self, valor_dep):
        self.balance += valor_dep
        if self.balance + 1:
            print(f"Has recibido  un deposito en tu cuenta por un monto de $+{valor_dep}")
        return self

    def retiro(self, valor_retiro):
        self.balance -= 10
        self.balance -= valor_retiro
        if self.balance < valor_retiro:
            print(f"Saldo disponible de: ${self.balance}, no es posible retirar esa cantidad")
            return self
        else:
            print(f"Tu retiro por: ${self.balance} se ralizado con exito.Por favor retira tu dinero")    

    def mostrar_info_cta(self):
        print(f"Tu saldo disponible es de: $ {self.balance} ")
        return self 

    def generar_interes(self):
        self.balance = self.balance * self.tasa_interés
        print(f"El total de tu saldo con tasa de interés es de: $ {self.balance}")    
        return self

    
    @classmethod
    def total_ctas(cls):
        print("Total clientes:", len(cls.ctas_bancarias))
        for ctaBancaria in cls.ctas_bancarias:
            print(f"Nombre Cliente {nombre_completo}")
            print(f"Id Cuenta {id_cuenta}")
            print(f"Balance {balance}")
            print(f"Tasa Interés {tasa_interés}\n")
    
