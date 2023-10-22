def rabin_karp(text, pattern):
    prime = 101
    text_length = len(text)
    pattern_length = len(pattern)
    h = 1
    for _ in range(pattern_length - 1):
        h = (h * 256) % prime
    pattern_hash = 0
    text_hash = 0
    for i in range(pattern_length):
        pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
        text_hash = (256 * text_hash + ord(text[i])) % prime
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            # Check character by character to avoid hash collisions
            if text[i:i+pattern_length] == pattern:
                print("Pattern found at index", i)
        if i < text_length - pattern_length:
            text_hash = (256 * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % prime
            if text_hash < 0:
                text_hash += prime

# Get user input for text and pattern
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

# Call the Rabin-Karp algorithm function
rabin_karp(text, pattern)
