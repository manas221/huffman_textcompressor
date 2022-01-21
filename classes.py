import heapq
import os


class Hnode:
    """
    Class for the nodes of the huffman tree and their properties
    """

    def __init__(self, char, freq):
        # basic characteristics of a huffman node
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """
        basically overload the less than operation
        since all nodes would definitely have a frequency ,we use tha
        :param other: the other object of Hnode class
        :return:
        """
        return self.freq < other.freq

    def __eq__(self, other):
        """
        if the other object is of None type or not an instance of Hnode return False else
        compare their frequency
        :param other:
        :return:
        """
        if other is None or not isinstance(other, Hnode):
            return False
        else:
            return self.freq == other.freq


class HuffmanTree:
    def __init__(self, path):
        self.path = path
        self.frequency_map = {}
        self.codes = {}
        self.tree = []

    def generate_map(self):
        # generate frequency map and save
        with open(self.path, 'r') as file:
            for line in file.readlines():
                line.rstrip()
                for char in line:
                    if char not in self.frequency_map:
                        self.frequency_map[char] = 0
                    self.frequency_map[char] += 1
        # return self.frequency_map

    def display_map(self):
        if len(self.frequency_map) < 1:
            print("Map is empty!!")
        else:
            for key, values in self.frequency_map.items():
                print(key, ' : ', values)

    def insertnodes(self):
        """
        builds the huffman tree using the heapq module
        why heapq ? because it allows to maintain a list in which first element is always the smallest.
        https://docs.python.org/3/library/heapq.html
        :return:
        """
        for char in self.frequency_map:
            node = Hnode(char, self.frequency_map[char])
            heapq.heappush(self.tree, node)

    def build(self):
        """
        Algorithm :
        Repeat below while there are more than 1 element in the list
        1. Pop two smallest nodes from the list
        2. Merge them and push them in the same list again
        3. Sort the list again
        """
        while len(self.tree) > 1:
            n1 = heapq.heappop(self.tree)
            n2 = heapq.heappop(self.tree)

            merged_node = Hnode(None, n1.freq + n2.freq)
            merged_node.left = n1
            merged_node.right = n2

            heapq.heappush(self.tree, merged_node)

    def recursive_code_generation(self, node: object, current_code):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code

        self.recursive_code_generation(node.left, current_code + '0')
        self.recursive_code_generation(node.right, current_code + '1')

    def generate_huffman_codes(self):
        """
        algorithm:
        1. build the tree by calling all the functions
        :return: dictionary with keys = characters and values = huffman tree codes
        """

        self.generate_map()  # generate the frequency map
        self.insertnodes()  # fill the node lists
        self.build()  # build the huffman tree

        root = heapq.heappop(self.tree)
        self.recursive_code_generation(root, "")

        filename, _ = os.path.splitext(self.path)
        newfilename = filename + "_huffmancodes" + ".txt"
        with open(newfilename, 'w') as file:
            for key, values in self.codes.items():
                file.write(f"{repr(key)} : {values}\n")
