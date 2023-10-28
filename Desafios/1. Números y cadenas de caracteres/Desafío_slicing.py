# Dadas cuatro variables con diferentes textos (de forma individual), genera una nueva variable con el siguiente contenido:

# Objetivo: “Python es un lenguaje de programación versátil”

# Partiendo de:

# cadena_1 = “versátil”

# cadena_2 = “Python”

# cadena_3 = “es un lenguaje”

# cadena_4 = “de programación”
chain1="versatil"
chain2="Python"
chain3="es un lenguaje"
chain4="de programación"
fullChain=f"{chain2} {chain3} {chain4} {chain1}"
print(fullChain)
fullChain=chain2+" "+chain3+" "+chain4+" "+chain1
print(fullChain)