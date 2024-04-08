from pessoa import Pessoa
from salario import Salario

nome = ("Eduardo")
idade = ("25")
cargo = ("Professor")
salario = float(input("Digite o salario: "))
if salario <= 2000:
    cargo = "Professor"
elif salario > 2000:
    cargo = "Diretor"

funcionario = Pessoa()
salario_funcionario = Salario()

print(funcionario.apresentar_nome(f"Nome = {nome}"))
print(funcionario.apresentar_idade(f"Idade = {idade}"))
print(funcionario.apresentar_cargo(f"Cargo = {cargo}"))
print(salario_funcionario.apresentar_salario(f"Salario = {salario} reais"))