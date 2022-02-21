import Detector
import analyser

for i in range(3,11):
    nodes = i
    for node in range(nodes-2):
        fanin = 2 + node
        fanout = nodes - fanin
        print("fan in = ",fanin, "fanout = ",fanout)
        obj = Detector.Detector(nodes,fanin,fanout,"benchmark_verilog_code","sub_graph_directory")

#obj = analyser.Analyser("JSON_9_2_7.json")
