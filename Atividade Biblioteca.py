# ======================================================================
# EXCEÇÕES PERSONALIZADAS
# ======================================================================
class BibliotecaError(Exception):
    """Exceção base para todos os erros do sistema."""
class LivroIndisponivelError(BibliotecaError):
    """Lançada ao tentar emprestar um livro que já está emprestado."""
class LimiteExcedidoError(BibliotecaError):
    """Lançada quando o usuário atinge o limite de empréstimos."""
class LivroNaoEmprestadoError(BibliotecaError):
    """Lançada ao devolver um livro que o usuário não possui."""
class RegistroNaoEncontradoError(BibliotecaError):
    """Lançada quando um livro ou usuário não é encontrado."""
class RegistroDuplicadoError(BibliotecaError):
    """Lançada ao cadastrar um livro/usuário que já existe."""

# ======================================================================
# CLASSE LIVRO
# ======================================================================

class Livro:
    """Representa um livro do acervo da biblioteca."""

    def __init__(self, titulo, autor, isbn):
        """Cria um livro, sempre inicialmente disponível."""
        if not titulo.strip() or not autor.strip() or not isbn.strip():
            raise ValueError("Título, autor e ISBN não podem ser vazios.")
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.isbn = isbn.strip()
        self.disponivel = True

    def emprestar(self):
        """Marca o livro como emprestado. Lança erro se já estiver emprestado."""
        if not self.disponivel:
            raise LivroIndisponivelError(
                f"O livro '{self.titulo}' já está emprestado."
            )
        self.disponivel = False

    def devolver(self):
        """Marca o livro como disponível novamente."""
        self.disponivel = True

    def descricao(self):
        """Retorna uma string com os dados e o status do livro."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.isbn}] '{self.titulo}' - {self.autor} ({status})"


# ======================================================================
# CLASSE USUARIO (SUPERCLASSE)
# ======================================================================
class Usuario:
    """Classe base para os usuários da biblioteca."""

    LIMITE_PADRAO = 3 # limite usado se a subclasse não definir outro

    def __init__(self, nome, matricula):
        """Cria um usuário com lista de livros emprestados vazia."""
        if not nome.strip() or not matricula.strip():
            raise ValueError("Nome e matrícula não podem ser vazios.")
        self.nome = nome.strip()
        self.matricula = matricula.strip()
        self.livros_emprestados = []

    property
    def limite(self):
        """Limite de livros que o usuário pode ter ao mesmo tempo."""
        return self.LIMITE_PADRAO

    property
    def tipo(self):
        """Nome do tipo de usuário (usado na exibição)."""
        return "Usuário"

    def pegar_livro(self, livro):
        """Empresta um livro ao usuário, respeitando o limite."""
        if len(self.livros_emprestados) >= self.limite:
            raise LimiteExcedidoError(
                f"{self.tipo} {self.nome} atingiu o limite de "
                f"{self.limite} livros."
            )
        livro.emprestar() # pode lançar LivroIndisponivelError
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        """Devolve um livro que está em posse do usuário."""
        if livro not in self.livros_emprestados:
            raise LivroNaoEmprestadoError(
                f"{self.nome} não está com o livro '{livro.titulo}'."
            )
        livro.devolver()
        self.livros_emprestados.remove(livro)

    def __str__(self):
        """Representação textual do usuário."""
        return (f"{self.tipo}: {self.nome} (Mat. {self.matricula}) - "
                f"{len(self.livros_emprestados)}/{self.limite} livros")


# ======================================================================
# SUBCLASSES
# ======================================================================
class Aluno(Usuario):
    """Aluno: pode ter no máximo 2 livros emprestados."""

    LIMITE_ALUNO = 2

    property
    def limite(self):
        """Sobrescreve o limite da superclasse."""
        return self.LIMITE_ALUNO

    property
    def tipo(self):
        return "Aluno"

    def pegar_livro(self, livro):
        """Sobrescreve pegar_livro com a regra específica do aluno."""
        if len(self.livros_emprestados) >= self.LIMITE_ALUNO:
            raise LimiteExcedidoError(
                f"Aluno {self.nome}: máximo de {self.LIMITE_ALUNO} livros."
            )
        super().pegar_livro(livro)


class Professor(Usuario):
    """Professor: pode ter no máximo 5 livros emprestados."""

    LIMITE_PROFESSOR = 5

    property
    def limite(self):
        """Sobrescreve o limite da superclasse."""
        return self.LIMITE_PROFESSOR

    property
    def tipo(self):
        return "Professor"

    def pegar_livro(self, livro):
        """Sobrescreve pegar_livro com a regra específica do professor."""
        if len(self.livros_emprestados) >= self.LIMITE_PROFESSOR:
            raise LimiteExcedidoError(
                f"Professor {self.nome}: máximo de {self.LIMITE_PROFESSOR} livros."
            )
        super().pegar_livro(livro)


# ======================================================================
# CLASSE BIBLIOTECA (GERENCIADORA)
# ======================================================================
class Biblioteca:
    """Gerencia o acervo de livros e os usuários cadastrados."""

    def __init__(self):
        """Inicia a biblioteca com acervo e usuários vazios."""
        self.livros = {} # chave: ISBN
        self.usuarios = {} # chave: matrícula

    def cadastrar_livro(self, livro):
        """Adiciona um livro ao acervo (ISBN único)."""
        if livro.isbn in self.livros:
            raise RegistroDuplicadoError(f"Já existe livro com ISBN {livro.isbn}.")
        self.livros[livro.isbn] = livro

    def cadastrar_usuario(self, usuario):
        """Cadastra um usuário (matrícula única)."""
        if usuario.matricula in self.usuarios:
            raise RegistroDuplicadoError(
                f"Já existe usuário com matrícula {usuario.matricula}."
            )
        self.usuarios[usuario.matricula] = usuario

    def buscar_livro(self, isbn):
        """Retorna o livro pelo ISBN ou lança erro se não existir."""
        if isbn not in self.livros:
            raise RegistroNaoEncontradoError(f"Livro com ISBN {isbn} não encontrado.")
        return self.livros[isbn]

    def buscar_usuario(self, matricula):
        """Retorna o usuário pela matrícula ou lança erro se não existir."""
        if matricula not in self.usuarios:
            raise RegistroNaoEncontradoError(
                f"Usuário com matrícula {matricula} não encontrado."
            )
        return self.usuarios[matricula]

    def emprestar(self, matricula, isbn):
        """Realiza o empréstimo de um livro a um usuário."""
        usuario = self.buscar_usuario(matricula)
        livro = self.buscar_livro(isbn)
        usuario.pegar_livro(livro)
        return usuario, livro

    def devolver(self, matricula, isbn):
        """Realiza a devolução de um livro por um usuário."""
        usuario = self.buscar_usuario(matricula)
        livro = self.buscar_livro(isbn)
        usuario.devolver_livro(livro)
        return usuario, livro


# ======================================================================
# MENU INTERATIVO
# ======================================================================
def ler_opcao(mensagem, validas):
    """Lê uma opção do teclado e repete até ser válida."""
    while True:
        opcao = input(mensagem).strip()
        if opcao in validas:
            return opcao
        print("Opção inválida. Tente novamente.")


def cadastrar_livro_menu(biblioteca):
    """Pede os dados no terminal e cadastra um livro."""
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    biblioteca.cadastrar_livro(Livro(titulo, autor, isbn))
    print("Livro cadastrado com sucesso!")


def cadastrar_usuario_menu(biblioteca):
    """Pede os dados no terminal e cadastra um aluno ou professor."""
    tipo = ler_opcao("Tipo (1-Aluno, 2-Professor): ", {"1", "2"})
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    classe = Aluno if tipo == "1" else Professor
    biblioteca.cadastrar_usuario(classe(nome, matricula))
    print("Usuário cadastrado com sucesso!")


def listar_livros_menu(biblioteca):
    """Mostra todos os livros do acervo."""
    if not biblioteca.livros:
        print("Nenhum livro cadastrado.")
    for livro in biblioteca.livros.values():
        print(livro.descricao())


def listar_usuarios_menu(biblioteca):
    """Mostra todos os usuários e seus empréstimos."""
    if not biblioteca.usuarios:
        print("Nenhum usuário cadastrado.")
    for usuario in biblioteca.usuarios.values():
        print(usuario)
        for livro in usuario.livros_emprestados:
            print(f" - {livro.titulo}")


def emprestar_menu(biblioteca):
    """Pede matrícula e ISBN e realiza o empréstimo."""
    matricula = input("Matrícula do usuário: ").strip()
    isbn = input("ISBN do livro: ").strip()
    usuario, livro = biblioteca.emprestar(matricula, isbn)
    print(f"{usuario.nome} pegou '{livro.titulo}' emprestado.")


def devolver_menu(biblioteca):
    """Pede matrícula e ISBN e realiza a devolução."""
    matricula = input("Matrícula do usuário: ").strip()
    isbn = input("ISBN do livro: ").strip()
    usuario, livro = biblioteca.devolver(matricula, isbn)
    print(f"{usuario.nome} devolveu '{livro.titulo}'.")


def exibir_menu():
    """Imprime as opções do menu principal."""
    print("\n===== BIBLIOTECA SENAI =====")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuário")
    print("3 - Listar livros")
    print("4 - Listar usuários")
    print("5 - Emprestar livro")
    print("6 - Devolver livro")
    print("0 - Sair")


def main():
    """Laço principal: exibe o menu e trata os erros de cada operação."""
    biblioteca = Biblioteca()

    # Dados iniciais para facilitar os testes
    biblioteca.cadastrar_livro(Livro("Dom Casmurro", "Machado de Assis", "111"))
    biblioteca.cadastrar_livro(Livro("O Cortiço", "Aluísio Azevedo", "222"))
    biblioteca.cadastrar_livro(Livro("Iracema", "José de Alencar", "333"))
    biblioteca.cadastrar_usuario(Aluno("Ana", "A001"))
    biblioteca.cadastrar_usuario(Professor("Carlos", "P001"))

    acoes = {
        "1": cadastrar_livro_menu,
        "2": cadastrar_usuario_menu,
        "3": listar_livros_menu,
        "4": listar_usuarios_menu,
        "5": emprestar_menu,
        "6": devolver_menu,
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break

        acao = acoes.get(opcao)
        if acao is None:
            print("Opção inválida.")
            continue

        try:
            acao(biblioteca)
        except BibliotecaError as erro: # erros das regras de negócio
            print(f"Erro: {erro}")
        except ValueError as erro: # dados de entrada inválidos
            print(f"Dados inválidos: {erro}")
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada.")
        except Exception as erro: # qualquer erro inesperado
            print(f"Erro inesperado: {erro}")


if __name__ == "__main__":
    main()