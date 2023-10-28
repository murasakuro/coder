# Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100

# number=0
# sumation=0

# while number<100:
#     number+=1
#     if (number%2)!=0: sumation+=number

sumation=0
# for digit in range(100):
#     if (digit%2)!=0: sumation+=digit

# for digit in range(1,100,2):
#     sumation+=digit
    
sumation=sum(range(1,100,2))

print("El resultado es:", sumation)