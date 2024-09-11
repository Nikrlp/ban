_Autor_ ="nicolas ramos lopez"
_License_ ="GPL"
_Version_ ="1.0.0"
_Email_ ="nicolas.ramos@campusucc.edu.co"
#metodo profesor 
#importaciones
from cuentaAhorros import CuentaAhorro
from cuentaCorriente import cuentaCorriente
from CDT import CDT
        
class SimuladorBancario:
            #atrbutos
    __cedula='' #´por la ley la cedula debe ir asi ''
    __nombre=''
    __MesActual =0
    
    
    __cuentaCorriente= cuentaCorriente() #CON LAS DOS LINEAS QUE SE COLOCARON TRAS LA VARIABLE SE HIZO PRIVADA LA INFORMACION DEL LOS USUARIOS
    __CuentaAhorrosIngreso = CuentaAhorro()
    __cdtIngreso = CDT()
    #------------------------------------------------------------------------
    _method_="Consignar cuenta corriente"
    _params_="Monto"
    _returns_="Nada"
    _descriptions_='Este metodo consigna un monto a la cuenta corriente'
    def ConsignarCuentaCorriente(self,monto):
        #aqui inicia mi metodo
        self.__cuentaCorriente.ConsignarValor(monto)
    _method_="calcularSaldo Total"
    _params_="Ningunoo"
    _returns_="Saldo total"
    _descriptions_='Este parametro suma el saldo de todas las cuentas '
    
    def calcularSaldoTotal(self):
        #Aqui inicia mi metodo 
        #forma 1
        total = self.__cuentaCorriente.DarSaldo()+self.__CuentaAhorrosIngreso. AhorroTotal()+self.__cdtIngreso.SaldoTotalCDT()
        return total
    _method_="PasarAhorrosACorriente"
    _params_="Ninguno"
    _returns_="Ninguno"
    _descriptions_='Este metodo transfiere el saldo de ahorro a corriente '
    def PasarAhorrosACorriente(self):
        saldoTemporal = self.__cuentaahorros.DarSaldoA()
        self.__cuentaahorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.ConsignarValor(saldoTemporal)
    
    _method_="Ahorrar"
    _params_="Monto"
    _returns_="Ninguno"
    _descriptions_="Este metodo permite pasar el saldo de cuenta corriente a cuenta ahorros"
    def Ahorror(self,monto):
        #Aqui inicia mi codigo
        monto = self.__cuentaCorriente.DarSaldo()
        self.__cuentaCorriente.RetirarValor(monto)
        self.__CuentaAhorrosIngreso .Valornuevo (monto)
        
        
    _method_="retirarAhorro"
    _params_="Monto"
    _returns_="Ninguno"
    _descriptions_="Metodo que permite retirar un valor que dio la cuenta de ahorros"
    def retirarAhorro (self, monto):

        #Aqui inicia mi codigo
        self.__CuentaAhorrosIngreso . RetirarSaldo(monto)
        
    _method_="DarSaldoCorriente"
    _params_="Ninguno"
    _returns_="DarSaldo"
    _descriptions_="Metodo me permite retornar saldo que hay en cuenta corriente "

    def CalcularTodo(self):
        # Aqui inicia mi codigo
        return self.__cuentaCorriente.DarSaldo()
    
    _method_="RetirarTodo"
    _params_="Ninguno"
    _returns_="retirar saldo y valor"
    _descriptions_="Meto me permite retirar todo lo que hay en la cuenta corriente y de ahorros"

    def RetirarTodo(self):
        total = self.__cuentaCorriente.DarSaldo()+ self CuentaAhorro.DarSaldo()
        self.__CuentaAhorros.retirarValor(self.__CuentaAhorros.DarSaldo())
        self.__cuentaCorriente.RetirarValor(self.__cuentaCorriente.DarSaldo())
        return "usted acaba de retirar "+total

    _method_="DuplicarAhorro"
    _params_="Ninguno"
    _returns_="ninguno"
    _descriptions_="metodo me permite duplicar el dinero que hay en cuenta Ahorros"

    def DuplicarAhorro(self):
        self.__CuentaAhorro.consignarValor(self.__CuentaAhorro.DarSaldo)
        
        
        