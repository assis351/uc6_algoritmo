#append()
frutas = ["maçã","banana"]
frutas.append("laranja")
print(frutas) #['maçã','banana','laranja']

#insert()
frutas = ["maçã","banana"]
frutas.insert(1,"uva")
print(frutas) #['maçã','uva','banana']

#extend()
a=[1,2]
b=[3,4]
a.extend(b)
print(a) #[1,2,3,4]

#remove()
numeros = [1,2,3]
numeros.remove(2)
print(numeros) #[1,3]

#pop()
numeros=[1,2,3]
numeros.pop()
print(numeros) #[1,2]

#clear()
dados=[1,2,3]
dados.clear()
print(dados) #[]

#index()
letras=["a","b","c"]
print(letras.index("b")) #1

#count()
nums = [1,1,2,3]
print(nums.count(1)) #2

#sort()
nums = [3,1,2]
nums.sort()
print(nums) #[1,2,3]

#reverse()
nums = [1,2,3]
nums.reverse()
print(nums)  #[3,2,1]
