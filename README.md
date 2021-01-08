# Steganography
The goal of this assignment is to produce a self-contained tool in Python that can be used for covertmessaging. The tool should be able to “hide” ASCII text inside PNG files.

**1. Execution**

Write Mode 

```console
$  python pngHidden.py -w New_PNG.png                               
``` 
- You need to add the arguments if you are not specified after that 

$ Please enter your Image path !: test.png
$ Please enter your Text !: hello guys !!

```console
$  python pngHidden.py -w New_PNG.png -f test.png    
``` 
- If you are not specified the text the programme add the default text 

```console
$  python pngHidden.py -w New_PNG.png -f test.png -t "text hidden"   
``` 
- Encoded the text into png file 
 
 
Option 

- -W : Mode wirte 
- -f : The image file
- -t : The text


Read Mode

```console
$  python pngHidden.py New_PNG.png   
```
- Decoded the text hidden in the png file you need to specified the new image file  
