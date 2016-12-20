


def main():

   with open("./twenty_a.txt", "r") as f:
      data = f.read().split("\n")[:-1]


   ranges = []
   for item in data:
      parts = item.split("-")
      ranges.append((int(parts[0]), int(parts[1])))

   ranges.sort()

   while True:
      cur_length = len(ranges)
      print "Ranges:", cur_length
      ranges = reduceRanges(ranges)

      if cur_length == len(ranges):
         break

   count = 0

   for idx in xrange(1, len(ranges)):
      count += (ranges[idx][0] - ranges[idx -1][1]) - 1

   print "Count:", count

def reduceRanges(ranges):
   new_ranges = [ranges[0]]

   for idx in xrange(1, len(ranges)):
      if ranges[idx][0] <= (new_ranges[-1][1] + 1):
         new_ranges[-1] = (
            min(new_ranges[-1][0], ranges[idx][0]),
            max(new_ranges[-1][1], ranges[idx][1])
         )
      else:
         new_ranges.append(ranges[idx])

   return new_ranges


if __name__ == "__main__":
   main()
