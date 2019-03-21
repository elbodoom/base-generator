import argparse

from pathlib import Path
from progress.bar import Bar

from line_generator import LineGenerator
from file_writer import FileWriter

def _parse_args():
    parser = argparse.ArgumentParser(description="Base Generator.")
    parser.add_argument("--name", type=str, help="File name", required=True)
    parser.add_argument("--records", type=int, help="Record's quantity", required=True)
    parser.add_argument("--line-size", type=int, help="Line size (except id)", required=True)
    return parser.parse_args()

def _main(args):
    file = Path(args.name)
    line_generator = LineGenerator(size = args.line_size)
    file_writer = FileWriter(file = file, records = args.records, line_generator = line_generator)
    file_writer.write(Bar("Processing", max = args.records))

if __name__ == "__main__":
    args = _parse_args()
    _main(args)
