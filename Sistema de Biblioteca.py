class livro: 
    def __int__ (self, titulo, autor, isbn): 
        self.titulo = titulo 
        self.autor =  autor
        self.isbn = isbn 
        self.disponivel = True

    def emprestar (self):
        if self .disponivel:
            self.disponivel = False
            return True
        return False
    
    def devolver (self):
        self. disponivel: True

    def descricao (self):
        status = "disponível" if self.disponivel else "Emprestado"
        return f"' {self.titulo}' de '{self.autor}' (ISBN: {self.isbn}) - {status}"

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