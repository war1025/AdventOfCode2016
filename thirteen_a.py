
import simplejson

from math import ceil, log

from heapq import heappush, heappop

gPreviousStates = set()

def _isPreviousState(state):
   return (state.x, state.y) in gPreviousStates

class State(object):

   def __init__(self):
      self.distance = 0
      self.stepNo   = 0
      self.x = 0
      self.y = 0

   def isValidState(self):
      if self.x < 0 or self.y < 0:
         return False

      value = (self.x * self.x) + (3 * self.x) \
                 + (2 * self.x * self.y) + self.y + (self.y * self.y) + 1352

      count = sum(
         1
         for idx in xrange(1, int(ceil(log(value, 2))))
         if value & (1 << idx) > 0
      )

      return (count % 2) == 0

   def getNextStates(self):
      new_state = self.moveToNextState(self.x + 1, self.y)

      if new_state.isValidState() and not _isPreviousState(new_state):
         gPreviousStates.add((new_state.x, new_state.y))
         yield new_state

      new_state = self.moveToNextState(self.x - 1, self.y)

      if new_state.isValidState() and not _isPreviousState(new_state):
         gPreviousStates.add((new_state.x, new_state.y))
         yield new_state

      new_state = self.moveToNextState(self.x, self.y + 1)

      if new_state.isValidState() and not _isPreviousState(new_state):
         gPreviousStates.add((new_state.x, new_state.y))
         yield new_state

      new_state = self.moveToNextState(self.x, self.y - 1)

      if new_state.isValidState() and not _isPreviousState(new_state):
         gPreviousStates.add((new_state.x, new_state.y))
         yield new_state

   def moveToNextState(self, newX, newY):
      new_state = State()
      new_state.stepNo = self.stepNo + 1
      new_state.x = newX
      new_state.y = newY

      new_state._calculateDistance()

      return new_state

   def _calculateDistance(self):
      self.distance = abs(self.x - 31) + abs(self.y - 39)


def main():
   initial_state = State()
   initial_state.x = 1
   initial_state.y = 1
   initial_state._calculateDistance()

   gPreviousStates.add((initial_state.x, initial_state.y))

   states = [(initial_state.distance, initial_state)]

   while len(states) > 0:
      new_states = heappop(states)[1].getNextStates()

      for state in new_states:
         if state.distance == 0:
            print "Found state:", state.stepNo
            return
         heappush(states, (state.distance, state))

if __name__ == "__main__":
   main()
