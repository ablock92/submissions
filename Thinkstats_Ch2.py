import sys
sys.path.append("./thinkstats.code")
import thinkstats
import math
import survey
import first
import Pmf
import operator


def Ex2_1():
    weight_sequence=[1,1,1,3,3,591]
    mean,variance = thinkstats.MeanVar(weight_sequence)
    standard_deviation = math.sqrt(variance)
    print "mean weight: %i \nvariance: %i \nstandard deviation: %i" % (mean, variance, standard_deviation)

def Ex2_2():
    first.Summarize('thinkstats.code')


def Ex2_3():
    def AllModes():
        hist = Pmf.MakeHistFromList([1,1,3,4,4])
        frequencies = [] # (Value,Freq)
        for val in sorted (hist.Values()):
            frequencies.append((val,hist.Freq(val)))
        return sorted(frequencies,key=operator.itemgetter(1),reverse=True)

    def Mode():
        frequencies = AllModes()
        return frequencies[0][0]
    
    print Mode()

def Ex2_5():
    def PmfMean(pmf):
        mean=0
        for xi in (pmf.Values()):
            mean+= pmf.Prob(xi) * xi
        return mean

    def PmfVar(pmf):
        variance = 0
        for xi in (pmf.Values()):
            variance+=pmf.Prob(xi) * ((xi-PmfMean(pmf))**2)
        return variance
    
    print PmfMean(Pmf.MakePmfFromList([1,1,3,4,4]))
    print PmfVar(Pmf.MakePmfFromList([1,1,3,4,4]))
