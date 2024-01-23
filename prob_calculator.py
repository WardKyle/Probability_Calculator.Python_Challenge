import copy
import random

class Hat:

  def __init__(self,
               yellow=0,
               red=0,
               blue=0,
               green=0,
               orange=0,
               black=0,
               pink=0,
               striped=0,
               test=0):
    self.yellow = ["yellow" for el in range(yellow)]
    self.green = ["green" for el in range(green)]
    self.red = ["red" for el in range(red)]
    self.blue = ["blue" for el in range(blue)]
    self.orange = ["orange" for el in range(orange)]
    self.black = ["black" for el in range(black)]
    self.pink = ["pink" for el in range(pink)]
    self.striped = ["striped" for el in range(striped)]
    self.test = ["test" for el in range(test)]
    self.contents = self.yellow + self.green + self.red + self.blue + self.orange + self.black + self.pink + self.striped + self.test

  def __str__(self):
    return ','.join(self.contents)

  def draw(self, num, use_arr = ""):
    arr = self.contents if use_arr == "" else use_arr
    if num > len(arr) or len(arr) == 0:
      return self.contents
    drawn = []
    for el in range(num):
      rand_int = random.randint(0, len(arr) - 1) if len(arr) > 1 else 0
      drawn.append(arr.pop(rand_int))
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  passed,drawn,hat_arr,n_experiment_test = [],{},"",""
  for x in range(num_experiments):
    drawn = {
      'blue':0,
      'red':0,
      'yellow':0,
      'green':0,
      'orange':0,
      'black':0,
      'pink':0,
      'striped':0,
      'test':0
    }
    hat_arr = str(hat).split(',')
    for y in range(num_balls_drawn):
      draw = hat.draw(1,hat_arr)[0]
      drawn[draw] = drawn[draw] + 1
    n_experiment_test = True
    for key,val in expected_balls.items():
      if drawn[key] < val:
        n_experiment_test = False
        break
    if n_experiment_test:
      passed.append(True)
  return (len(passed)/num_experiments) 
