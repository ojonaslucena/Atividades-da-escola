v1=float(input('Digite o primeiro valor:\n'))
v2=float(input('Digite o segundo valor:\n'))
op=input('Qual operação deseja fazer? *adição, subtração, divisão ou multiplicação\n')
if op=='adição':
    print('O resultado é:', v1+v2)
elif op=='subtração':
    print('O resultado é:', v1-v2) 
elif op=='divisão':
    print('O resultado é:', v1/v2) 
elif op=='multiplicação':
    print('O resultado é:', v1*v2)          