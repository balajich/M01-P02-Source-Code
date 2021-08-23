from Node import Node
from VirtualNodeMap import VirtualNodeMap

if __name__ == '__main__':
    # Creates a node first and creates a random VirtualNodeMap inside it
    virtualNodeMap = VirtualNodeMap(['node1', 'node2', 'node3', 'node4', 'node5', 'node6'], 200)

    # Creates other initial set of nodes, with the same virtual node mapping and
    # connects them with each other
    node1 = Node('node1', 200, virtualNodeMap)
    node2 = Node('node2', 200, virtualNodeMap)
    node3 = Node('node3', 200, virtualNodeMap)
    node4 = Node('node4', 200, virtualNodeMap)
    node5 = Node('node5', 200, virtualNodeMap)
    node6 = Node('node6', 200, virtualNodeMap)
