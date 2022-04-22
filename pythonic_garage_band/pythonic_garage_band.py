
class Musician:
  def __init__(self, name):
    self.name = name


class Guitarist(Musician):
  # def __init__(self, name):
  #   self.name = name

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
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"My name is {self.name} and I play bass"
  
  def __repr__(self):
    return f"Bassist instance. Name = {self.name}"

  @staticmethod
  def play_solo():
    return "bom bom buh bom"

  @staticmethod
  def get_instrument():
    return "bass"



class Drummer(Musician):
  def __init__(self, name):
    self.name = name
  
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

class Band:
  instances = []

  def __init__(self, name, members):
    self.name = name
    self.members = members
    Band.instances.append(self)
  
  
  def play_solos(self):
    solos = []
    for member in self.members:
      solos.append(member.play_solo())
    return solos

  @staticmethod
  def to_list():
    return Band.instances

