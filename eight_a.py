

def main():

   with open("./eight_a.txt", "r") as f:
      data = f.read()

   grid = [[False for _ in xrange(6)] for _ in xrange(50)]

   lines = data.split("\n")[:-1]

   for line in lines:
      if line.startswith("rect"):
         rect(grid, line)
      elif line.startswith("rotate row"):
         rotateRow(grid, line)
      elif line.startswith("rotate column"):
         rotateColumn(grid, line)

   print "Number on:", sum(1 for column in grid for row in column if row == True)

def rect(grid, command):
   x, y = [int(val) for val in command[len("rect"):].split("x")]

   for idx_x in xrange(x):
      for idx_y in xrange(y):
         grid[idx_x][idx_y] = True

def rotateRow(grid, command):
   row, offset = [int(val) for val in command.split("=")[1].split(" by ")]

   values = [grid[col][row] for col in xrange(50)]

   for idx in xrange(50):
      grid[(idx + offset) % 50][row] = values[idx]

def rotateColumn(grid, command):
   col, offset = [int(val) for val in command.split("=")[1].split(" by ")]

   values = [grid[col][row] for row in xrange(6)]

   for idx in xrange(6):
      grid[col][(idx + offset) % 6] = values[idx]

def gridToString(grid):
   return "\n".join([
      "".join(["#"if val else "." for val in column])
      for column in grid
   ])

if __name__ == "__main__":
   main()
