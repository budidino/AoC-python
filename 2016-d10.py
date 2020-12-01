INPUT = "2016-d10.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

outputs = []
bots = []

def getBotWithId(botId):
    global bots
    for bot in bots:
        if bot.botId == botId:
            return bot

def getOutputWithId(outputId):
    global outputs
    for output in outputs:
        if output.outputId == outputId:
            return output
    output = Output(outputId)
    outputs.append(output)
    return output

class Output:
    outputId = 0
    values = []

    def __init__(self, outputId):
        self.outputId = outputId
        self.values = []

class Bot:
    botId = 0
    lowToBot = False
    highToBot = False
    lowTo = 0
    highTo = 0
    values = []

    def __init__(self, botId, low, high, lowBot, highBot):
        self.botId = botId
        self.lowTo = low
        self.highTo = high
        self.lowToBot = lowBot
        self.highToBot = highBot
        self.values = []

    def give(self):
        global bots, outputs
        valLow = min(self.values)
        valHigh = max(self.values)

        self.values = []

        if valLow == 17 and valHigh == 61:
            print(f"part 1: {self.botId}") # 86

        if self.lowToBot:
            lowBot = getBotWithId(self.lowTo)
            lowBot.getValue(valLow)
        else:
            output = getOutputWithId(self.lowTo)
            output.values.append(valLow)

        if self.highToBot:
            highBot = getBotWithId(self.highTo)
            highBot.getValue(valHigh)
        else:
            output = getOutputWithId(self.highTo)
            output.values.append(valHigh)

    def getValue(self, val):
        self.values.append(val)
        if len(self.values) == 2:
            self.give()

for string in strings:
    if "gives low" in string:
        splits = string.split(" ")
        botId = int(splits[1])
        low = int(splits[6])
        high = int(splits[11])
        lowBot = False
        highBot = False
        
        if splits[5] == "bot":
            lowBot = True
        if splits[10] == "bot":
            highBot = True

        newBot = Bot(botId, low, high, lowBot, highBot)
        bots.append(newBot)

for string in strings:
    if "goes to bot" in string:
        splits = string.split(" ")
        value = int(splits[1])
        toBot = int(splits[5])
        
        bot = getBotWithId(toBot)
        bot.getValue(value)

result = 1
for output in outputs:
    if output.outputId in [0, 1, 2]:
        result *= output.values[0]
    
print(f"part 2: {result}") # 22847