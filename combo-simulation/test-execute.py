import subprocess
import time
import os
import signal

def execSubProc(args):
    start_time = time.time()
    subproc = subprocess.Popen(args)
    subproc.wait()
    end_time = time.time()
    execTime = end_time-start_time
    print(f"Command        : {args}")
    print(f"Execution time : {execTime}")
    print("--------------------------------------------------------------------")

pyfiles = ["test-cases-generator.py", "solo-mapping.py", "simple-combo-mapping.py", "maxima-combo-mapping.py"]
inp = ""

print("SFC-PHY Mapping Problem | Simulation")
print("--------------------------------------------------------------------")
for f in pyfiles:
    execSubProc(args=["python", f])