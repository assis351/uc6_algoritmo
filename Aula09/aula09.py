# como criar uma funcao
def saudacao():
    print("Olá, seja bem-vindo")
#chamar uma funcao
saudacao()

#parametros sempre vao dentro de parenteses
def saudacao(nome):
    print("Olá,", nome ,"seja bem-vindo")
#chamar uma funcao
saudacao("Beltrano")

#recebe dois valores, faz a soma e retorna o resultado
def somar(valor1, valor2):
    return valor1 + valor2
resultado = somar(5,3)
print(resultado)

#soma dois valores se a idade do usuario for igual ou maior de 18
#senao mostrar mensagem "sua idade é menor que 18"
idade_usuario = int(input("Digite a sua idade:"))

if idade_usuario >= 18:
    var1 = int(input("digite o primeiro n°:"))
    var2 = int(input("digite o segundo n°:"))
    resultado= somar(var1,var2)
    print(resultado)
else:
    print("sua idade é menor que 18")
    
    
    