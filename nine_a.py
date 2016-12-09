
import re

CODE = re.compile("\((?P<length>[^x]+)x(?P<repeat>[^\)]+)\)")

def main():

   with open("./nine_a.txt", "r") as f:
      data = f.read().replace("\n", "")

   data = re.compile("\s").sub("", data)

   output = []

   idx = 0

   while idx < len(data):
      if data[idx] == "(":
         match = CODE.match(data, idx)

         length = int(match.group("length"))
         repeat = int(match.group("repeat"))

         idx = match.span()[1]

         text = [char for char in data[idx:idx + length]]

         for _ in xrange(repeat):
            output.extend(text)

         idx += length

      else:
         output.append(data[idx])
         idx += 1

   print "Output length:", len(output)

if __name__ == "__main__":
   main()
