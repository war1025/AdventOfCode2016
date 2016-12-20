

class Link(object):

   def __init__(self, value):
      self.value = value

      self.prev = self
      self.next = self

   def remove(self):
      self.prev.next = self.next
      self.next.prev = self.prev

   def insertAfter(self, link):
      self.next.prev = link

      link.prev = self
      link.next = self.next

      self.next = link



def main():

   data = 3004953

   main = Link(1)

   end = main

   for idx in xrange(1, data):
      link = Link(idx + 1)
      end.insertAfter(link)

      end = link

   to_remove = main

   for _ in xrange(data / 2):
      to_remove = to_remove.next

   while data > 1:
      to_remove.remove()
      to_remove = to_remove.next

      if (data & 1) == 1:
         to_remove = to_remove.next

      data -= 1

   print "Final position:", to_remove.value

def printLinks(link):
   values = [link.value]

   start = link.next

   while start != link:
      values.append(start.value)
      start = start.next

   print values

if __name__ == "__main__":
   main()
