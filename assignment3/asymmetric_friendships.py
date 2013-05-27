import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate((record[0],record[1]), 1)
    mr.emit_intermediate((record[1],record[0]), 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    sum = 0
    for value in list_of_values:
        sum += value
    if sum == 1:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
