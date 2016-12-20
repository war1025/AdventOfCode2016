

def main():

   data = ".^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^" \
          "...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^"


   num_safe = countSafe(data)

   for _ in xrange(1, 40):
      data = nextRow(data)

      num_safe += countSafe(data)

   print "Total number of safe spaces:", num_safe


def countSafe(row):
   return sum(1 for tile in row if tile == ".")

def nextRow(curRow):
   return ["^" if nextIsTrap(idx, curRow) else "." for idx in xrange(len(curRow))]

def nextIsTrap(idx, curRow):
   left = "." if idx == 0 else curRow[idx - 1]
   center = curRow[idx]
   right = "." if idx == (len(curRow) - 1) else curRow[idx + 1]

   if (left, center, right) == ("^", "^", "."):
      return True

   if (left, center, right) == (".", "^", "^"):
      return True

   if (left, center, right) == ("^", ".", "."):
      return True

   if (left, center, right) == (".", ".", "^"):
      return True

   return False

if __name__ == "__main__":
   main()
