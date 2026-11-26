class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True


    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False


    def devolver(self):
        self.disponivel = True


    def descricao(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}) - {status}"


class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.limite = 3
        self.livros_emprestados = []


    def pegar_livro(self, livro):
        if len(self.livros_emprestados) >= self.limite:
            print(f"{self.nome}: limite de {self.limite} livros atingido.")
            return False
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print(f"{self.nome} pegou {livro.titulo}.")
            return True
        print(f"{self.nome}: '{livro.titulo}' não está disponível.")
        return False


    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu {livro.titulo}.")


class Aluno(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 2


    def pegar_livro(self, livro):
        if len(self.livros_emprestados) >= 2:
            print(f"Aluno {self.nome}: máximo de 2 livros.")
            return False
        return super().pegar_livro(livro)


class Professor(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 5


    def pegar_livro(self, livro):
        if len(self.livros_emprestados) >= 5:
            print(f"Professor {self.nome}: máximo de 5 livros.")
            return False
        return super().pegar_livro(livro)

if __name__ == "__main__":
    livros = [
        Livro("Dom Casmurro", "Machado de Assis", "111"),
        Livro("O Cortiço", "Aluísio Azevedo", "222"),
        Livro("Iracema", "José de Alencar", "333"),
        Livro("Vidas Secas", "Graciliano Ramos", "444"),
        Livro("A Moreninha", "Joaquim Manuel de Macedo", "555"),
        Livro("Memórias Póstumas", "Machado de Assis", "666"),
    ]


    aluno = Aluno("Ana", "A001")
    prof = Professor("Carlos", "P001")


    print("--- Aluno (limite 2) ---")
    for l in livros[:3]:
        aluno.pegar_livro(l)


    print("\n--- Professor (limite 5) ---")
    for l in livros[2:]:
        prof.pegar_livro(l)


    print("\n--- Descrição dos livros ---")
    for l in livros:
        print(l.descricao())


    print("\n--- Devolução ---")
    aluno.devolver_livro(livros[0])
    print(livros[0].descricao())