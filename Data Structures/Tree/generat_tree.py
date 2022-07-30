from __future__ import print_function
from distutils.command.build import build
from logging import root
from platform import node
from tenacity import retry_never

'''General tree implementation from scratch == '''
'''                                        Electronics(root,level 0)               
                                                |
                Laptop(node,level 1)          Mobile(node,level 1)           Tv((node,level 1) )
                  |                             |                             |  
    [Mac] [Surface] [Thinkpad]         [Apple] [Samsung] [Mi]           [Samsung] [LG]
            (leaf,level 2)                  (leaf,level 2)                  (leaf,level 2)'''


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_tree_node():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("Apple"))
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Mi"))

    tv = TreeNode("Tv")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    return root

if __name__ == '__main__':
    root = build_tree_node()
    root.print_tree()
    # print(root.get_level())