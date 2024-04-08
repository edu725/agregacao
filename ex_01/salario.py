class Salario:
    def __init__(self) :
        self.__salario_funcionario = float
    
    @property
    def salario_funcionario(self)-> float:
        return self.__salario_funcionario
    
    @salario_funcionario.setter
    def salario_funcionario(self,salario) -> int:
        self.__salario_funcionario = salario

    def apresentar_salario(self,salario):
        self.__salario_funcionario == salario
        return salario 
    
    