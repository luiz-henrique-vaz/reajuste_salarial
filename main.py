salario = float(input('digite o salario'))

if (salario <= 280):
   reajuste = 0.2
elif (salario > 280 and salario <= 700):
   reajuste = 0.15
elif (salario > 700 and salario <= 1500):
   reajuste = 0.10
else:
   reajuste = 0.5

valor_reajuste = salario * reajuste

salario_reajustado = salario + valor_reajuste

print( 'salario antes do reajuste: ' + str (salario))
print('valor do reajuste: ' + str(valor_reajuste))
print('percentual: ' + str (reajuste))
print('novo salario: ' + str (salario_reajustado))

