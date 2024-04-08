class Pessoa:
    def __init__(self):
        self.__funcionario = str
        self.__idade_funcionario = int
        self.__cargo_funcionario = str
        self.__salario_funcionario = float

    @property
    def funcionario(self)->str:
        return self.__funcionario
    
    @funcionario.setter
    def funcionario(self,nome):
        self.__funcionario = nome

    @property
    def idade_funcionario(self)-> int:
        return  self.__idade_funcionario
    
    @idade_funcionario.setter
    def idade_funcionario(self,idade):
        self.__idade_funcionario = idade 

    @property
    def salario_funcionario(self)-> float:
        return self.__salario_funcionario
    
    @salario_funcionario.setter
    def salario_funcionario(self,salario) -> int:
        self.__salario_funcionario = salario 

    @property
    def cargo_funcionario(self) :
        return self.__cargo_funcionario
    
    @cargo_funcionario.setter
    def cargo_funcionario(self,cargo)-> str:
        self.__cargo_funcionario = cargo

    def apresentar_nome(self, nome):
        self.funcionario == nome
        return nome

    def apresentar_idade(self,idade):
        self.idade_funcionario == idade
        return idade 

    def apresentar_cargo(self,cargo):
        self.cargo_funcionario == cargo
        return cargo  
    