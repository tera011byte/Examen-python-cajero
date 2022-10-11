from datetime import datetime
from models.Cuenta import Cuenta
from models.Historico import Historico

class Operaciones:
    global cuenta
    cuenta = Cuenta


    def mostrarOperaciones():
        print(f""" Bienvenido {cuenta.Nombre} """)
        
        print(f""" 1.- Consultar Saldo """)
        print(f""" 2.- Retirar Saldo """)
        print(f""" 3.- Historico de movimientos """)
        print(f""" 4.- Salir """)
        opcion = 0
        while opcion != 4:
            print(f""" Opcion: {opcion} """)
            try:
                opcion = int(input(f"""Elige una opcion """))
            except ValueError:
                print("Opcion no valida")
            if opcion == 1:
                Operaciones.consultarSaldo()
                break
            elif opcion == 2:
                Operaciones.retirarSaldo()
                break
            elif opcion == 3:
                Operaciones.mostrarHisotrico()
                break
            elif opcion == 4:
                print("Opcion 4")
                break

    def subMenu():
        print(f""" 1.- Menu Principal """)
        print(f""" 2.- Salir """)
        opcionSub = 0
        while True:
            try:
                opcionSub = int(input(f"""Elige una opcion """))
            except ValueError:
                print("Opcion no valida")
            if opcionSub == 1:
                Operaciones.mostrarOperaciones()
                break
            elif opcionSub == 2:
                print("Opcion 2")
                break

    def consultarSaldo():
        print(f""" Tu Saldo Actual es de ${cuenta.saldo} """)
        Operaciones.subMenu()

    def retirarSaldo(): 
        print(f""" Tu Saldo Actual es de ${cuenta.saldo} """)
        monto = 0
        try:
            monto = int(input(f"""Monto a Retirar:  """))
        except ValueError:
            print("Opcion no valida")
        if monto > cuenta.saldo:
            print(f""" Saldo Insuficiente """)
            Operaciones.subMenu()
        else:
            Operaciones.transaccionSaldo(monto)
            Operaciones.subMenu()

    def transaccionSaldo(monto):
        histori = Historico()
        histori.saldoAnterior = cuenta.saldo
        cuenta.saldo = cuenta.saldo - monto
        histori.saldoActual = cuenta.saldo
        histori.montoRetirado = monto
        histori.fecha = datetime.now()
        cuenta.listHistorico.append(histori)

    def mostrarHisotrico():
        print(len(cuenta.listHistorico))
        if len(cuenta.listHistorico) == 0:
            print("No se han realizado movimientos")
            Operaciones.subMenu()
        else:
            his = Historico
            for his in cuenta.listHistorico:
                print(f"{his}")
            Operaciones.subMenu()
        