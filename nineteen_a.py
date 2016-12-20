

def main():

   data = 3004953

   slots = [(idx + 1, 1) for idx in xrange(data)]

   while len(slots) > 1:
      for idx in xrange(len(slots) - 1):
         if slots[idx][1] > 0:
            slots[idx] = (slots[idx][0], slots[idx][1] + slots[idx + 1][1])
            slots[idx + 1] = (slots[idx + 1][0], 0)

      idx = len(slots) - 1
      if slots[idx][1] > 0:
         slots[idx] = (slots[idx][0], slots[idx][1] + slots[0][1])
         slots[0] = (slots[0][0], 0)

      slots = [slot for slot in slots if slot[1] != 0]

   print "Final slot:", slots[0][0]

if __name__ == "__main__":
   main()
