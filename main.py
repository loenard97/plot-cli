import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        prog="hdf5-cli",
        description="HDF5 file cli tool",
    )
    parser.add_argument("-i", "--input", default=None, help="input file path")
    parser.add_argument("-o", "--output", default=None, help="output file (show as window if no output specified)")
    parser.add_argument("-x", "--xlabel", default=None, help="x label")
    parser.add_argument("-y", "--ylabel", default=None, help="y label")
    parser.add_argument("--delimiter", default=" ", help="delimiter (default is ' ')")
    args = parser.parse_args()

    x_label = args.xlabel if args.xlabel is not None else "x data"
    y_label = args.ylabel if args.ylabel is not None else "y data"
    data = np.loadtxt(sys.stdin, delimiter=args.delimiter)
    print(data.shape)
    print(data.ndim)
    if data.ndim == 1:
        x_data = np.linspace(0, len(data), len(data))
        y_data = data
    elif data.ndim == 2:
        x_data, y_data = data.transpose()
    else:
        ValueError("too many inputs")

    plt.figure()
    plt.plot(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if args.output is None:
        plt.show()
    else:
        plt.savefig(args.output)


if __name__ == "__main__":
    try:
        main()
    except BaseException as err:
        eprint(err)

