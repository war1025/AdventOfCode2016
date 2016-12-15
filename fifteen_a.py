
class Disc(object):

   def __init__(self, size, initialPos, number):
      self.size = size
      self.pos  = initialPos

      for _ in xrange(number):
         self.increment()

   def increment(self):
      self.pos += 1
      if self.pos == self.size:
         self.pos = 0

   def decrement(self):
      self.pos -= 1
      if self.pos < 0:
         self.pos = (self.size - 1)

def main():

   data = [
      Disc(17, 1, 0),
      Disc(7,  0, 1),
      Disc(19, 2, 2),
      Disc(5,  0, 3),
      Disc(3,  0, 4),
      Disc(13, 5, 5)
   ]

   #data = [
   #   Disc(5, 4, 0),
   #   Disc(2, 1, 1)
   #]


   idx = -1
   while {disc.pos for disc in data} != {0}:
      idx += 1
      for disc in data:
         disc.increment()

   print "Aligned at:", idx

if __name__ == "__main__":
   main()
