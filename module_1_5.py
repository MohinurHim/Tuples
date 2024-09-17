immutable_var = 3,4,True,'word'
print(immutable_var)
#immutable_var[0] = 1
#'tuple' object does not support item assignment
mutable_list = ([3,4,True,'word'],0)
print(mutable_list)
mutable_list [0][1] = 3
print(mutable_list)