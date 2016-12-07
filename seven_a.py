
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

      match = len([1 for part in parts if part[0] != "[" and _hasPair(part)]) > 0  \
                 and len([1 for part in parts if part[0] == "[" and _hasPair(part)]) == 0

      if match:
         num_matches += 1

   print "Num matches:", num_matches


def _hasPair(text):
   if text[0] == "[":
      text = text[1:-1]

   for idx in xrange(len(text) - 3):
      if text[idx] == text[idx + 3] \
            and text[idx + 1] == text[idx + 2] \
            and text[idx] != text[idx + 1]:
         return True

   return False

if __name__ == "__main__":
   main()
