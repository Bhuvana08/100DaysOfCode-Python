alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text,shift_amount,direction):
  cipher_text = ""
  if direction == "decode":
    shift_amount *= -1
  for letter in text:
   
    if letter.isalpha():
       position = alphabet.index(letter)
       new_position = (position+shift_amount)%26
       cipher_text += alphabet[new_position]
    else:
      cipher_text += letter
  print(f"The {direction}d text is {cipher_text}")

import art
print(art.logo)

end_of_process = False
while not end_of_process:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))


  caesar(text=text,shift_amount=shift%26,direction = direction)
  do_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  if do_again == "no":
    end_of_process = True

