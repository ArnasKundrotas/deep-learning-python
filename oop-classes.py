import numpy as np
class model(object):
  
  def __init__(self, num_layers, num_units, name):
    
    self.layers   = num_layers
    self.units    = num_units
    self.name     = name
    self.weights  = 1

  def how_many_units(self):
    total_units = self.layers * self.units
    print(f'There are {total_units} units in the model.')

  def train_model(self,x):
    self.weights += x
    return self.weights

  def __str__(self):
    return f'this is a {self.name} architecture.'

class new_class(object):
  
  def __init__(self, num_layers, num_units, name):
    
    self.layers   = num_layers
    self.units    = num_units
    self.name     = name
    self.weights  = np.random.rand(num_layers, self.units)

  def how_many_units(self):
    total_units = self.layers * self.units
    print(f'There are {total_units} units in the model.')

  def train_model(self,x,y):
    self.weights = self.weights*x+y

  def __str__(self):
    return f'this is a {self.name} architecture.'


m2 = new_class(2,3,"CNN")

m2.train_model(20,30)

print(m2.weights)

# vanishing gradiens?
# exploding gradiens?