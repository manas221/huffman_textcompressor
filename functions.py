from classes import HuffmanTree
import os


def compressor(path):
    h = HuffmanTree(path)

    # initialize all codes and saves a .txt of the same
    h.generate_huffman_codes()

    filename, _ = os.path.splitext(path)
    newfilename = filename + '_compressed' + '.bin'
    with open(newfilename, 'wb') as output, open(path, 'r') as input:
        string = ''
        for line in input:
            line.rstrip()
            for char in line:
                string += h.codes[char]
                if len(string) > 8:
                    # convert the first 8 parts of string to binary
                    b_part = string[0:8]
                    b = bytearray()
                    b.append(int(b_part, 2))
                    # insert that binary into output
                    output.write(bytes(b))
                    # change string to string - first 8 parts
                    string = string[8:]