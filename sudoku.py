# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
	[6,7,2,1,9,5,3,4,8],
	[1,9,8,3,4,2,5,6,7],
	[8,5,9,7,6,1,4,2,3],
	[4,2,6,8,5,3,7,9],	# <---
	[7,1,3,9,2,4,8,5,6],
	[9,6,1,5,3,7,2,8,4],
	[2,8,7,4,1,9,6,3,5],
	[3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
	[6,7,2,1,9,5,3,4,8],
	[1,9,8,3,4,2,5,6,7],
	[8,5,9,7,6,1,4,2,3],
	[4,2,6,8,5,3,7,9,1],
	[7,1,3,9,2,4,8,5,6],
	[9,6,1,5,3,7,2,8,4],
	[2,8,7,4,1,9,6,3,5],
	[3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
	[6,7,2,1,9,5,3,4,8],
	[1,9,8,3,8,2,5,6,7],
	[8,5,9,7,6,1,4,2,3],
	[4,2,6,8,5,3,7,9,1],
	[7,1,3,9,2,4,8,5,6],
	[9,6,1,5,3,7,2,8,4],
	[2,8,7,4,1,9,6,3,5],
	[3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
	[3,0,6,0,0,8,4,0,0],
	[8,0,0,0,4,0,0,0,2],
	[0,2,0,0,3,1,0,0,7],
	[0,0,0,0,8,0,0,0,0],
	[1,0,0,9,5,0,0,6,0],
	[7,0,0,0,9,0,0,0,1],
	[0,0,1,2,0,0,3,0,6],
	[0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
	[0,3,0,0,2,0,0,0,8],
	[0,0,9,6,0,0,5,0,0],
	[0,0,5,3,0,0,9,0,0],
	[0,1,0,0,8,0,0,0,2],
	[6,0,0,0,0,4,0,0,0],
	[3,0,0,0,0,0,0,1,0],
	[0,4,0,0,0,0,0,0,7],
	[0,0,7,0,0,0,3,0,0]]

from copy import copy, deepcopy

def valid_row(row):
	found = []
	for e in row:
		if e in found:
			return False
		
		if e!=0:
			found.append(e)
	return True
	
def check_sudoku(grid):
	valid = range(10)
	if len(grid)!=9:
		return None
	
	for row in grid:
		if len(row)!=9:
			return None
		for e in row:
			if e in valid==False:
				return None
	
	for row in grid:
		if valid_row(row)==False:
			return False
			
		for i in range(len(row)):
			if row[i]!=0:
				for row2 in grid:
					if row!=row2 and row[i]==row2[i]:
						return False;
			
	return True

def solve_sudoku (grid):
	c = check_sudoku(grid)
	if c==None or c==False:
		return None

	solved = True
	for row in grid:
		if 0 in row:
			solved = False
			break
			
	if solved==True:
		return grid
	
	for r in range(len(grid)):
		if 0 in grid[r]:
			c = grid[r].index(0)
			for n in range(9):
				new_grid = deepcopy(grid)
				#print_sudoku(new_grid)
				new_grid[r][c] = n+1
				#print "new_grid["+str(r)+"]["+str(c)+"]: "+str(n+1)
				#print_sudoku(new_grid)
				#print "---------------------------------"
				result = solve_sudoku(new_grid)
				if result!=None and result!=False:
					return result
			return False
	return False

def print_sudoku(grid):
	if grid==False or grid==None :
		print grid;
	else:
		i = 0
		j = 0

		for r in grid:
			for e in r:
				print " "+str(e),
				i+=1

				if i%3 == 0 and i<8:
					print " |",

			print ""
			i=0
			j+=1


			if j%3 == 0 and j<8:
				print " ==============================="

	print "\n"

print_sudoku(solve_sudoku(ill_formed))
print_sudoku(solve_sudoku(valid))
print_sudoku(solve_sudoku(invalid))
print_sudoku(solve_sudoku(easy))
print_sudoku(solve_sudoku(hard))