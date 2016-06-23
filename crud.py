class Crud():

  id = 1

  def __init__(self,name):
    self.name = name
    self.id = Crud.id
    Crud.id += 1

cruds_list = [Crud('first')]