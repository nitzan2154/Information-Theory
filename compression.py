from MTFT import MTF
from RLET import RLE
from BWT import BWT
from LZWT import LZW
from bitarray import bitarray
from time import time


class TextCompressor:

    def __init__(self):
        self.bwt = BWT()
        self.mtf = MTF()
        self.rle = RLE()
        self.lzw = LZW()

    def compress(self, text):
        """
        Compresses text to a string of bits
        :param text:
        :return compressed_text:
        """
        # Borrows-Wheeler
        print("Performing Borrows-Wheeler transform...")
        bw_text = self.bwt.transform(text)

        # Move-to-Front
        print("Performing Move-to-Front transform...")
        mtf_text = self.mtf.transform(bw_text)

        # Lempel-Ziv-Welch Encoding
        print("Performing Lempel-Ziv-Welch encoding...")
        compressed_text = self.lzw.transform(mtf_text)

        return compressed_text

    def expand(self, compressed):
        """
        Expands a string of bits back to text
        :param compressed:
        :return text:
        """
        # Lempel-Ziv-Welch Decoding
        print("Inverting Lempel-Ziv-Welch encoding...")
        lzw_expanded = self.lzw.inverse_transform(compressed)

        # Move-to-Front
        print("Inverting Move-to-Front transform...")
        mtf_expanded = self.mtf.inverse_transform(lzw_expanded)

        # Borrows-Wheeler
        print("Inverting Borrows-Wheeler transform...")
        text = self.bwt.inverse_transform(mtf_expanded)

        return text


class FileCompressor:
    def __init__(self):
        self.compressor = TextCompressor()

    def read_text_file(self, file_path):
        """Reads the content of a text file and returns it as a string."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write_text_file(self, file_path, text):
        """Writes a string to a text file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

    def write_binary_file(self, file_path, bit_string):
        """Writes a bit string to a binary file using bitarray."""
        # Convert string of 0s and 1s to bitarray
        bit_arr = bitarray(bit_string)
        # Write the bitarray to a binary file
        with open(file_path, 'wb') as binary_file:
            bit_arr.tofile(binary_file)

    def read_binary_file(self, file_path):
        """Reads a binary file and returns the bit string."""
        bit_arr = bitarray()
        with open(file_path, 'rb') as binary_file:
            bit_arr.fromfile(binary_file)
        return bit_arr.to01()  # Convert the bitarray to a string of 0s and 1s

    def compress(self, input_text_file, output_binary_file):
        """Reads text, compresses it, and saves the result as binary."""
        print(f"Compressing file {input_text_file}...")
        start_time = time()

        # Step 1: Read the text file
        text = self.read_text_file(input_text_file)

        # Step 2: Compress the text using the provided compression function
        compressed_bit_string = self.compressor.compress(text)

        # Step 3: Write the compressed bit string to the binary file
        self.write_binary_file(output_binary_file, compressed_bit_string)

        end_time = time()
        total = end_time - start_time
        print(f"Total time: {total} seconds.")

    def decompress(self, input_binary_file, output_text_file):
        """Reads a binary file, decompresses it, and saves the result as a text file."""
        print(f"Decompressing file {input_binary_file}...")
        start_time = time()

        # Step 1: Read the binary file
        compressed_bit_string = self.read_binary_file(input_binary_file)

        # Step 2: Decompress the bit string using the provided decompression function
        decompressed_text = self.compressor.expand(compressed_bit_string)

        # Step 3: Write the decompressed text to a text file
        self.write_text_file(output_text_file, decompressed_text)

        end_time = time()
        total = end_time - start_time
        print(f"Total time: {total} seconds.")


def main():
    input_text_file = "large/bible.txt"
    output_text_file = "bible_result.txt"
    output_file = "compressed_bible.bin"
    comp = FileCompressor()
    start_time = time()
    comp.compress(input_text_file, output_file)
    end_time = time()
    total = end_time - start_time
    print("total time (sec): ", total)
    # start_time = time()
    # comp.decompress(output_file, output_text_file)
    # end_time = time()
    # total = end_time - start_time
    # print("total time (sec): ", total)

if __name__ == "__main__":
    main()
