#! usr/bin/python3

class Graph:
    def __init__(self):
        self.nodes = {}

    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)
        
    def addNode(self, listForm):
        name = listForm[0]
        rules = listForm[1]

        node = None
        if name in self.nodes:
            node = self.nodes[name]
        else:
            node = Node()
            self.nodes.update({name:node})
            
        for rule in rules:
            self.applyRule(rule, name)
            
    def applyRule(self, rule, node):
        if rule == 'no other':
            return
        
        firstSpace = rule.find(' ')
        target = rule[firstSpace + 1:]
        modifier = int(rule[:firstSpace])

        if target not in self.nodes:
            self.addNode([target, []])
        self.nodes[node].addChild(target, modifier)
        self.nodes[target].addParent(node)
            
class Node:
    def __init__(self):
        self.children = {}
        self.parents = set()
                    
    def addChild(self, name, modifier):
        self.children.update({name:modifier})

    def addParent(self, name):
        self.parents.update([name])

def interpretRules(filename):
    plaintextRules = openfile(filename)
    formattedRules = organize(plaintextRules)
    return formattedRules

def openfile(filename):
    with open(filename) as f:
        rules = [line.strip() for line in f]
        return rules

def organize(plaintextRules):
    formattedRules = []
    
    for line in plaintextRules:
        line = line.replace(' bags', '')
        line = line.replace(' bag', '')
        line = line.replace('.', '')
        
        name, roughrules = line.split(' contain ')
        rules = [x.strip() for x in roughrules.split(',')]

        formattedRules.append([name, rules])

    return formattedRules

def findAllChildren(graph, name):
    node = graph.nodes[name]
    count = 1
    
    for child in node.children:
        childName = child
        modifier = node.children[childName]
        
        count += (modifier * findAllChildren(graph, childName))

    return count
        
MY_BAG = 'shiny gold'

rules = interpretRules('input7.txt')
ruleGraph = Graph()
ruleGraph.addNodes(rules)
numRequiredBags = findAllChildren(ruleGraph, MY_BAG) - 1
print(numRequiredBags)


