# Task 1
# Define the message from Vishal!
message = """
Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 

For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!
    
    xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
    
This message has an offset of 10. Can you decode it?
"""
# Print out the message
print(message)

# Task 2 
full_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_length = len(full_alphabet)

# Make a function for decoding sentence
def caesar_decode(message, offset):
  completed_new_decoded_sentence = ""
  for alphabet in message:
    if alphabet in full_alphabet:
      letter_index = full_alphabet.index(alphabet)
      previous_alphabet = full_alphabet[letter_index-offset]
    else:
      previous_alphabet = alphabet
    completed_new_decoded_sentence += previous_alphabet
  return completed_new_decoded_sentence

# Make a function for encoding sentence
def caesar_encode(message, offset):
  completed_new_encoded_sentence = ""
  for alphabet in message:
    if alphabet in full_alphabet:
      letter_index = full_alphabet.index(alphabet)
      if letter_index + offset <= alphabet_length-1:
        next_alphabet = full_alphabet[letter_index + offset]
      else:
        shift_index = (letter_index + offset) - alphabet_length - 1
        next_alphabet = full_alphabet[shift_index]
    else:
      next_alphabet = alphabet
    completed_new_encoded_sentence += next_alphabet
  return completed_new_encoded_sentence

# Recall functions to see if our program is working!
message_1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
        
message_2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

# Testing functions 
print(caesar_decode(message_1, 1))
print()
print(caesar_decode(message_2, 1))
print()
print(caesar_encode(message_1, 1))
print()
print(caesar_encode(message_2, 2))

# Task 3
# Substitute message with provided keyword
# Create function for substitution
def monoalphabetic_substitution(message, keyword):
  full_alphabet = "abcdefghijklmnopqrstuvwxyz"
  new_sentence = ""
  keyword_index = 0

  for letter in message:
      if letter in full_alphabet:
          keyword_letter = keyword[keyword_index % len(keyword)]
          keyword_index += 1
          new_sentence += keyword_letter
      else:
          new_sentence += letter

  return new_sentence

#Testing the function
message_3 = "barry is the spy"
print(monoalphabetic_substitution(message_3, "dog"))
