'''
creates parent and child structure for the grocery data
'''

class Node(object):
    def __init__(self, name, id= None, url = None):
        self.name = name
        self.ID = id
        self.url = url
        self.children = []

    '''
     Appends a child nodes to the parent node
    '''
    def add_child(self, detials):
        child_found = [c for c in self.children if c.name == detials[0]]
        if not child_found:
            _child = Node(detials[0], detials[1], detials[2])
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child
        
    '''
     creates a json structre with all the details of parent and child nodes
    '''
    def as_dict(self):
        res = {}
        if self.url and self.ID:
            res = {'name': self.name, 'ID': self.ID, "url" : self.url}
        elif self.name:
            res = {'name': self.name}
        if self.name:
            res['children'] = [c.as_dict() for c in self.children]
        return res

