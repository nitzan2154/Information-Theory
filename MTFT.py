class MTF:
    def __init__(self, symbols=range(128)):
        # Initialize a list of symbols
        self.legal_symbols = list(symbols)

    def transform(self, text):
        """
        Move to Front Encoding.
        """
        symbol_list = self.legal_symbols[:]
        output_array = []

        for c in text:
            index = symbol_list.index(ord(c))  # Find the index of the character
            output_array.append(index)         # Append index to output array
            symbol_list.insert(0, symbol_list.pop(index))  # Move symbol to front

        return ''.join(chr(i) for i in output_array)

    def inverse_transform(self, transformed_text):
        """
        Move to Front Decoding
        """
        symbol_list = self.legal_symbols[:]
        result = []

        for c in transformed_text:
            index = ord(c)
            symbol = symbol_list[index]
            result.append(chr(symbol))  # Add the decoded symbol to the result
            symbol_list.insert(0, symbol_list.pop(index))  # Move symbol to front

        return ''.join(result)


def main():
    text_now = "the quick brown fox jumps over the lazy dog"

    print(f"Input text: {text_now}")
    print("Move to Front Transform: ", end='')

    # Computes Move to Front transform of given text
    mtf = MTF()
    transformed_text_now = mtf.transform(text_now)

    print(transformed_text_now)
    inverse_text_now = mtf.inverse_transform(transformed_text_now)
    print(inverse_text_now)


if __name__ == "__main__":
    main()
