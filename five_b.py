
from hashlib import md5

def main():

   data = "uqwqemis"

   passwd = [None] * 8

   idx = 0
   found = 0

   while found < 8:
      digest = md5(data + str(idx)).hexdigest()

      if digest[:5] == "00000":
         pos = int(digest[5], 16)
         if pos < 8:
            if passwd[pos] is None:
               passwd[pos] = digest[6]
               found += 1

      idx += 1

   print "Password:", passwd

if __name__ == "__main__":
   main()
