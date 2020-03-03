import asyncio

async def work(uid, directory):
	if	directory.path.exists("PlayerData/Nuggets/{}.nuggets".format(uid)):
		read = open("PlayerData/Nuggets/{}.nuggets".format(uid), "rt")
		sum = read.read()
		read.close()
		
		await asyncio.sleep(300)
		write = open("PlayerData/Nuggets/{}.nuggets".format(uid), "wt")
		add = int(sum) + 15
		plus = write.write(str(add))
		write.close()
		
	else:
		write = open("PlayerData/Nuggets/{}.nuggets".format(uid), "wt")
		sum = write.write("0")
		write.close()
		
		read = open("PlayerData/Nuggets/{}.nuggets".format(uid), "rt")
		sum = read.read()
		add = int(sum) + 15
		read.close()
		
		await asyncio.sleep(300)
		write = open("PlayerData/Nuggets/{}.nuggets".format(uid), "wt")
		sum = write.write(str(add))
		write.close()
	
async def bal(mssg):
	try:
		bal = open("PlayerData/Nuggets/{}.nuggets".format(mssg.author.id), "rt")
		await mssg.channel.send("You have " + bal.read())
	except:
		write = open("PlayerData/Nuggets/{}.nuggets".format(mssg.author.id), "wt")
		sum = write.write("0")
		write.close()
		
		bal = open("PlayerData/Nuggets/{}.nuggets".format(mssg.author.id), "rt")
		await mssg.channel.send("`Taco's:`" + bal.read())
		bal.close()
