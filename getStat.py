import psutil
import json

class MyServer(object):
	def __init__(self, serverName):
		self.name = serverName
		self.cpu = 0

cpuStats = psutil.cpu_times_percent(percpu=True, interval=1)
#cpuStats = [json.dumps(stats._asdict()) for stats in cpuStats]

memStats = psutil.virtual_memory()
memStatsList = dict()
cpuStatsList = dict()


for stats in cpuStats:
	for name in stats._fields:
		value = getattr(stats, name)
		cpuStatsList[name] = value

for name in memStats._fields:
	value = getattr(memStats, name)
	if name != 'percent':
		# might change this later, convert all to Gb for now
		convert = 1 << 30
		value = float(value) / convert
		value = round(value, 2)
		#print(value)
	memStatsList[name.capitalize()] = value

#print(memStatsList)
#memStats = json.dumps(memStatsList)
memStats = memStatsList
cpuStats = cpuStatsList

data = {'cpuStats': cpuStats , 'memStats' : memStats}

#print(cpuStats)
#print(memStats)

with open('data.json', 'w') as f:
     json.dump(data, f)
