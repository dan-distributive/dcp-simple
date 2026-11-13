from getpass import getpass
import json
import dcp
dcp.init()

# input set (x)
inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# work function arguments (a, b, c)
args = [98, 99, 100]

# work function
def my_function(x, a, b, c):
    dcp.progress()
    import numpy as np
    result = np.sqrt(x * a * b - c)
    return result

# DCP job - maps work_function and arguments to each input in the input set
job = dcp.compute_for(inputs, my_function, args)

# Job config
job.public.name = 'Simple demo'
job.modules = ['numpy']
job.computeGroups = [{'attachKey': 'tensparrows'}]
for g in job.computeGroups:
    if g.get("attachKey") != "global":
        g["attachSecret"] = getpass(f"Enter attach secret for compute group '{g['attachKey']}': ")

# Event listeners
job.on('accepted', lambda _: print(f"Job ID: {job.id}\nAwaiting results..."))
job.on('error',    lambda err: print(json.dumps(err, indent=4).replace('\\n', '\n')))
job.on('nofunds',  lambda nof: print(json.dumps(nof, indent=4).replace('\\n', '\n')))
job.on('result',   lambda res: print(json.dumps(res, indent=4).replace('\\n', '\n')))

# Job execution
job.exec()
results = job.wait()

# Result post-processing
print(results)