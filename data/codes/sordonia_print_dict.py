import pprintimport sysimport cPickleimport numpy
print cPickle.load(open(sys.argv[1], 'r'))[sys.argv[2]]