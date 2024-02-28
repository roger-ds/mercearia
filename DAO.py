from models import *


class DaoCategoria:


    @classmethod
    def salvar(cls, categoria):
        with open("categoria.txt", "a") as arq:
            arq.writelines(categoria)
            arq.writelines("\n")


    @classmethod
    def ler(cls):
        with open("categoria.txt", "r") as arq:
            cls.categoria = arq.readlines()
        cls.categoria =list(map(lambda x: x.strip(), cls.categoria))
        print(cls.categoria)
        cat = [
            Categoria(i)
            for i in cls.categoria
        ]
        return cat


    # DaoCategoria.salvar("Frutas")
    # DaoCategoria.salvar("Verduras")
    # DaoCategoria.salvar("Legumes")
    # DaoCategoria.ler()


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open("venda.txt", "a") as arq:
            arq.writelines(venda.itens_vendidos.nome + "|" +
                          venda.itens_vendidos.preco + "|" +
                          venda.itens_vendidos.categoria + "|" +
                          venda.vendedor + "|" +
                          venda.comprador + "|" +
                          str(venda.quantidade_vendida) + "|" +
                          venda.data)
            arq.writelines("\n")


    @classmethod
    def ler(cls):
        with open("venda.txt", "r") as arq:
            cls.venda = arq.readlines()
        cls.venda = list(map(lambda x: x.strip().split("|"), cls.venda)) 
        vend = [
            Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6])
            for i in cls.venda
        ]
        print(vend[0].itens_vendidos.nome,
              vend[1].data)
        return vend

        
    # p = Produtos("banana", "5", "frutas")
    # p = Produtos("maca", "7", "frutas")
    # v = Venda(p, "joao", "maria", "5")
    # DaoVenda.salvar(v)
    # DaoVenda.ler()


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open("estoque.txt", "a") as arq:
            arq.writelines(produto.nome + "|" +
                           produto.preco + "|" +
                           produto.categoria + "|" +
                           str(quantidade))
            arq.writelines("\n")


    @staticmethod
    def ler():
        with open("estoque.txt", "r") as arq:
            estoque = arq.readlines()
        estoque = list(map(lambda x: x.strip().split("|"), estoque))
        print(estoque)
        return [
            Estoque(Produtos(i[0], i[1], i[2]), i[3])
            for i in estoque
        ]


    # p = Produtos("Uva", "3", "Frutas")
    # p = Produtos("Melancia", "1", "Frutas")

    # DaoEstoque.salvar(p, "235")
    # DaoEstoque.ler()


class DaoFornecedores:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open("fornecedores.txt", "a") as arq:
            arq.writelines(fornecedor.nome + "|" +
                           fornecedor.cnpj + "|" + 
                           fornecedor.telefone + "|" +
                           fornecedor.categoria)
            arq.writelines("\n")


    @classmethod
    def ler(cls):
        with open("fornecedores.txt", "r") as arq:
            cls.fornecedor = arq.readlines()
        cls.fornecedor = list(map(lambda x: x.strip().split("|"), cls.fornecedor))
        print(cls.fornecedor)
        return [
            Fornecedor(i[0], i[1], i[2], i[3])
            for i in cls.fornecedor
        ]


    # f = Fornecedor("Paulo", "123.234/0001-07", "98191-2120","Limpeza")
    # f = Fornecedor("Gean", "457.879/0001-01", "93137-8675","Laticinios")
    # DaoFornecedores.salvar(f)
    # DaoFornecedores.ler()


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoa.txt", "a") as arq:
            arq.writelines(pessoa.nome + "|" + 
                           pessoa.telefone + "|" +
                           pessoa.cpf + "|" +
                           pessoa.email + "|" +
                           pessoa.endereco)
            arq.writelines("\n")


    @classmethod
    def ler(cls):
        with open("pessoa.txt", "r") as arq:
            cls.pessoa = arq.readlines()
        cls.pessoa = list(map(lambda x: x.strip().split("|"), cls.pessoa))
        print(cls.pessoa)
        return[
            Pessoa(i[0], i[1], i[2], i[3], i[4])
            for i in cls.pessoa
        ]
    

    # p = Pessoa("Helena", "12345-0987", "324.678/0001-99", "helena@gmail.com", "Rua das flores n. 0")
    # DaoPessoa.salvar(p)
    # DaoPessoa.ler()



class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open("funcionarios.txt", "a") as arq:
            arq.writelines(funcionario.clt  + "|" +
                           funcionario.nome + "|" + 
                           funcionario.telefone + "|" +
                           funcionario.cpf + "|" +
                           funcionario.email + "|" +
                           funcionario.endereco)
            arq.writelines("\n")


    @classmethod
    def ler(cls):
        with open("funcionarios.txt", "r") as arq:
            cls.funcionario = arq.readlines()
        cls.funcionario = list(map(lambda x: x.strip().split("|"), cls.funcionario))
        print(cls.funcionario)
        return[
            Funcionario(i[0], i[1], i[2], i[3], i[4], i[5])
            for i in cls.funcionario
        ]
    

    # f = Funcionario("12334590909090", "Helena", "12345-0987", "324.678/0001-99", "helena@gmail.com", "Rua das flores n. 0")
    # DaoFuncionario.salvar(f)
    # DaoFuncionario.ler()