class Musician: 
    '''
    base class to handle common functionality which particular kinds of musicians will inherit.
    inherits name attributes for all child classes
    
'''
    def __init__(self, name):
        self.name = name


class Band:
    '''
       Band class to create instances that have name,members attributes
       also each instance will have a play_solo method that asks each member musician to play a solo
       each instance should have  __str__ and __repr__ methods.
       and this Band class have a class method to_list which returns a list of previously created Band instances
    '''
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"
        pass
    def __repr__(self):
        return f'The Band instance, {self.name}'
       

    def play_solos(self):
        return list(map(lambda member: member.play_solo(), self.members))

    @classmethod
    def to_list(cls):
        return cls.instances



class Guitarist(Musician):
    '''
    Musician instance should have  __str__ and __repr__ methods.
    get_instrument method that returns string.
    a play_solo method that returns string.
    '''
    
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Bassist(Musician):
    '''
    Musician instance should have  __str__ and __repr__ methods.
    get_instrument method that returns string.
    a play_solo method that returns string.
    '''

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer(Musician):
    '''
    Musician instance should have  __str__ and __repr__ methods.
    get_instrument method that returns string.
    a play_solo method that returns string.
    '''

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"
    


__name__=="__main__"  

g1=Guitarist("tamim")
print(g1)
print(g1.play_solo())
print(g1.get_instrument())
print(g1.__repr__())
g2=Band("julia")
g3=Band("Mohammed")
print(g2.to_list())
print(g2)
