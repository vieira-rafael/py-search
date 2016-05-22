# coding=utf-8# ## Written in Python.  See http://www.python.org/# Placed in the public domain.# Neil Schemenauer <nas@arctrix.com>
import mathimport random
random.seed(0)

def rand(a, b): """     a <= rand < b     :param a:    :param b:    :return: """ return (b - a) * random.random() + a

def makeMatrix(I, J, fill=0.0): """    NumPy    :param I:     :param J:     :param fill:     :return: """    m = [] for i in range(I):        m.append([fill] * J) return m

def randomizeMatrix(matrix, a, b): """     :param matrix:    :param a:    :param b: """ for i in range(len(matrix)): for j in range(len(matrix[0])):            matrix[i][j] = random.uniform(a, b)

def sigmoid(x): """    sigmoid 1/(1+e^-x)    :param x:    :return: """ return 1.0 / (1.0 + math.exp(-x))

def dsigmoid(y): """    sigmoid     :param y:    :return: """ return y * (1 - y)

class NN: def __init__(self, ni, nh, no): # number of input, hidden, and output nodes """         :param ni:        :param nh:        :param no: """ self.ni = ni + 1 # +1  self.nh = nh self.no = no
 #  self.ai = [1.0] * self.ni self.ah = [1.0] * self.nh self.ao = [1.0] * self.no
 #  self.wi = makeMatrix(self.ni, self.nh)  #  self.wo = makeMatrix(self.nh, self.no)  #  #         randomizeMatrix(self.wi, -0.2, 0.2)        randomizeMatrix(self.wo, -2.0, 2.0) #  self.ci = makeMatrix(self.ni, self.nh) self.co = makeMatrix(self.nh, self.no)
 def runNN(self, inputs): """         :param inputs:        :return: """ if len(inputs) != self.ni - 1: print 'incorrect number of inputs'
 for i in range(self.ni - 1): self.ai[i] = inputs[i]
 for j in range(self.nh): sum = 0.0 for i in range(self.ni): sum += ( self.ai[i] * self.wi[i][j] ) self.ah[j] = sigmoid(sum)
 for k in range(self.no): sum = 0.0 for j in range(self.nh): sum += ( self.ah[j] * self.wo[j][k] ) self.ao[k] = sigmoid(sum)
 return self.ao

 def backPropagate(self, targets, N, M): """         :param targets:         :param N:         :param M:         :return:  """ # http://www.youtube.com/watch?v=aVId8KMsdUU&feature=BFa&list=LLldMCkmXl4j9_v0HeKdNcRA
 #  deltas # dE/dw[j][k] = (t[k] - ao[k]) * s'( SUM( w[j][k]*ah[j] ) ) * ah[j]        output_deltas = [0.0] * self.no for k in range(self.no):            error = targets[k] - self.ao[k]            output_deltas[k] = error * dsigmoid(self.ao[k])
 #  for j in range(self.nh): for k in range(self.no): # output_deltas[k] * self.ah[j]  dError/dweight[j][k]                change = output_deltas[k] * self.ah[j] self.wo[j][k] += N * change + M * self.co[j][k] self.co[j][k] = change
 #  deltas        hidden_deltas = [0.0] * self.nh for j in range(self.nh):            error = 0.0 for k in range(self.no):                error += output_deltas[k] * self.wo[j][k]            hidden_deltas[j] = error * dsigmoid(self.ah[j])
 #  for i in range(self.ni): for j in range(self.nh):                change = hidden_deltas[j] * self.ai[i] # print 'activation',self.ai[i],'synapse',i,j,'change',change self.wi[i][j] += N * change + M * self.ci[i][j] self.ci[i][j] = change
 #  # 1/2 **2         error = 0.0 for k in range(len(targets)):            error = 0.5 * (targets[k] - self.ao[k]) ** 2 return error

 def weights(self): """  """ print 'Input weights:' for i in range(self.ni): print self.wi[i] print print 'Output weights:' for j in range(self.nh): print self.wo[j] print ''
 def test(self, patterns): """         :param patterns: """ for p in patterns:            inputs = p[0] print 'Inputs:', p[0], '-->', self.runNN(inputs), '\tTarget', p[1]
 def train(self, patterns, max_iterations=1000, N=0.5, M=0.1): """         :param patterns:        :param max_iterations:        :param N:        :param M: """ for i in range(max_iterations): for p in patterns:                inputs = p[0]                targets = p[1] self.runNN(inputs)                error = self.backPropagate(targets, N, M) if i % 50 == 0: print 'Combined error', error self.test(patterns)

def main():    pat = [        [[0, 0], [1]],        [[0, 1], [1]],        [[1, 0], [1]],        [[1, 1], [0]]    ]    myNN = NN(2, 2, 1)    myNN.train(pat)

if __name__ == "__main__":    main()