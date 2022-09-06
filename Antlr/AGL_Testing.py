"""
Created on Wed May  4 10:37:01 2022

@author: JuneethKumar Meka

Project Name : Attributed Graph Grammar Benchmark Development
"""

#Modules
#-----------------------------------------------------------------------------#
from AGL import AGL2GGX
from AGL import GGX2Verilog

#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#

"""
AGL parsing 

"""
AGLVal  = AGL2GGX("./AGL/LevelGenerator.txt")
# AGLVal  = AGL2GGX("./AGL/Memory_V2.txt")
AGLVal()
# print(AGLVal.getPortOder())

"""
Need to add the loadGGX file 

"""



# GGX2Verilog("Benchmark_testing100_out.ggx","gfg.v",AGLVal.getPortOder())
# graph = g1.getGraph()
# Networkx2Verilog(graph, "gfg", "gfg.v",not_change_enable=False)
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#

