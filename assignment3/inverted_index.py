import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):

	key = record[0]
	value = record[1]
	words = value.split()
	for w in words:
		mr.emit_intermediate(w, key)

def reducer(key,list_of_values):
	
	l2 = []
	for value in list_of_values:
		if not value in l2:
			l2.append(value)
	mr.emit((key,l2))

if __name__ == "__main__":
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)

