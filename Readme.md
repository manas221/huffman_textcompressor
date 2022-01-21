# Text Compressor using Huffman Codes

<br></br>
Huffman coding is a lossless data compression technique .The main idea behind the technique is to
assign the least bits to the most frequent data or character(in case of text file). This little 
implements the said technique to compress text files. It also generates another text file containing
the huffman codes for the same text files.


# Installation

```
$ git clone --depth 1 https://github.com/manas221/huffman_textcompressor.git
$ cd huffman_textcompressor.git
$ python3 -m venv env
$ source ./env/bin/activate
$ pip3 install -r requirements.txt
```

# Usage

**Make sure you run `source ./env/bin/activate` every time you want to run the
program.**

Run main:
<br></br>
There is a sample file called SherlockHolmes.txt in the "resources" directory whose
path is hardcoded as a path variable in main.py. To run program for a different text file
,change the path to desired file's path.

```

$ ./main.py
```



# Sources


https://youtu.be/JCOph23TQTY

https://en.wikipedia.org/wiki/Huffman_coding
