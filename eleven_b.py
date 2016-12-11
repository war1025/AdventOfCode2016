
import simplejson

from heapq import heappush, heappop

gPreviousStates = set()

def _isPreviousState(state):
   return state.getStateJson() in gPreviousStates

class State(object):

   def __init__(self):
      self.distance = 0
      self.stepNo   = 0
      self.elevator = 0

      self.floors = [] * 4

   def isValidState(self):
      if len(self.floors[self.elevator]) == 0:
         return False

      for floor in self.floors:
         generators = {item[0] for item in floor if item[1] == "G"}
         chips = {item[0] for item in floor if item[1] == "M"}

         if len(generators - chips) > 0 and len(chips - generators) > 0:
            return False

      return True

   def getNextStates(self):
      for combination in self._moveCombinations():
         if self.elevator > 0:
            new_state = self.moveToNextState(self.elevator - 1, combination)

            if new_state.isValidState() and not _isPreviousState(new_state):
               gPreviousStates.add(new_state.getStateJson())
               yield new_state

         if self.elevator < 3:
            new_state = self.moveToNextState(self.elevator + 1, combination)

            if new_state.isValidState() and not _isPreviousState(new_state):
               gPreviousStates.add(new_state.getStateJson())
               yield new_state


   def moveToNextState(self, nextFloor, load):
      new_state = State()
      new_state.stepNo = self.stepNo + 1
      new_state.elevator = nextFloor
      new_state.floors = [list(floor) for floor in self.floors]
      cur_floor  = new_state.floors[self.elevator]
      next_floor = new_state.floors[new_state.elevator]
      new_state.floors[self.elevator] = list(set(cur_floor) - load)
      new_state.floors[new_state.elevator] = list(set(next_floor) | load)

      new_state._calculateDistance()

      return new_state

   def _moveCombinations(self):
      cur_floor = self.floors[self.elevator]
      for idx in xrange(1, 2 ** len(cur_floor)):
         to_move = []
         for pos in xrange(len(cur_floor)):
            if idx & (1 << pos) > 0:
               to_move.append(cur_floor[pos])

         if len(to_move) <= 2:
            yield set(to_move)

   def _calculateDistance(self):
      distance = 0
      for idx, floor in enumerate(self.floors):
         distance += (3 - idx) * len(floor)

      self.distance = distance

   def getStateJson(self):
      return simplejson.dumps({
         "elevator" : self.elevator,
         "floors" : [sorted(floor) for floor in self.floors]
      })




def main():
   initial_state = State()
   initial_state.elevator = 0
   initial_state.floors = [
      ["SG", "SM", "PG", "PM", "EG", "EM", "DG", "DM"],
      ["TG", "RG", "RM", "CG", "CM"],
      ["TM"],
      []
   ]
   initial_state._calculateDistance()

   gPreviousStates.add(initial_state.getStateJson())

   tree_depth = 0

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
