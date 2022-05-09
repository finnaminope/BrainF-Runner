import runBf
import argparse
import os
import gui

owner = os.environ['REPL_OWNER']
# to print, use owner



print("hello " + owner + " now running your BrainF")

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-e", "--inFile", required=False, help="inFile")
ap.add_argument("-i", required=False)
args = vars(ap.parse_args())
if "-e" in args:
  runBf.BulidProgFunctions.RunFile(args["inFile"])
else:
  gui.StartGui()
