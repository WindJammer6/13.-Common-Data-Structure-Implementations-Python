class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None              

    def add_child_node(self, child_node_data):
        child_node_data.parent = self
        return self.children.append(child_node_data)

    def get_level_of_node(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_general_tree(self):
        number_of_spaces = ' ' * self.get_level_of_node() * 3
        prefix = number_of_spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_general_tree()

def build_electronics_tree():
    root_node = GeneralTreeNode("Electronics")

    laptop = GeneralTreeNode("Laptop")
    laptop.add_child_node(GeneralTreeNode("Macbook"))
    laptop.add_child_node(GeneralTreeNode("Microsoft Surface"))
    laptop.add_child_node(GeneralTreeNode("Thinkpad"))

    cellphone = GeneralTreeNode("Cell Phone")
    cellphone.add_child_node(GeneralTreeNode("iPhone"))
    cellphone.add_child_node(GeneralTreeNode("Google Pixel"))
    cellphone.add_child_node(GeneralTreeNode("Vivo"))

    television = GeneralTreeNode("Television")
    television.add_child_node(GeneralTreeNode("Samsung"))
    television.add_child_node(GeneralTreeNode("LG"))

    root_node.add_child_node(laptop)
    root_node.add_child_node(cellphone)
    root_node.add_child_node(television)

    return root_node

        
if __name__ == '__main__':
    electronics_general_tree = build_electronics_tree()

    print(electronics_general_tree.get_level_of_node())

    electronics_general_tree.print_general_tree()
