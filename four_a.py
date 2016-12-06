
from collections import defaultdict

def main():

   with open("./four_a.txt", "r") as f:
      data = f.read()

   lines = data.split("\n")[:-1]

   sector_sum = 0

   for line in lines:
      parts = line.split("-")

      counts = defaultdict(int)

      text  = "".join(parts[:-1])
      check = parts[-1].split("[")

      sector = int(check[0])

      checksum = check[1][:-1]

      for char in text:
         counts[char] += 1

      values = [
         item
         for _, item in sorted([(-count, char) for (char, count) in counts.items()])
      ]

      calculated = "".join(values[:5])

      if checksum == calculated:
         sector_sum += sector

   print "Sector sum:", sector_sum

if __name__ == "__main__":
   main()


