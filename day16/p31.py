from numpy import prod
# Abstract base class
class Packet: 
	def __init__(self,binVal,start=0):
		self.version = int(binVal[start:start+3],2)
		self.typeID = int(binVal[start+3:start+6],2)
		self.start = start
		self.end = None
		self.subPackets = []
		
class LiteralPacket(Packet):
	def __init__(self,binVal,start=0):
		Packet.__init__(self,binVal,start)
		self.literal,self.end = self.evalLiteral(binVal)

	def evalLiteral(self, binVal):
		idx = self.start + 6
		literal = []
		while True:
			literal.append(binVal[idx+1:idx+5])
			if not int(binVal[idx]): break
			idx += 5
		return int("".join(literal),2), idx+4

class OperatorPacket(Packet):
	def __init__(self,binVal,start=0):
		Packet.__init__(self,binVal,start)
		self.end = self.populateSubPackets(binVal)

	def populateSubPackets(self, binVal):
		lengthID = int(binVal[self.start+6],2)
		if lengthID:
			numSubPackets = int(binVal[self.start+7:self.start+7+11],2)
			curr = self.start+7+11
			for i in range(numSubPackets):
				subPacket, curr = parsePacket(binVal,curr)
				self.subPackets.append(subPacket)
				curr+=1
		else:
			lengthSubPackets = int(binVal[self.start+7:self.start+7+15],2)
			curr = self.start+7+15
			while curr < self.start+7+15+lengthSubPackets:
				subPacket, curr = parsePacket(binVal, curr)
				self.subPackets.append(subPacket)
				curr+= 1
		return curr-1

## UGLY RECURSION! BREAKS ENCAPSULATION
def parsePacket(binVal,start=0):
	typeID = int(binVal[start+3:start+6],2)
	if typeID == 4:
		subPacket = LiteralPacket(binVal, start)
		return subPacket, subPacket.end 
	subPacket = OperatorPacket(binVal, start)
	return subPacket, subPacket.end

def dfsPart1(packet):
	s=packet.version
	for subPacket in packet.subPackets:
		s+=dfsPart1(subPacket)
	return s
def dfsPart2(packet, operators):
	if packet.typeID == 4:
		return packet.literal
	vals = []
	for subPacket in packet.subPackets:
		vals.append(dfsPart2(subPacket, operators))
	return operators[packet.typeID](vals)

def main():
	with open("translate.txt") as t:
		translator = {}
		for line in t:
			h,_,b = line.split()
			translator[ord(h)] = b
	with open("input.txt") as f:
		hexVal = f.readline().rstrip()
		binVal = hexVal.translate(translator)

	operators = {
		0:sum,
		1:prod,
		2:min,
		3:max,
		5:lambda x: int(x[0] > x[1]),
		6:lambda x: int(x[0] < x[1]),
		7:lambda x: int(x[0] == x[1])
				}

	root,_ = parsePacket(binVal)
	print(dfsPart2(root,operators))



if __name__ == '__main__':
	main()
