
from models.Historico import Historico


class Cuenta:
    Nombre = "Cristobal Flores"
    saldo = 1000
    listHistorico : Historico = []

    def __str__(self) -> str:
        str_result = 'Historial de Movimientos'
        for his in self.listHistorico:
            str_result += "\n  * {}".format(his)
        return str_result
