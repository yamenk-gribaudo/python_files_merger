import merger
import argparse

SUCCESS = '\033[32m'
ENDC = '\033[0m'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('args',type=str, nargs="*")
    args = parser.parse_args()

    merged_string = merger.merge(args.args)

    if merged_string != "":
        output_file = args.output if args.output is not None else "output.py"
        file = open(output_file, "w")
        file.write(merged_string)
        file.close()
        print("\n" + SUCCESS + "Merged!!!" + ENDC)
        print(SUCCESS + "Output was saved in " + output_file + ENDC)

