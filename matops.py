import numpy
N, M, P = map(int, raw_input().split())
n = numpy.array([map(int, raw_input().split()) for _ in range(N)])
m = numpy.array([map(int, raw_input().split()) for _ in range(M)])
print (numpy.concatenate((n, m)))