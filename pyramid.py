
# In this exercise, you will develop a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string.
# Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).
# Your function must be able to process an input file with the following format:
# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you
# In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively, like so:
#   1
#  2 3
# 4 5 6
# The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:
# 1: I
# 3: love
# 6: computers
# and your function should return the string "I love computers".

def decode(message_file):

    with open(message_file, 'r') as file:
        lines = file.readlines()

    message_dict = {}

    for line in lines:
        num, word = line.strip().split()
        num = int(num)
        message_dict[num] = word

    pyramid = []
    current_level = []
    level_size = 1
    for key in sorted(message_dict.keys()):
        current_level.append(message_dict[key])
        if len(current_level) == level_size:  
            pyramid.append(current_level)
            current_level = []  
            level_size += 1  
    print(pyramid)

    decoded_words = []
    for level in pyramid:
        decoded_words.append(level[-1])

    return ' '.join(decoded_words)


print(decode("message.txt"))  # Output:  I love computers
