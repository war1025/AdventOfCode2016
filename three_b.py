

def main():

   with open("three_a.txt", "r") as f:
      data = f.read()

   count = 0

   columns = [[], [], []]

   for line in data.split("\n"):
      if len(line) == 0:
         continue

      vals = [int(val) for val in filter(None, line.split(" "))]

      for idx in xrange(3):
         columns[idx].append(vals[idx])

   for column in columns:
      idx = 0

      while idx < len(column):
         vals = sorted([column[idx], column[idx + 1], column[idx + 2]])

         if (vals[0] + vals[1]) > vals[2]:
            count +=1

         idx += 3

   print "Count:", count



if __name__ == "__main__":
   main()
