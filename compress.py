import argparse
import os
from compression import FileCompressor


def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Compress a text file into a binary file.")

    parser.add_argument('-i', '--input', required=True, help="Path to the input text file.")
    parser.add_argument('-o', '--output', required=True, help="Path to the output binary file.")

    return parser.parse_args()


def main():
    # Parse command-line arguments
    args = parse_arguments()

    input_file = args.input
    output_file = args.output

    # Check if input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    # Initialize the Compressor
    compressor = FileCompressor()

    # Compress the input file and write the output to a binary file
    try:
        compressor.compress(input_file, output_file)
        print(f"Compression successful! Output written to {output_file}")
    except Exception as e:
        print(f"Error during compression: {e}")


if __name__ == "__main__":
    main()
