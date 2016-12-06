
from collections import defaultdict

def main():

   with open("./six_a.txt", "r") as f:
      data = f.read()

   lines = data.split("\n")

   dicts = [defaultdict(int) for _ in xrange(len(lines[0]))]

   for line in lines:
      for idx, char in enumerate(line):
         dicts[idx][char] += 1

   message = ""

   for item in dicts:
      message += max((count, value) for (value, count) in item.viewitems())[1]

   print "Message:", message

if __name__ == "__main__":
   main()

