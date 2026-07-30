#classe base que representa qualquer pessoa na empresa
class empresa:
    def __init__(self,nome="",funcao="",departamento="",salario=""):
        # atributos comuns a todos os cargos
         self.nome = nome
         self.funcao = funcao
         self.departamento = departamento
         self.salario = salario


#subclasse que representa o CEO da empresa
class ceo_empresa(empresa):
     def __init__(self):
         #inicializar com os dados especificos da subclasse CEO
         super().__init__(
             nome="henrique gonçalves",
             funcao="supervisiona as operações diárias e contrata funcionários",
             departamento="diretoria executiva",
             salario="R$45.000"
         )

     def __str__(self):
         #retorna uma descriçao formatada do CEO
         return (f"CEO: {self.nome}\n"
                 f"funcao: {self.funcao}\n"
                 f"departamento: {self.departamento}\n"
                 f"salario: {self.salario}")

#subclasse que representar o VICE_CEO
class vice_ceo(empresa):
    def __init__(self):
        #inicializar com os dados especificos da subclasse VICE_CEO
        super().__init__(
            nome="joao jose",
            funcao="Trabalha diretamente com o CEO na definição e execução das estratégias corporativas.",
            departamento="diretoria executiva",
            salario="R$35.000"
        )

    def __str__(self):
        #retorna uma descriçao formatada do VICE_CEO
        return (f"VICE_ceo: {self.nome}\n"
                f"funcao: {self.funcao}\n"
                f"departamento: {self.departamento}\n"
                f"salario: {self.salario}")

#subclasse  que representar o GERENTE_EMPRESA
class gerente_empresa(empresa):
    def __init__(self):
        #inicializar com os dados especificos subclasse GERENTE_EMPRESA
        super().__init__(
            nome="bernardo santos",
            funcao="cuidando de equipes e tarefas dentro de cada departamento",
            departamento="Departamento de vendas ",
            salario="R$20.000"
        )

    def __str__(self):
        #retorna uma descriçao formatada do GERENTE_EMPRESA
        return (f"GERENTE: {self.nome}\n"
                f"funcao: {self.funcao}\n"
                f"departamento: {self.departamento}\n"
                f"salario: {self.salario}")

#subclasse que representar o FUNCIONARIO
class funcionario(empresa):
    def __init__(self):
        #inicializar com os dados especificos subclasse FUNCIONARIO
        super().__init__(
            nome="ailton jose",
            funcao="Usinador ",
            departamento="responsável por transformar o ferro em peças específicas para máquinas.",
            salario="R$7.500"
        )

    def __str__(self):
        #retorna uma descriçao formatada da subclasse funcionario
        return (f"funcionario: {self.nome}\n"
                f"funcao: {self.funcao}\n"
                f"departamento: {self.departamento}\n"
                f"salario: {self.salario}")

#impriminto a subclasse CEO
print(ceo_empresa())
print()

#impriminto a subclasse VICE_ceo
print(vice_ceo())
print()

#impriminto a subclasse GERENTE_empresa
print(gerente_empresa())
print()

#imprimnto a subclasse funcionario
print(funcionario())