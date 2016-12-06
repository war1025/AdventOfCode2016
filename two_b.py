

def main():

   with open("two_a.txt", "r") as f:
      data = f.read()

   position = (0, 2)

   movements = {
      "U" : lambda p : (p[0], clamp(p[1] - 1, p[0])),
      "D" : lambda p : (p[0], clamp(p[1] + 1, p[0])),
      "L" : lambda p : (clamp(p[0] - 1, p[1]), p[1]),
      "R" : lambda p : (clamp(p[0] + 1, p[1]), p[1]),
   }

   code = ""

   for line in data.split("\n"):
      for move in line:
         position = movements[move](position)

      if len(line) > 0:
         code += keypadValue(position)

   print "Code:", code


def clamp(val, idx):
   bounds = boundsForIdx(idx)
   return min(max(val, bounds[0]), bounds[1])

def keypadValue(pos):
   pad = [
   [" ", " ", "1", " ", " "],
   [" ", "2", "3", "4", " "],
   ["5", "6", "7", "8", "9"],
   [" ", "A", "B", "C", " "],
   [" ", " ", "D", " ", " "]
   ]
   return pad[pos[1]][pos[0]]

def boundsForIdx(idx):
   dist = abs(2 - idx)
   return (dist, 4 - dist)


if __name__ == "__main__":
   main()
