class TADFracao:
    num = 1
    denominador = 1

    def _init_(self, num, denominador):
        self.num = num
        self.denominador = denominador

    def adicionar(self, fracao):
        num = (self.num * fracao.denominador) + (fracao.num *
                                                       self.denominador)
        deno = (self.denominador * fracao.denominador)
        return Fracao(num, deno)

    def sub(self, fracao):
        if (self.denominador
                == fracao.denominador) & (self.num != fracao.num):
            num = (self.num - fracao.num)
            denominador = (self.denominador)
        elif (self.denominador == fracao.denominador) & (self.num
                                                         == fracao.num):
            num = 0
            deno = 0
        else:
            num = (self.num * fracao.denominador) - (fracao.num *
                                                           self.denominador)
            deno = (self.denominador * fracao.denominador)
        return Fracao(num, deno)

    def multiplicar(self, fracao):
        num = (self.num * fracao.num)
        deno = (self.denominador * fracao.denominador)
        return Fracao(num, deno)

    def infinito():
        i = 0
        while True:
            yield i
            i += 1

    def simplificar(self):        
      loop = True
      j = 2
      
      while loop == True:               
        control = False
        if self.num / j == 1 or self.denominador / j == 1:
          loop = False
        
        if self.num % j == 0 and self.denominador % j == 0:       
          self.num = self.num / j
          self.denominador = self.denominador / j
          control = True
          
        else:          
          j += 1
          control = True

        if control == False:
          loop = False
          
          
      return fracao(self.num, self.denominador)

    def gcd(self):
        while self.denominador != 0:
            t = self.denominador
            self.denominador = self.num % self.denominador
            self.num = t
        return self.num

    def reduce(self):
        greatest = self.gcd(self)
        num = self.num / greatest
        deno = self.denominador / greatest
        return Fracao(num, deno)

    def resolver(self):
        return self.num / self.denominador

    def _str_(self):
        return f"{self.num}/{self.denominador}"


fracao1 = Fracao(24,60)
print(f"Simplificacao: {fracao1.simplificar()}")

fracao1 = Fracao(56,75)
print(f"Simplificacao: {fracao1.simplificar()}")

fracao1 = Fracao(8,20)
print(f"Simplificacao: {fracao1.simplificar()}")

fracao1 = Fracao(200,350)
print(f"Simplificacao: {fracao1.simplificar()}")