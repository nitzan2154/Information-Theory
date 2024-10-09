import argparse
import os
from compression import FileCompressor


def parse_arguments():
    """Parses command-line arguments for decompression."""
    parser = argparse.ArgumentParser(description="Decompress a binary file into a text file.")

    parser.add_argument('-i', '--input', required=True, help="Path to the input binary file.")
    parser.add_argument('-o', '--output', required=True, help="Path to the output text file.")

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

    # Initialize the Decompressor
    compressor = FileCompressor()

    # Decompress the binary file and write the output to a text file
    try:
        compressor.decompress(input_file, output_file)
        print(f"Decompression successful! Output written to {output_file}")
    except Exception as e:
        print(f"Error during decompression: {e}")


if __name__ == "__main__":
    main()
