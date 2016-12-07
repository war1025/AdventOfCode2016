
import re

BRACKETS = re.compile("(\[[^\]]*\])")

def main():

   with open("./seven_a.txt", "r") as f:
      data = f.read()

   lines = data.split("\n")

   num_matches = 0

   for line in lines:
      if len(line) == 0:
         continue

      parts = BRACKETS.split(line)

      outer_pairs = set()
      inner_pairs = set()

      for part in parts:
         if part[0] != "[":
            outer_pairs |= _findPairs(part)
         else:
            inner_pairs |= _findPairs(part)

      if not outer_pairs.isdisjoint(inner_pairs):
         num_matches += 1

   print "Num matches:", num_matches


def _findPairs(text):
   invert = False
   if text[0] == "[":
      text = text[1:-1]
      invert = True

   pairs = set()

   for idx in xrange(len(text) - 2):
      if text[idx] == text[idx + 2] \
            and text[idx] != text[idx + 1]:
         pairs.add(text[idx:idx+3])

   if invert:
      pairs = {pair[1] + pair[0] + pair[1] for pair in pairs}

   return pairs

if __name__ == "__main__":
   main()
