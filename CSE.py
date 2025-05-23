'''
question->
Coding Scheme Extractor: Your tool should extract a coding scheme abiding by Gilbert-Varshamov
bound. 
'''


import tkinter as tk
from tkinter import scrolledtext
from math import comb

# Function to calculate the maximum number of code words using Gilbert-Varshamov bound
def calculate_max_code_words(field_size, code_length, min_distance):
    
    max_code_words = field_size ** code_length / sum(comb(code_length, i) * (field_size - 1) ** i for i in range(min_distance))
    return max_code_words

# Function to generate the coding scheme
def generate_coding_scheme():
    # Retrieve user inputs
    field_size = int(field_size_entry.get())
    code_length = int(code_length_entry.get())
    min_distance = int(min_distance_entry.get())

    if(field_size<=1):
        return 0
    
    if(min_distance>code_length):
        return 0
    
    # Calculate the maximum number of code words using Gilbert-Varshamov bound
    max_code_words = calculate_max_code_words(field_size, code_length, min_distance)
    print("Maximum number of code words:", max_code_words)

    # Placeholder for generated coding scheme
    coding_scheme = []

    # Generate code words
    for i in range(field_size ** code_length):
        # Convert index i to base field_size to get the code word
        code_word = [(i // (field_size ** j)) % field_size for j in range(code_length)]
        
        # Check if the code word satisfies the minimum Hamming distance from existing code words
        valid = all(hamming_distance(code_word, cw) >= min_distance for cw in coding_scheme)
        
        # If valid, add the code word to the coding scheme
        if valid:
            coding_scheme.append(code_word)
            
            # If enough code words found, stop
            if len(coding_scheme) >= max_code_words:
                break

    # Display coding scheme in the text area
    output_text.delete(1.0, tk.END)
    for code_word in coding_scheme:
        output_text.insert(tk.END, ' '.join(map(str, code_word)) + '\n')

# Function to calculate the Hamming distance between two code words  
def hamming_distance(a, b):
    hd = 0
    for i in range(len(a)):
        if a[i] != b[i]:  
            hd += 1
    return hd

# Create the main window
root = tk.Tk()
root.title("Coding Scheme Extractor")

# Create input fields
field_size_label = tk.Label(root, text="Field Size (Fq):")
field_size_label.grid(row=0, column=0)
field_size_entry = tk.Entry(root)
field_size_entry.grid(row=0, column=1)

code_length_label = tk.Label(root, text="Code Length:")
code_length_label.grid(row=1, column=0)
code_length_entry = tk.Entry(root)
code_length_entry.grid(row=1, column=1)

min_distance_label = tk.Label(root, text="Minimum Hamming Distance:")
min_distance_label.grid(row=2, column=0)
min_distance_entry = tk.Entry(root)
min_distance_entry.grid(row=2, column=1)

# Create button to generate coding scheme
generate_button = tk.Button(root, text="Generate Coding Scheme", command=generate_coding_scheme)
generate_button.grid(row=3, column=0, columnspan=2)

# Create text area to display coding scheme
output_text = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.NONE)
output_text.grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
