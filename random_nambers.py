#Gerando valores aleatórios

print('Olá, seja bem vindo, aqui temos várias funções ao seu dispor.'
    '\nPois bem, temos as seguintes funções:'
    '\nGerar valores aleatórios : 1'
    '\nCalculadora básica : 2'
    '\nCalculadora de média de notas anuais: 3'
    '\nVocê pode acessar cada uma pelo seu número correspondente'
    )

nmr_funcao = int(input('Insira o número correspondente a função desejada: '))

if nmr_funcao == 1:
    import random    

    class GerarNumero:
    #Parte da interface com o usuario INICIO
        def __init__(self):
            self.valor_minimo = int(input('Informe o valor mínimo = '))
            self.valor_maximo = int(input('Indorme o valor máximo = '))
            self.mensagem = input('Você gostaria de gerar um novo número? ')
            print(random.randint(self.valor_minimo,self.valor_maximo))
        #FINAL
        #Parte do tratamento e retorno dos dados INICIO
        def Iniciar(self):
            resposta = self.mensagem.lower()
            #try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValor()
            elif resposta == 'não' or resposta == 'n':
                print('Obrigado pela participação')
            else:
                print('Favor digitar apenas sim ou não')
                simulador = GerarNumero()
                simulador.Iniciar()

    #FINAL
    simulador = GerarNumero()
    simulador.Iniciar()

elif nmr_funcao == 2:
    try:
        a = int(input('Entre com o primeiro valor: '))
        b = int(input('Entre com o segundo valor: '))
        soma = a + b
        subtracao = a - b
        multiplicacao = a * b
        divisao = a / b
        resto = a % b
        print('Soma: {soma}'
            '\nSubtracao: {sub}'
            '\nMultiplicacao: {mult}'
            '\nDivisao: {div}'
            '\nResto: {resto}'.format(soma=soma,
                                                        sub=subtracao,
                                                        mult=multiplicacao,
                                                        div=divisao,
                                                        resto=resto))
    except:
        print('Erro na coleta ou processamento dos seu dados.'
        '\nFavor rodar o programa novamente e inserir apenas números, agradeçemos desde já pela participação.')


elif nmr_funcao == 3:

    try:
        a = int(input('insira a nota do primeiro bimestre:'))
        while a > 10:
            a = int(input('você digitou errado. primeiro bimestre: '))
        b = int(input('insira a nota do segundo bimestre: '))
        while b > 10:
            b = int(input('você digitou errado. segundo bimestre: '))
        c = int(input('insira a nota do terceiro bimestre: '))
        while c > 10:
            c = int(input('você digitou errado. terceiro bimestre: '))
        d = int(input('insira a nota do quarto bimestre: '))
        while d > 10:
            d = int(input('você digitou errado. quarto bimestre: '))
        media = (a + b + c + d) / 4
        print('média: {med}'.format(med=media))
    except:
        print('erro na coleta ou processamento de seus dados, favor, sertifique-se de que foram inseridos apenas números.')

elif nmr_funcao == 4:
        try:
            a = int(input('entre com o primeiro valor: '))
            b = int(input('entre com o segundo valor: '))
            c = int(input('entre com o terceiro valor: '))

            if a > b and a > c:
                print('o maior numero é {}'.format(a))
            elif b > a and b > c:
                print('o maior numero é {}'.format(b))
            else:
                print('o maior valor é {}'.format(c))
        except:
            print('erro na coleta ou processamento de seus dados, favor, sertifique-se de que foram inseridos apenas números.')

else: 
    print('Não existe número correspondente para essa função por enquanto, agradeçemos a participação UwU ')