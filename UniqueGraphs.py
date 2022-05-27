"""
Created on Fri May 27 12:26:11 2022

@author: JuneethKumar Meka

Project Name : Attributed Graph Grammar Benchmark Development
"""

#Modules
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
def UniqueGraphs(data):
    """data should be of type list<list<strings>>"""
    data_str = []
    final_data = []
    for eachlist in data:
        eachlist.sort()
        data_str.append("%".join(eachlist))
        data_str = list(set(data_str))
    for eachlist in data_str:
        final_data.append(eachlist.split("%"))
    return final_data
        
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
# data = [["N10","N11","N1","N7"],["N2","N3","N1","N0"],["N7","N1","N10","N11"]]
# print(UniqueGraphs(data))
#-----------------------------------------------------------------------------#

