from node import Node

class ListaDin:
    home = None

    def _init_(self):
        self.home = None

    def adicionar(self, i):
        if (self.home == None):
            self.home = Node(i, None)

        else:
            aux = self.home
            while (aux.proximo != None):
                aux = aux.proximo

            aux.proximo = Node(i, None)

    def mostrar(self):
        aux = self.home
        print("[", end='')

        while (aux != None):
            print(f"{aux.valor}, ", end='')
            aux = aux.proximo

        print("]")

    def remover_apenas_um(self, i):
        aux = self.home   

        if aux == None:         
          return

        if aux != None:
          if aux.valor == i:
            self.home = self.proximo
            self = None
                    

        while aux != None:         
          if aux.i == i:           
            break
          prev = aux
          aux = aux.proximo

        prev.proximo = aux.proximo
        aux = None

    def remover_todos(self, i):
        aux = self.home

        while aux != None:
          self.remover_apenas_um(i)
          aux = aux.proximo