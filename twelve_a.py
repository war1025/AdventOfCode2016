

def main():

   with open("./twelve_a.txt", "r") as f:
      data = f.read().split("\n")[:-1]

   registers = {
      "a" : 0,
      "b" : 0,
      "c" : 0,
      "d" : 0
   }

   ptr = 0

   while ptr < len(data):
      if data[ptr].startswith("inc"):
         registers[data[ptr][4]] += 1
      elif data[ptr].startswith("dec"):
         registers[data[ptr][4]] -= 1
      elif data[ptr].startswith("cpy"):
         parts = data[ptr].split(" ")
         if parts[1] in registers.viewkeys():
            registers[parts[2]] = registers[parts[1]]
         else:
            registers[parts[2]] = int(parts[1])
      elif data[ptr].startswith("jnz"):
         parts = data[ptr].split(" ")
         if parts[1] in registers.viewkeys():
            if registers[parts[1]] != 0:
               ptr += int(parts[2])
               continue
         else:
            if int(parts[1]) != 0:
               ptr += int(parts[2])
               continue

      ptr += 1

   print "Registers:", registers

if __name__ == "__main__":
   main()
