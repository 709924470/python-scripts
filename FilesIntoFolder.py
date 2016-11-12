import os,shutil,sys,time
#import pdb

dir = os.getcwd() + '\\'
scname = sys.argv[0].split("\\")[len(sys.argv[0].split("\\")) - 1]
lst1 = os.listdir(dir)
lst1.remove(scname)
for x9 in lst1:
	if os.path.isdir(x9):
		lst1.remove(x9);
dict = {}
t = 0
m = 5

def log_(s,l=0):
	lvl = ''
	if(l==0):
		lvl = ''
	if(l==1):
		lvl = "\033[0;31m *Critical :"
	if(l==-1):
		lvl = "\033[0;32m *Info :"
	print(time.strftime("[%H:%M:%S] ")+lvl+s+"\033[0m") 

log_("Thanks for downloading & using File combiner Created by twitter @709924470_",-1)
log_("Now initialing......")
if len(lst1) == 0:
	log_("Do not put this script in to a empty folder OR a folder is full of subfolders!",1)
	exit()
while t < m:
	vstr = lst1[t][0:5]
	svstr = ''
	pass
	keys = [x for x in lst1 if vstr in x]
	t = t + 1
	m = len(lst1)
	if len(keys) == 1:
		continue
	key1 = keys[0]
	key2 = keys[1]
	for x0 in range(0,len(key1)):
		if key1[:x0] == key2[:x0] and key1[x0] != "_":
			svstr = key1[:x0+1]
		else:
			break
	keys = [x for x in lst1 if svstr in x]
	log_(""+str(len(keys))+" files will be moved to a subfolder named '"+svstr+"'")
	dict[svstr] = keys
	for x0 in keys:
		lst1.remove(x0);
	m = len(lst1)

if len(dict) == 0:
	pass
else:
	for k in dict:
		ndir = dir + k + "\\"
		if os.path.exists(ndir) is False:
			os.mkdir(ndir)
			log_("Created forder :"+ndir,-1)
			for f in dict[k]:
				shutil.move(dir + f, ndir + f)
				log_("Moved '"+dir+f+"' to '"+ndir+f+"'",-1)
		else:
			for f in dict[k]:
				shutil.move(dir + f, ndir + f)
				log_("Moved '"+dir+f+"' to '"+ndir+f+"'",-1)

if len(lst1) == 0:
	log_("Work done!",1)
	exit()

t = 0

while t < m:
	vstr = ''
	try:
		vstr = lst1[t]
		vstr = vstr[int(len(vstr)*0.5):int(len(vstr)*0.75)]
	except:
		vstr = lst1[t]
		vstr = os.path.splitext(vstr)[0]
		vstr = vstr[3:]
	svstr = ''
	pass
	keys = [x for x in lst1 if vstr in x]
	m = len(lst1)
	t += 1
	if len(keys) == 1:
		continue
	key1 = os.path.splitext(keys[0])[0]
	key2 = os.path.splitext(keys[1])[0]
	for x0 in range(0,len(key1)):
		state = 0
		if key1[x0:] == key2[x0:]:
			state += 1
			svstr += key1[x0]
		else:
			if state != 0:
				break
	keys = [x for x in lst1 if svstr in x]
	dict[svstr] = keys
	log_(""+str(len(keys))+" files will be moved to a subfolder named '"+svstr+"'")
	for x0 in keys:
		lst1.remove(x0);
	m = len(lst1)

if len(dict) == 0:
	pass
for k in dict:
		ndir = dir + k + "\\"
		if os.path.exists(ndir) is False:
			os.mkdir(ndir)
			log_("Created forder :"+ndir,-1)
			for f in dict[k]:
				shutil.move(dir + f, ndir + f)
				log_("Moved '"+dir+f+"' to '"+ndir+f+"'",-1)
		else:
			for f in dict[k]:
				shutil.move(dir + f, ndir + f)
				log_("Moved '"+dir+f+"' to '"+ndir+f+"'",-1)

log_("Work done!",1)