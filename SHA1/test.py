def binary_to_text(binary_string):
    text_result = ""
    
    for i in range(0, len(binary_string), 8):
        byte_chunk = binary_string[i:i+8]
        
        char_code = int(byte_chunk, 2)
        text_result += chr(char_code)
    
    return text_result
