import numpy as np
class Colas:
    def __init__(self,n):
        
        self.lcola=[]
        print('se a creado una cola')
        self.size=n
    def add(self,lcola):
        if self.size<= len(self.lcola):
            print('la cola esta llena ')
        else:
            self.lcola.append(lcola)
            print('se agrego dato', lcola, 'a la cola')
    
    def get(self):
        if  len(self.lcola)<=0:
            print('la cola ya esta vacia')
            
           
            
        else:
            print('se elimino', self.lcola.pop(0))
    def is_empty(self):
        if len(self.lcola)==0:
            print('esta vacia ')
        elif self.size<= len(self.lcola):
            print('esta llena la cola')
        else:
            print('tiene elementos pero aun no esta llena ')

cola= Colas(5)
cola= Colas(5)