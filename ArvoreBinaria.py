# Arthur Ferreira da Silva Mateus
# Lucas Gazoni Araújo 
# Sérgio Murilo Moreira Morais
# Henrique Weirich Meurer siegel
class Node():
    def __init__(self, palavra):
        self.palavra = palavra
        self.contagem = 1
        self.esquerda = None
        self.direita = None

class ArvoreBinaria():
    def __init__(self):
        self.raiz = None
    
    def inserir(self, palavra):
        if self.raiz is None:
            self.raiz = Node(palavra)
        else:
            self._inserir(self.raiz, palavra)
    
    def _inserir(self, no, palavra):
        if palavra == no.palavra:
            no.contagem += 1
        elif palavra < no.palavra:
            if no.esquerda is None:
                no.esquerda = Node(palavra)
            else:
                self._inserir(no.esquerda, palavra)
        else:
            if no.direita is None:
                no.direita = Node(palavra)
            else:
                self._inserir(no.direita, palavra)
                
    def em_ordem(self):
        self._em_ordem(self.raiz)
        
    def _em_ordem(self, no):
        if no is not None:
            self._em_ordem(no.esquerda)
            print(f'{no.palavra} ({no.contagem})')
            self._em_ordem(no.direita)

def processaPalavras(strings):
    arvore = ArvoreBinaria()
    for palavra in strings:
        if palavra:
            arvore.inserir(palavra)
    arvore.em_ordem()

def main():
    palavras = []
    while True:
        string = str(input('Digite uma palavra com até 15 letras: '))
        if len(string) > 15:
            print("A palavra deve ter no máximo 15 letras. Tente novamente.")
            continue
        palavras.append(string)
        continuar = input("Deseja continuar? (s/n) ").lower()
        if continuar != 's':
            break
    processaPalavras(palavras)
    
if __name__ == "__main__":
    main()
