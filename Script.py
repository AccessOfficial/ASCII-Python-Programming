import os, time

os.system('cls')

# Use TXTFile List Maker for list or manually add each txt file in list
filenames = []
frames=[]

for name in filenames:
	with open(name, "r", encoding="utf8") as f:
			frames.append(f.readlines())

for frame in frames:
	print("".join(frame))
	time.sleep(1)
	os.system("cls")

