from cajero.Login import Login
from cajero.Operaciones import Operaciones

login = Login
access = login.logIn()
operaciones = Operaciones
if access == True:
    operaciones.mostrarOperaciones()

else:
    print("NIP Incorrecto")