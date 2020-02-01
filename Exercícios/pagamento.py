# Programa para o cálculo de uma folha de pagamento, Os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
# 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto Desconto IR
# Até 1.900 isento
# De 1.901 até 2.800 7%  /  if pagamento = 1900: 
# De 2.801 até 3.700 15%
# de 3.701 até 4.600 22%
# Acima de 4.600 27%



vlr_hora = float(input('Digite valor da hora: '))
qtd_hora = float(input('Digite a quantidade de horas trabalhadas: '))
sal_bruto = vlr_hora * qtd_hora

if sal_bruto > 4600:
    desconto_ir = (sal_bruto * 0.27)
    val_alicota = '27%'
elif sal_bruto > 3701:
    desconto_ir = (sal_bruto * 0.22)
    val_alicota = '22%'
elif sal_bruto > 2801:
    desconto_ir = (sal_bruto * 0.15)
    val_alicota = '15%'
elif sal_bruto > 1901:
    desconto_ir = (sal_bruto * 0.07)
    val_alicota = '7%'
else:
    desconto_ir = 0.0
    val_alicota = '0%'

desconto_sind = sal_bruto * 0.03
desconto_total = desconto_ir + desconto_sind
fgts = sal_bruto * 0.11
sal_liq = sal_bruto - desconto_total
print('valor da hora:', vlr_hora)
print('Quantidade de horas trabalhadas: ',qtd_hora)
print('Salario Bruto R$: ', sal_bruto)
print('(-) IR (', val_alicota,'):', desconto_ir)
print('(-) Sindicato (3%):',desconto_sind)
print('FGTS: ',fgts)
print('Total de descontos',desconto_total)
print('Salario líquido: ',sal_liq)


