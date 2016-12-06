
from hashlib import md5

def main():

   data = "uqwqemis"

   passwd = ""

   idx = 0

   while len(passwd) < 8:
      digest = md5(data + str(idx)).hexdigest()

      if digest[:5] == "00000":
         passwd += digest[5]

      idx += 1

   print "Password:", passwd

if __name__ == "__main__":
   main()
