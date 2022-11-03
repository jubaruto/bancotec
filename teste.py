from models.cliente import Cliente
from models.conta import Conta

baruto: Cliente = Cliente('Baruto', 'baruto@gmail.com', '987.654.321-00', '13/10/1985')
mury: Cliente = Cliente('Mury', 'mury@gmail.com', '12.456.789-00', '27/05/1988')

# print(baruto)
# print(mury)

contabaruto: Conta = Conta(baruto)
contamury: Conta = Conta(mury)

print(contabaruto)
print(contamury)
