



num1 = int (input("intrud 1 numero"))
num2 = int (input("intrud 2 numero"))
num3 = int (input("intrud 3 numero"))

num_maior = num1
num_menor = num1
if num2 > num_maior:
    num_maior = num2
if num3 > num_maior:
    num_maior = num3
if num2 < num_menor:
    num_menor = num2
if num3 < num_menor:
    num_menor = num3
print(f"numero maior: {num_maior} & numero menor ")
    