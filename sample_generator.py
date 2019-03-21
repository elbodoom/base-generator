import argparse

from pathlib import Path
from progress.bar import Bar

from sampler import Sampler

def _parse_args():
    parser = argparse.ArgumentParser(description="Sample Generator.")
    parser.add_argument("--name", type=str, help="File name", required=True)
    parser.add_argument("--records", type=int, help="Record's quantity", required=True)
    parser.add_argument("--max-id", type=int, help="Maximum id", required=True)
    return parser.parse_args()

def _main(args):
    file = Path(args.name)
    sampler = Sampler(file = file, records = args.records, max_id = args.max_id)
    sampler.generate(Bar("Processing", max = args.records))

if __name__ == "__main__":
    args = _parse_args()
    _main(args)
