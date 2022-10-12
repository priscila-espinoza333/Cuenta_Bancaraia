from BancoDojo import BancoDojo

cta_cliente01 = BancoDojo("Margarita", "Reyes", "numero cta 111", 800000)
cta_cliente02 = BancoDojo("Matiah", "Chinasky", "nuemro cta 222", 500000)
cta_cliente03 = BancoDojo("Frank", "Mezco", "numero de cta 333", 789000)

cta_cliente01.retiro(20000).generar_interes().depósito(5000).depósito(10000).deposito(20000).mostrar_info_cta()("/n")
cta_cliente02.depósito(5000).depósito(5000).depósito(5000).retiro(1000).retiro(1000).retiro(500).retiro(1000).generar_interes().mostrar_info_cta()

BancoDojo.ctas_bancarias()