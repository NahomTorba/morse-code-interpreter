import winsound
import time

# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def text_to_morse(text):
    text = text.upper()
    morse_code = ' '.join(morse_code_dict.get(char, '') for char in text)
    return morse_code

# Function to play Morse code sound
def sound_morse(morse_code):
    # Define durations for dot, dash, and space
    dot_duration = 100
    dash_duration = 300
    space_duration = 700


    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(1000, dot_duration)  # Dot sound
        elif symbol == '-':
            winsound.Beep(1000, dash_duration)  # Dash sound
        elif symbol == ' ':
            time.sleep(space_duration / 1000)  # Space between letters
        elif symbol == '/':
            time.sleep(space_duration / 1000)  # Space between words
        time.sleep(dot_duration / 1000)  # Space between symbols
    return "Morse code sound played."

# Input text from the user
user_input = input("Enter text to convert to Morse code: ")
morse_output = text_to_morse(user_input)

print(f"Message: {morse_output}")
print(sound_morse(morse_output))
