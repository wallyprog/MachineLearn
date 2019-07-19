class Robos:
    mensagem_erro = 'Valor não pode ser aplicado'
    
    def move_up(self):
        if ( self.y < 10):
            self.y += 1
        else:
            print (self.mensagem_erro)
    
    def move_down(self):
        if ( self.y > 0):
            self.y -= 1
        else:
            print (self.mensagem_erro)

    def move_right(self):
        if ( self.x < 10):
            self.x += 1
        else:
            print (self.mensagem_erro)

    def move_left(self):
        if ( self.x > 0):
            self.y -= 1
        else:
            print (self.mensagem_erro)
    

    
