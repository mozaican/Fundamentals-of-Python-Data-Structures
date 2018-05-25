"""
Defines a class for profiling sort algorithms.
A Profiler object tracks the list, the number of
comparisons and exchanges and the running time. The 
Profiler can also print a trace and can create a list
of unique or duplicate numbers. 
"""

import time
import random

class Profiler():
    def test(self, function, lyst=None, size=10, unique=True, comp=True, exch=True, trace=False):

        """
        function: the algorithm being profiled
        lyst: allow calling a list
        size: the size of the list
        unique: if true, the list contains unique integers
        comp: if true, count comparisons
        exch: if true, count exchanges
        trace: if true, print the list after each exchange
        """

        self.comp = comp
        self.exch = exch
        self.trace = trace
        if lyst != None:
            self.lyst = lyst
        elif unique:
            self.lyst = range(1, size + 1)
            random.shuffle(self.lyst)
        else: 
            self.lyst = []
            for count in range(size):
                self.lyst.append(random.randint(1, size))

        self.exchCount = 0
        self.cmpCount = 0
        self.startClock()
        function(self.lyst, self)
        self.stopClock()
        print(self)


