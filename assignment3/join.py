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
    key = record[1]
    mr.emit_intermediate(key, record)
    
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    left = []
    right = []
   
    for value in list_of_values:
        if value[0] == 'order':
            left.append(value)
        else:
            right.append(value)
            
    for v1 in left:
        for v2 in right:
            join = v1 + v2
            mr.emit(join)

                      
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
