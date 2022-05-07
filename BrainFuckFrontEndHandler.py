import runBf
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-e", "--inFile", required=True,
    help="inFile")
args = vars(ap.parse_args())
runBf.BulidProgFunctions.RunFile(args["inFile"])
