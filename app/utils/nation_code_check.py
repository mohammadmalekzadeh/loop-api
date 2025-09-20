def check_id(id):
  def devide(x,y):
    a = 0
    for i in range(x):
      if y*i <= x:
        a = i
      else:
        return a,x-(a*y)
        break


  lst = []

  for i in range(9):
    lst.append(int(id[i]) * int(10-i))


  if (devide(sum(lst),11)[1]) < 2:
    if int(id[-1]) ==devide(sum(lst),11)[1]:
      return True
    else:
      return False

  else:
    if int(id[-1]) ==(11-(devide(sum(lst),11)[1])):
      return True
    else:
      return False