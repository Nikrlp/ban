_Autor_ ="nicolas ramos lopez"
_License_ ="GPL"
_Version_ ="1.0.0"
_Email_ ="nicolas.ramos@campusucc.edu.co"

from cuentaCorriente import AhorroYcorriente #"Lo que primero se hace es llamar a la cuenta corrientepara asi poder llamar a los datos que estan en la otra cuenta

class CuentaAhorro:   #ahora definimos una clase para poner los datos de la cuenta de ahorros y asi poder pasar a las otras cuentas los datos
    # Aqui inicia la declaracion de mi clase
    
    #PRIMERO SE EMPESARIA A DEFINIR LAS VARIABLES O ATRIVUTOS QUE CREO SON LOS MISMOS
    '''#
    ATRIVUTOS
    #'''
    
    __saldoAhorro =0
    __Interes = 0.006 #lo que se esta haciendo es colocar el interes que cobra el ahorro
    
    # Aqui incia mis metodos que voy a usar para la solucion
    '''#
    metodos
    #'''
    
    _method_="ValorNuevo"
    _params_="valor_nuevo"
    _returns_="nada"
    _descriptions_='metodo suma al valor incial nuevo saldo' #este metodo nos ayuda a consignar un nuevo valor al valor inicial 
    def Valornuevo(self,nuevoInteres):                       #lo que nos quiere decir que aqui se ara la suma de los nuevos datos 
        self.__saldoAhorro=self.__saldoAhorro + nuevoInteres       #que se calcularan de mes en mes con un interes del 0.006 para darnos un nuevo dato de un nuevo mes
    
    
    _method_="DarSaldoAhorro"
    _params_="ninguno"                                              
    _returns_="saldo"                                        # En esta parte el codigo nos indica en el saldo en cuenate de ahorros  
    _descriptions_="metodo muestra el saldo en la cuenta"
    def DarSaldoAhorro (self):
        #Aqui va el codigo
        return self.__saldoAhorro 
    
    _method_="RetirarSaldo"
    _parameter_="monto"
    _returns_="ninguno"                                   #con este codigo es posible retirar el saldo de la cuenta de ahorros
    _descriptions_="metodo me permite retirar el saldo"
    def RetirarSaldo(self, monto):
        # Aqui va mi codigo
        self.__saldoAhorro =self.__saldoAhorro-monto
        
    
    _method_="InteresMensual"
    _parameter_="ninguno"
    _returns_="interes"
    _descriptions_=" metodo  muestra el interes "      #con este metodo lo que hacemos es calcular el interes por el sado inicial dependiendo de
    def InteresMensual (self):                                     #de los meses
        # Aqui comiesa mi metodo
        return self.__interes*self.__saldoAhorro
    
    _method_="Dar_saldo_total_mes"
    _parameter_="ninguno"                    #Lo que estamos haciendo aqui es sumar el interes con el saldo 
    _returns_="interes"
    _descriptions_="metodo calcula el interes del la cuenta"
    def Dar_saldo_total_mes (self):
        #aqui esta mi codigo
        return self.InteresMensual() +self._saldoAhorro
    
    _method_="AhorroTotal"
    _parameter_="ninguno"
    _returns_ ="interes"
    _parameter_="Metodo que calcula el total del saldo"
    
    def AhorroTotal (self):
        #aqui esta mi codigo
        return self.Dar_saldo_total_mes() + self.__saldoAhorro
    
    _method_="Ver_saldo_por_Mes"
    _parameter_="Ninguo" 
    _returns_="saldo"
    _descriptions_="metodo me indica el saldo mes por mes"
    def Ver_saldo_por_mes(self):
        #Aqui esta mi saldo
        return self.__Interes()+self.__saldoAhorro
        