INPUT = "2018-d8.txt"
numbers = list(map(int, open(INPUT).read().split(' ')))

nodes = []

def process(nodes, sumMetadata):
  childCount, metaCount, nodes = nodes[0], nodes[1], nodes[2:]
  childValues = []
  for _ in range(childCount):
    nodes, sumMetadata, nodeValue = process(nodes, sumMetadata)
    childValues.append(nodeValue)

  nodeValue = 0
  for i in range(metaCount):
    sumMetadata += nodes[i]
    if childCount == 0: 
      nodeValue += nodes[i]
    elif nodes[i] - 1 in range(childCount):
      nodeValue += childValues[nodes[i] - 1]

  return nodes[metaCount:], sumMetadata, nodeValue

nodes, sumMetadata, nodeValue = process(numbers, 0)
print(f"part 1: {sumMetadata}")
print(f"part 2: {nodeValue}")