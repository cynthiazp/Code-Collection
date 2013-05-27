import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    row = record[1]
    col = record[2]
    
    if(matrix == 'a'):
        for i in range(0,5):
            mr.emit_intermediate((row,i), record)
    else:
        for j in range(0,5):
            mr.emit_intermediate((j,col), record)
    
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    left = []
    right = []
    sum = 0
    for record in list_of_values:
        if(record[0] == 'a'):
             left.append(record)
        else:
             right.append(record)

    for v1 in left:
        for v2 in right:
            if v1[2] == v2[1]:
                sum += v1[3]*v2[3]
    mr.emit((key[0],key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
