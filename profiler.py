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




