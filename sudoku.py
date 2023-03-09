def contains(list, val):
  for i in range(len(list)):
    if list[i] == val:
      return True
  return False


def has_one(list, val):
  times = 0
  for i in range(len(list)):
    if list[i] == val:
      times += 1
  return times == 1

  
def make_box(board, r, c):
  box  = []
  if r < 3:
    if c < 3:
      for i in range(3):
        for j in range(3):
          if board[i][j] != ".":
            #print(board[i][j])
            box.append(int(board[i][j]))
            
    elif c < 6:
      for i in range(3):
        for j in range(3, 6):
          if board[i][j] != ".":
            box.append(int(board[i][j]))
    else:
      for i in range(3):
        for j in range(6, 9):
          if board[i][j] != ".":
            box.append(int(board[i][j]))
  elif r < 6:
    if c < 3:
      for i in range(3, 6):
        for j in range(3):
          if board[i][j] != ".":
            box.append(int(board[i][j]))
    elif c < 6:
      for i in range(3, 6):
        for j in range(3, 6):
          if board[i][j] != ".":
            box.append(int(board[i][j]))
    else:
      for i in range(3, 6):
        for j in range(6, 9):
          if board[i][j] != ".":
            box.append(int(board[i][j]))
  else:
    if c < 3:
      for i in range(6, 9):
        for j in range(3):
          if board[i][j] != ".":
            box.append(int(board[i][j]))
    elif c < 6:
      for i in range(6, 9):
        for j in range(3, 6):
          if board[i][j] != ".":
            box.append(int(board[i][j]))
    else:
      for i in range(6, 9):
        for j in range(6, 9):
          if board[i][j] != ".":
            box.append(int(board[i][j]))
  return box 
def solver(board):
  possible = {}
  #errors = 0
  locked = True
  while locked:
    locked = False
    for i in range(9):
      for j in range(9):
        if board[i][j] == ".":
          nums = []
          for k in range(1, 10):
            row = board[i]
            column = []
            for l in range(9):
              column.append(board[l][j])
            box = make_box(board, i, j)
          #print(box)
            if not(contains(row, str(k))) and not(contains(column, str(k))) and not(contains(box, k)):
              nums.append(str(k))
            #board[i][j] = str(k)
            #print(k)
            #break
            #possible[str(i*10+j)] = 
          #if k == 9:
           # errors += 1
              if len(nums) == 1:
                board[i][j] = nums[0]
                locked = True
              else:
                possible[str(i*10+j)] = nums
  #check rows for single blanks              
  for i in range(9):
    if has_one(board[i], "."):
      p = [1,2,3,4,5,6,7,8,9]
      for j in range(1,10):
        if contains(board[i], str(j)):
          p.remove(j)
      board[i][board[i].index(".")] = str(p[0])
  print(board)
  # cheeck cols
  for i in range(9):
    col = []
    for j in range(9):
      col.append(board[j][i])
    print(col)
    if has_one(col, "."):
      print(1)
      p = [1,2,3,4,5,6,7,8,9]
      for k in range(1, 10):
        if contains(col, str(k)):
          p.remove(k)
      board[col.index(".")][i] = str(p[0])
      
      
      
      
  #print(errors)
  return board


b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(b)
print(solver(b))
