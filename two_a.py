

def main():

   with open("two_a.txt", "r") as f:
      data = f.read()

   position = (1, 1)

   movements = {
      "U" : lambda p : (p[0], clamp(p[1] - 1)),
      "D" : lambda p : (p[0], clamp(p[1] + 1)),
      "L" : lambda p : (clamp(p[0] - 1), p[1]),
      "R" : lambda p : (clamp(p[0] + 1), p[1]),
   }

   code = ""

   for line in data.split("\n"):
      for move in line:
         position = movements[move](position)

      if len(line) > 0:
         code += keypadValue(position)

   print "Code:", code


def clamp(val):
   return min(max(val, 0), 2)

def keypadValue(pos):
   return str((pos[1] * 3) + (pos[0] + 1))


if __name__ == "__main__":
   main()
