import argparse
from .merger import merge

SUCCESS = '\033[32m'
ENDC = '\033[0m'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('args', type=str, nargs="*")
    args = parser.parse_args()

    merged_string = merge(args.args)

    if merged_string != "":
        output_file = args.output if args.output is not None else "output.py"
        with open(output_file, "w", encoding='UTF-8') as file:
            file.write(merged_string)
            file.close()
            print("\n" + SUCCESS + "Merged!!!" + ENDC)
            print(SUCCESS + "Output was saved in " + output_file + ENDC)
