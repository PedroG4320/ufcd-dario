OPC = 0
saida = True

while True:
    print("1 - Bom dia")
    print("1 - Bom tarde")
    print("1 - Boa noite")
    print("4 - sair")
    OCP = int (input("Intrud a opcão"))

    match OPC :
        case 1:
            print("Bom dia")
        case 2:
            print("Boa tarde")
        case 3:
            print("Boa noite")
        case 4:
            print("Adeus")  
            break  
        
