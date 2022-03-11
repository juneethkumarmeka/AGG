"""
Created on Sat Feb 12 13:43:53 2022

@author: JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
"""

#Modules
#-----------------------------------------------------------------------------#
import os
#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class LoadGGX:
    def __init__(self,file):
        if os.path.isfile(file):
            self.file = file 
        else:
            raise Exception("{} not found".format(file))
    
    def __call__(self):
        os.system('java -Xmx10g -XX:+UseParallelGC -Dfile.encoding=UTF-8 \
                  -classpath "AGG/bin" \
                  agg_execution.Importing {}'.format(self.file))
        
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
# LoadGGX("gfg.ggx")()
#-----------------------------------------------------------------------------#

