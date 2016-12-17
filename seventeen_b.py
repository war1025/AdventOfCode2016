
from hashlib import md5

from heapq import heappush, heappop

class State(object):

   def __init__(self):
      self.distance = 0
      self.stepNo   = 0

      self.path = []

      self.row    = 0
      self.column = 0

   def getNextStates(self):
      next_hash = md5("pvhmgsws" + "".join(self.path)).hexdigest()[:4]

      if self.row > 0 and next_hash[0] in ["b", "c", "d", "e", "f"]:
         new_state = self.moveToNextState("U")

         yield new_state

      if self.row < 3 and next_hash[1] in ["b", "c", "d", "e", "f"]:
         new_state = self.moveToNextState("D")

         yield new_state

      if self.column > 0 and next_hash[2] in ["b", "c", "d", "e", "f"]:
         new_state = self.moveToNextState("L")

         yield new_state

      if self.column < 3 and next_hash[3] in ["b", "c", "d", "e", "f"]:
         new_state = self.moveToNextState("R")

         yield new_state

   def moveToNextState(self, direction):
      new_state = State()
      new_state.stepNo = self.stepNo + 1
      new_state.path = list(self.path) + [direction]
      if direction == "U":
         new_state.row = self.row - 1
         new_state.column = self.column

      if direction == "D":
         new_state.row = self.row + 1
         new_state.column = self.column

      if direction == "L":
         new_state.row = self.row
         new_state.column = self.column - 1

      if direction == "R":
         new_state.row = self.row
         new_state.column = self.column + 1

      new_state._calculateDistance()

      return new_state

   def _calculateDistance(self):
      self.distance = (3 - self.row) + (3 - self.column)

def main():
   initial_state = State()
   initial_state._calculateDistance()

   states = [(initial_state.distance, initial_state)]

   solved_states = []

   while len(states) > 0:
      new_states = heappop(states)[1].getNextStates()

      for state in new_states:
         if state.distance == 0:
            solved_states.append(state)
         else:
            heappush(states, (state.distance, state))

   print "Longest path:",  max(len(state.path) for state in solved_states)

if __name__ == "__main__":
   main()
