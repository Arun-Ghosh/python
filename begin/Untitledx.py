def purify(p):
  x = []
  for i in p:
    if i%2 == 0:
      x.in
      i = i + 1
return x
print purify([2,4,6])



def median(l):
  if len(l)%2 == 0:
    l.sort()
    p = len(l)/2
    return l.index(0,p)
print median( [0, 1, 2, 3, 4, 5] )  


def median(l):
  if len(l)%2 != 0:
    l.sort()
    p = len(l)/2
    return l[p]
  elif len(l)%2 == 0:
    l.sort()
    p = len(l)/2
    q = float((l[p-1] + l[p])/2.0)
    return q
print median( [6, 1, 5, 2, 4, 3] ) 

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def grades_sum(scores):
  total = 0
  for i in scores:
    total = total + i
  return total
print grades_sum(grades)




grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance = ((average - score) ** 2) + variance
    result = float(variance)/len(scores)
  return result
print grades_variance(grades)




class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg = mpg
    self.battery_type = battery_type
  
  def drive_car(self):
    self.condition = "like new"
    
print my_car.condition
my_car.drive_car()
print my_car.condition

my_car = ElectricCar("Austin", "Blue", 86, "molten salt")

my_car.drive_car()
print my_car.condition


    
    
f = open("~/Downloads/abcd.txt", "r+"):
  print f
  f.close()

  ZCFMCRDAGPRABZOGCZEV

  

