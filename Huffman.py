import heapq
from collections import defaultdict

# Node class for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for heapq
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(frequencies):
    # Create a min-heap with initial nodes
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    # Build the Huffman Tree
    while len(heap) > 1:
        # Remove the two nodes of lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node to the heap
        heapq.heappush(heap, merged)
    
    # The remaining node is the root of the Huffman Tree
    return heap[0]

# Function to generate Huffman codes
def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return

    # If this is a leaf node, it contains a character
    if root.char is not None:
        codes[root.char] = current_code
        return

    # Traverse the left and right children
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

# Function to calculate frequency of each character in the input string
def calculate_frequencies(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1
    return frequencies

# Main function to encode text using Huffman's coding algorithm
def huffman_encoding(text):
    # Calculate frequency of each character
    frequencies = calculate_frequencies(text)
    
    # Build the Huffman Tree
    huffman_tree = build_huffman_tree(frequencies)
    
    # Generate Huffman codes for each character
    huffman_codes = generate_huffman_codes(huffman_tree)
    
    # Encode the text using the generated Huffman codes
    encoded_text = ''.join(huffman_codes[char] for char in text)
    
    return encoded_text, huffman_codes

# Function to decode the encoded text using Huffman codes
def huffman_decoding(encoded_text, huffman_codes):
    # Reverse the Huffman codes to decode
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in reverse_codes:
            decoded_text += reverse_codes[code]
            code = ""
    
    return decoded_text

# Test the Huffman's coding implementation
if __name__ == "__main__":
    text = input("Enter the text to encode: ")
    
    # Encode the text
    encoded_text, huffman_codes = huffman_encoding(text)
    print("Huffman Codes:", huffman_codes)
    print("Encoded Text:", encoded_text)
    
    # Decode the text
    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print("Decoded Text:", decoded_text)
