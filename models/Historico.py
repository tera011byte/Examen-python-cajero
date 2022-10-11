from datetime import date


class Historico:
    saldoAnterior : int
    saldoActual : int 
    montoRetirado : int
    fecha: date

    def __repr__(self):  
        return "Test a:% s b:% s" % (self.montoRetirado, self.saldoActual)

    def __str__(self) -> str:
        str_result = f""" Fecha: {self.fecha}, Saldo Anterior: {self.saldoAnterior}, Saldo Actual: {self.saldoActual}, Monto Retirado: {self.montoRetirado}"""
        return str_result