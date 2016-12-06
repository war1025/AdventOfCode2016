

def main():

   with open("./one_a.txt", "r") as f:
      data = f.read()

   steps = data.split(", ")

   value = (0, 0)

   for step in steps:
      rot, distance = step[0], int(step[1:])

      if rot == "L":
         value = left(value)
      else:
         value = right(value)

      value = (value[0] + distance, value[1])

   print "Distance:", (abs(value[0]) + abs(value[1]))

def left(value):
   return (-value[1], value[0])

def right(value):
   return (value[1], -value[0])


if __name__ == "__main__":
   main()
