from SAIS import makeSuffixArray

class BWT:

    def transform(self, text):
        text += "\0"
        length = len(text)

        # sorted suffix array
        suffix_arr = makeSuffixArray(bytearray(text, 'utf-8'))[1:]

        # create transform
        bwt = ''.join([text[suffix_arr[i] - 1] for i in range(length)])

        return bwt

    def inverse_transform(self, transformed_text):
        length = len(transformed_text)
        # calculate histogram of characters
        hist = {}
        for ch in transformed_text:
            hist[ch] = hist.get(ch, 0) + 1

        chs = sorted(hist.keys())
        sorted_text = "".join([ch*hist[ch] for ch in chs])

        start = {}
        for i in range(len(chs)):
            ch = chs[i]
            if i == 0:
                start[ch] = 0
            else:
                start[ch] = start[chs[i-1]] + hist[chs[i-1]]

        # create map between transformed text and sorted text
        map = [0]*length
        transform_count = {}
        start_index = 0
        for i in range(length):
            ch = transformed_text[i]
            if ch == '\0':
                start_index = i
            map[i] = start[ch] + transform_count.get(ch,0)
            transform_count[ch] = 1+ transform_count.get(ch, 0)

        # use map to get the text (in reverse order)
        text = ""
        current = start_index
        for i in range(length):
            current = map[current]
            text += transformed_text[current]

        return text[::-1][1:]


