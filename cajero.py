# manejo de cajero
datos={"clave":"1234","cbu":"0110253654125412367346","ayn":"Virili Omar Dario","saldo":25000,"saldoDolar":500,"plazofijo":[{"f_ini":"22-10-2022","f_fin":"22-11-2022","monto":30000},{"f_ini":"22-10-2023","f_fin":"22-11-2023","monto":50000}]}
movimientos =list()
listadoServicio = {"LUZ":(500,False)},{"AGUA":(500,False)},{"TELEFONO":(500,False)}
dolar = 215
def servicio():
    #tabajando en estas funcionalidades
    print("-------------MENU DE SERVICIOS------------")
    print("""
    1-NUEVO SERVICIO
    2-PAGAR SERVICIO
    3-ELIMNAR SERVICIO
    4-LISTAR SERVICIOS
    9-SALIR SIN CAMBIOS
    """)
    op = int(input("Ingrese opcion elegida: "))
    if op==1:
        nuevoSer=input("Ingrese nombre del Servicio")
        valor =int(input("Ingrese el monto del servicio"))
        nuevo = dict()
        nuevo[nuevoSer]=(valor,False)
        listadoServicio.append(nuevo)
        print(f"Servicio {nuevoSer} se agrego con Exito")
    elif op==2:
        pass
    elif op==3:
        pass
    elif op==4:
        pass
    elif op==9:
        print("No se realizaron cambios")
        salir = False

def menu():
    print(
        """
        MENU DE OPCIONES DEL CAJERO
        # 01-CONSULTA SALDO
        # 02-DEPOSITAR DINERO
        # 03-EXTRAER DINERO
        # 04-TRANSFERIR DINERO
        # 05-COMPRAR DOLARES
        # 06-VENDER DOLARES
        # 07-CREAR PLAZO FIJO
        # 08-ULTIMOS MOVIMIENTOS
        # 09-PAGAR SERVICIOS
        # 10-SALIR
        """
    )
    fin=True
    op=int(input("Ingrese una opcion: "))
    if op==1:
        print("------------------SALDO--------------------")
        print(f"Su saldo en Pesos es: {datos['saldo']}")
        print(f"Su saldo en Dolares: {datos['saldoDolar']}")
        total=0
        for x in datos['plazofijo']:
            total = total+x['monto']
            print(f"Plazo Fijo con Vencimiento el: {x['f_fin']} es: ${x['monto']}")
        print(f"El Saldo total acumulado en Plazo Fijos es: {total}")
        print("////////////////////////////////////////")
        movimientos.append("Consulta de Saldo")
    if op==2:
        print("--------------DEPOSITAR DINERO------------")
        caja = int(input(
                """Seleccione la cuenta a la cual depositara
                1-Pesos
                2-Dolares\n"""))
        if caja ==1:
            monto=int(input("Ingrese la cantidad de Pesos: $"))
            datos['saldo']=datos['saldo']+monto
            print(f"Su saldo en Pesos es: {datos['saldo']}")
            movimientos.append("Deposito de Pesos")
        elif caja ==2:
            monto=int(input("Ingrese la cantidad de Dolares: "))
            datos['saldo']=datos['saldoDolar']+monto
            print(f"Su saldo en Dolares es: {datos['saldoDolar']}")
            movimientos.append("Deposito de Dolare")
            
        
          
    if op==3:
        print("--------------EXTRACCION DINERO------------")
        print(f"Su saldo en Pesos es: {datos['saldo']}")
        monto = int(input("Ingrese el monto que desea extraer: $"))
        if(datos['saldo']>= monto):
            datos['saldo']=datos['saldo']-monto
            print(f"Su saldo en Pesos luego de la extraccion es : {datos['saldo']}")
            movimientos.append("Extraccion de Pesos")

    if op==4:
        print("--------------REALIZAR TRANSFERENCIA------------")
        divisa = int(input("Ingrese la divisa que transfiere 1-Pesos 2-Dolar: "))
        if divisa==1:
            cuenta=input("Ingrese el cbu de destino: ")
            
            if len(cuenta)==22:
                monto = int(input("Ingrese el monto a trasferir: "))
                if(datos['saldo']>= monto):
                    print(f"Transferencia de cbu origen: {datos['cbu']}\n a cbu destino: {cuenta}")
                    print(f"Por un monto de: {monto}")
                    print(f"Operación EXITOSA")
                    datos['saldo']=datos['saldo']-monto
                    movimientos.append("Transferencia de pesos a otra cuenta")
                else:
                    print("SALDO INSUFICIENTE para realizar la operación")
            else:
                print("Numero de cuenta incorrecta")

        elif divisa==2:
           
            cuenta=input("Ingrese el cbu de destino: ")
            if len(cuenta)==22:
                monto = int(input("Ingrese el monto a trasferir: "))
                if(datos['saldoDolar']>= monto):
                    print(f"Transferencia de cbu origen: {datos['cbu']}\n a cbu destino: {cuenta}")
                    print(f"Por un monto de: {monto}")
                    print(f"Operación EXITOSA")
                    datos['saldoDolar']=datos['saldoDolar']-monto
                    movimientos.append("Transferencia de dolares a cuenta de tercero")
                else:
                    print("SALDO INSUFICIENTE para realizar la operación")
            else:
                print("Numero de cuenta incorrecta")

        else:
            print("Opcioón no valida")
    if op==5:
        print("---------------COMPRA DE DOLARES-----------")
        print(f"Cotizacion del Dolar hoy: {dolar}")
        monto = int(input("Ingrese la cantidad de dolares que quiere comprar: "))
        if(datos['saldo']>= monto * dolar):
            datos['saldoDolar']+= monto
            datos['saldo']-=(monto * dolar)
            print("La Operación se completo con EXITO")
            movimientos.append("Compra de dolares")
        else:
            print("Los fondos no son suficiente")
    if op==6:
        print("---------------VENTA DE DOLARES-----------")
        print(f"Cotizacion del Dolar hoy: {dolar}")
        print(f"Su saldo en dolares actual es: {datos['saldoDolar']}")
        monto = int(input("Ingrese la cantidad de dolares que quiere vender: "))
        if(datos['saldoDolar']>= monto):
            datos['saldoDolar']-= monto
            datos['saldo']+=(monto * dolar)
            print("La Operación se completo con EXITO")
            movimientos.append("Venta de dolares")
        else:
            print("Los fondos no son suficiente")
    if op==7:
        print("------------CONSTITUIR PLAZO FIJO-----------")
        print("Constitucion de Plazo fijo")
        pf = {}
        pf['f_ini']="25-01-2023"
        pf['f_fin']="25-02-2023"
        pf['monto'] = int(input("Ingrese el monto destinado para el PF: $"))
        datos['plazofijo'].append(pf)
        print("Su plazo fijo fue conformado correctamente")
        movimientos.append("Constitucion de plazo fijo")
        # print(f"Su saldo en Plazo Fijo: {datos['plazofijo']['monto']}")
        print("////////////////////////////////////////")
    if op==8:
        print("------------ULTIMOS MOVIMIENTOS-----------")
        for x in movimientos:
            print(f"{x}")
    if op==9:
        servicio()
    if op==10:
        fin=False
    return fin

def cajero():
    flag= True
    print("*********************")
    if(input("Ingrese Clave: "))== datos["clave"]:
        while flag:
            flag=menu()

cajero()
