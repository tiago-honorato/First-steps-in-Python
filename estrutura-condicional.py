'''
As estruturas condicionais (if, elif, else) em Python  não requerem chaves {} para delimitar os blocos de código,
em vez disso, a indentação é usada para determinar os blocos de código.
'''
idade = 23

if idade >= 18:

    print("Você é maior de idade.")
    
#elif é a junção de else + if.
elif idade >= 13:

    print("Você é adolescente.")

else:

    print("Você é criança.")
