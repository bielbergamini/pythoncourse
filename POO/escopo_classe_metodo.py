class Animal:
    def __init__(self, animal):
        self.animal = animal

           
    def comendo(self, alimento):
        return f'O {self.animal} está comendo a {alimento}'





leao = Animal(animal='Leao')
print(leao.animal)
print(leao.comendo('presa'))


                                               
                                            
    


        
    


