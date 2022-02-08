import Detector
import analyser

for node in range(7):
    fanin = 2 + node
    fanout = 9 - fanin
    print("fan in = ",fanin, "fanout = ",fanout)
    #obj = Detector.Detector(9,fanin,fanout,"benchmark_verilog_code","sub_graph_directory")
obj = analyser.Analyser("JSON_9_2_7.json")