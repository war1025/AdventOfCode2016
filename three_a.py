

def main():

   with open("three_a.txt", "r") as f:
      data = f.read()

   count = 0

   for line in data.split("\n"):
      if len(line) == 0:
         continue

      vals = sorted([int(val) for val in filter(None, line.split(" "))])

      if (vals[0] + vals[1]) > vals[2]:
         count +=1

   print "Count:", count



if __name__ == "__main__":
   main()
