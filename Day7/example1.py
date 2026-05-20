class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []
        
    def __str__(self, level = 0):
        ret = " " * level * 4 + repr(self.data) + "\n"
        for ch in self.child:
            ret += ch.__str__(level + 1)
        return ret

    def addChild(self, object):
        self.child.append(object)
        print("Tree node added")
        
rootNode = Tree("Drinks")
Hot = Tree("Hot")
Cold = Tree("Cold")

rootNode.addChild(Hot)    
rootNode.addChild(Cold)

print(rootNode)
        