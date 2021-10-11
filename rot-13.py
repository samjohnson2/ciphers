from string import ascii_letters


def rot13(message):
    displaced_letters = (
        ascii_letters[13:26]
        + ascii_letters[:13]
        + ascii_letters[39:]
        + ascii_letters[26:39]
    )
  
    table = str.maketrans(ascii_letters, displaced_letters)
    return message.translate(table)
  
  print(rot13("Hello, world!"))
