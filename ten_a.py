
import re

from collections import defaultdict

INITIAL_RE = re.compile("value (?P<value>[^ ]+) goes to bot (?P<bot>.*)")

COMPARISON_RE = re.compile(
   "bot (?P<bot>[^ ]+) gives low to (?P<lowPlace>[^ ]+) (?P<lowNumber>[^ ]+) " \
   "and high to (?P<highPlace>[^ ]+) (?P<highNumber>.*)"
)

class Bot(object):

   def __init__(self):
      self.number = None
      self.values = []
      self.lowDestination = None
      self.highDestination = None

      self.hadRequested = False

   def receiveValue(self, value):
      self.values.append(value)

      self.tryAction()

   def setLowDestination(self, dest):
      self.lowDestination = dest

      self.tryAction()

   def setHighDestination(self, dest):
      self.highDestination = dest

      self.tryAction()

   def tryAction(self):
      if len(self.values) == 2 and None not in (self.lowDestination, self.highDestination):
         self.lowDestination.receiveValue(min(self.values))
         self.highDestination.receiveValue(max(self.values))

class Output(object):

   def __init__(self):
      self.values = []

   def receiveValue(self, value):
      self.values.append(value)

def main():
   bots = defaultdict(Bot)
   outputs = defaultdict(Output)

   with open("./ten_a.txt", "r") as f:
      data = f.read().split("\n")

   for line in data:
      match = INITIAL_RE.match(line)
      if match is not None:
         bot = bots[int(match.group("bot"))]
         bot.receiveValue(int(match.group("value")))

      match = COMPARISON_RE.match(line)
      if match is not None:
         bot = bots[int(match.group("bot"))]

         low_type = bots if match.group("lowPlace") == "bot" else outputs

         bot.setLowDestination(low_type[int(match.group("lowNumber"))])

         high_type = bots if match.group("highPlace") == "bot" else outputs

         bot.setHighDestination(high_type[int(match.group("highNumber"))])

   print "Bot:", [number for (number, bot) in bots.viewitems() if sorted(bot.values) == [17, 61]]

if __name__ == "__main__":
   main()


