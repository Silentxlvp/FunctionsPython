#Caulcula volume, área lateral, área de base e área total de cilindros :    )


from cmath import pi


print('calculadora de cilindros.')
print('calcula o volume = 1 ' 
'\ncalcula a área lateral = 2'
'\ncalcula a área da base = 3'
'\ncalcula a áres total = 4')
try:
    a = int(input('insira o número da função desejada = '))
    if a == 1:
    #volume
        vol_h = int(input('insira a altura do cilindro = '))
        vol_r = int(input('insira o valor do raio = '))
        raio = vol_r*vol_r
        resultado_vol = raio*vol_h*pi
        print('O resultado é:', resultado_vol)

    elif a == 2:
    #área lateral
        vol_h = int(input('insira a altura do cilindro = '))
        vol_r = int(input('insira o valor do raio = '))
        Al = 2*3.14*vol_r*vol_h
        print('O resultado é:', Al)

    elif a == 3:
    #área da base
        vol_r = int(input('insira o valor do raio = '))
        resul_Ab = vol_r*vol_r*3.14
        print('O resultado é:', resul_Ab)

    elif a == 4:
    #área total
        vol_h = int(input('insira a altura do cilindro = '))
        vol_r = int(input('insira o valor do raio = '))
        resul_Ab = vol_r*vol_r*3.14 #área da base
        Ab = resul_Ab*2
        Al = 2*3.14*vol_r*vol_h
        At = Ab + Al
        print(At)

except:
    print('favor digitar apenas números :)')
