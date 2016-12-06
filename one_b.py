
NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

def main():

   with open("./one_a.txt", "r") as f:
      data = f.read()

   steps = data.split(", ")

   value = (0, 0, NORTH)

   previous_locations = set()

   for step in steps:
      rot, distance = step[0], int(step[1:])

      if rot == "L":
         value = left(value)
      else:
         value = right(value)

      for _ in xrange(distance):
         value = (value[0] + 1, value[1], value[2])

         as_north = rotateNorth(value)

         if as_north in previous_locations:
            print "Distance:", (abs(value[0]) + abs(value[1]))
            return

         previous_locations.add(as_north)

def left(value):
   return (-value[1], value[0], (value[2] - 1) % 4)

def right(value):
   return (value[1], -value[0], (value[2] + 1) % 4)

def rotateNorth(value):
   while value[2] != NORTH:
      value = left(value)
   return value


if __name__ == "__main__":
   main()
