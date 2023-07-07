def designerPdfViewer(h, word):
    # Write your code here
    
    alphabets = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
    'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    
    word_position = []
    word_length = 0
    word_heights = []
    
    for a in word:
        word_position.append(alphabets[a])
        word_length += 1
        
    for i in word_position:
        word_heights.append(h[i])
        
    return max(word_heights) * word_length
