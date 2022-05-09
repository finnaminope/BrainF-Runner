import sys
import getch
import random
import click
import warnings
import pickle

class BulidProgFunctions:
  def loadSyntaxFile(inputFile=""):
    try:
      fd = open(inputFile, 'rb')
      dataset = pickle.load(fd)
      return dataset
    except FileNotFoundError:
      syntaxBase = {"LC":"}"}
      fd = open(inputFile, 'wb')
      pickle.dump(syntaxBase, fd)
      warnings.warn("Syntax File Not Found. This May Cause Some Programs To Not Run Correctly")

  def RunFile(FileName, CBFASSF="Unnamed_syntax"):
    fd = open(FileName, 'r')
    evaluate(fd.read(), BulidProgFunctions.loadSyntaxFile(CBFASSF))

  def __init__(self):
    print("you are an idiot! hahahahahahaha hahahahahaha")
  
  def __call__(self):
    while True:
      print("you are an idiot! hahahahahahaha hahahahahaha")

def evaluate(code, Syntax):
  code     = list(code)
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == ">":
      cellptr += 1
      if cellptr == len(cells) and not len(cells) == 255: print("lol")#cells.append(0) #set to a number higher than 0 to break all brainf programs

    if command == "<":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "+":
      try:
        cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0
      except IndexError:
        print("runBfError: fatal: incError: IndexError: Please report this bug to the Devloper.")
        print("codePointer:")
        print(codeptr)
        print("cellPointer:")
        print(cellptr)
        print("")
        
        

    if command == "-":
      try:
        cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255
      except IndexError:
        print("runBfError: fatal: deincError: IndexError: Please report this bug to the Devloper.")
        print("codePointer:")
        print(codeptr)
        print("cellPointer:")
        print(cellptr)
        print("")

    if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    
    if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    
    if "L" in command:
      codeptr += 2
      #time.sleep()
      wsc = ""
      while not command == Syntax['LC']:
        codeptr += 1
        command = code[codeptr]
        wsc = wsc + command
      wsc = ''.join((filter(lambda x: x not in ['}'], wsc)))
      print(wsc)
      
    if command == "C": click.clear()
    if command == "M": 
      cells.clear()
      cells.append(0)
    if command == ".": 
      sys.stdout.write(chr(cells[cellptr]))
      #print("")
      #print(cells)
    if command == ",": cells[cellptr] = ord(getch.getch())
    codeptr += 1
  print("")
  print(cells)
class _Outdated:
  def _Cleanup(code):
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-', 'C', 'M', "L", "{", "}"], code))



def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "[": temp_bracestack.append(position)
    if command == "]":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap


def main():
  if len(sys.argv) == 2: BulidProgFunctions.RunFile(sys.argv[1])
  else: 
    print("Usage:", sys.argv[0], "filename")


if __name__ == "__main__": main()

