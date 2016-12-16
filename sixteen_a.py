

def main():

   data = "10011111011011001"
   length = 272

   while len(data) < length:
      data = dragon(data)

   data = data[:length]

   while (len(data) & 1) != 1:
      data = checksum(data)

   print "Checksum:", data

def dragon(value):
   new_value = "".join(reversed(value.replace("1", "2").replace("0", "1").replace("2", "0")))

   return "%s0%s" % (value, new_value)

def checksum(value):
   parts = []
   for idx in xrange(0, len(value), 2):
      if value[idx] == value[idx + 1]:
         parts.append("1")
      else:
         parts.append("0")

   return "".join(parts)


if __name__ == "__main__":
   main()
