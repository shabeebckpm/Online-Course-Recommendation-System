import browserhistory as bh
dict_obj = bh.get_browserhistory() 
for  x in range(20)  :
  print ( dict_obj['chrome'][x][1] )