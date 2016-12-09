
import re

CODE = re.compile("\((?P<length>[^x]+)x(?P<repeat>[^\)]+)\)")

def main():

   with open("./nine_a.txt", "r") as f:
      data = f.read().replace("\n", "")

   data = re.compile("\s").sub("", data)

   length = expand(data, 0, len(data))

   print "Output length:", length

def decompress(data, start):
   match = CODE.match(data, start)

   length = int(match.group("length"))
   repeat = int(match.group("repeat"))

   idx = match.span()[1]

   data_length = expand(data, idx, idx + length)

   return data_length * repeat, idx + length

def expand(data, start, end):
   length = 0

   idx = start

   while idx < end:
      if CODE.match(data, idx):
         part_length, idx = decompress(data, idx)

         length += part_length
      else:
         length += 1
         idx += 1

   return length




if __name__ == "__main__":
   main()
