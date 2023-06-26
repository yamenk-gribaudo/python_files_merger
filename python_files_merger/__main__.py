import merger
import sys

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)  # Remove this file as arg
    merged_string = merger.merge(args)
    file = open("output.py", "w")
    file.write(merged_string)
    file.close()
