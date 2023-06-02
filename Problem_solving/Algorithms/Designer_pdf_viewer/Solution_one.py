def designerPdfViewer(h, word):
    # Write your code here

    letters = {}
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i, j in zip(lower_case, h):
        letters[i] = j
        
    word_high = []
    for i in word:
        if i in letters:
            word_high.append(letters[i])
            
    max_height = max(word_high)
    area = len(word) * max_height
    return area
