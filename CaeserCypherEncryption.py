class encodingDecoding():
    """ Encoding and Decoding the Text"""
    def __init__(self):
        self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.hashing = 3
        
    def name_spliter(self, name):
        """ Spliting each character from the given words"""
        name_ls = [letter for letter in name]
        return name_ls
    
    def key_getter(self):
        """setting the Key"""
        checker = True
        while checker:
            try:
                key = int(input("Enter the Key inbetween 1 to 26 : "))
            except Exception as e:
                print('please enter number for Key')
                key = 0
                continue

            if 1 < key < 27:
                checker = False
        return key
            
    def word_convertor(self, letter, org_letter):
        """Checking the letter Uppercase or Lowercase to return the equallent word"""
        if org_letter.isupper():
            return letter.upper()
        return letter.lower()
    
    def encryption(self, words, key):
        """Encrytion takes place here"""
        encrypted_str = ''
        for letter in words:
            if letter.upper() in self.letters:
                org_letter = letter
                index_pos = self.letters.index(letter.upper())
                position = index_pos + key + self.hashing

                encrypted_str += self.word_convertor(self.letters[position % len(self.letters)], org_letter)
            else:
                encrypted_str += str(letter)
            
        return encrypted_str
    
    def decryption(self, words, key):
        """Decryption takes place here"""
        decrypted_str = ''
        for letter in words:
            if letter.upper() in self.letters:
                org_letter = letter
                index_pos = self.letters.index(letter.upper())
                position = index_pos - key - self.hashing

                decrypted_str += self.word_convertor(self.letters[position], org_letter)
            else:
                decrypted_str += str(letter)
            
        return decrypted_str
    
def main():
    """Encryption and Decryption program"""
    wanna_continue = True
    while wanna_continue:
        text = input("Encryption or Decryption: ")

        encDe = encodingDecoding()
        
        if text == 'Encryption' or text == 'enc':
            encrypt_text = encDe.name_spliter(input("Enter the text to encrypt : "))
            key = encDe.key_getter()
            text = encDe.encryption(encrypt_text, key)
            print(f'The Encrypted Text is: {text}')

                    
        if text == 'Decryption' or text == 'dec':
            decrypt_text = encDe.name_spliter(input("Enter the text to decrypt : "))
            key = encDe.key_getter()
            text = encDe.decryption(decrypt_text, key)
            print(f'The Decrypted Text is: {text}')
            
        if input("Wanna Continue Type yes : ") != 'yes' :
            wanna_continue = False
if __name__ == '__main__':
    main()
        
"""
demo: 
Encryption or Decryption: enc
Enter the text to encrypt : a Lazy dOg 1 juMps oveR Sleeping Fox Near riVer Next To lOG.
Enter the Key inbetween 1 to 26 : 3
The Encrypted Text is: d Odcb gRj 1 mxPsv ryhU Vohhslqj Ira Qhdu ulYhu Qhaw Wr oRJ.
Wanna Continue Type yes or enter: yes
Encryption or Decryption: dec
Enter the text to decrypt : d Odcb gRj 1 mxPsv ryhU Vohhslqj Ira Qhdu ulYhu Qhaw Wr oRJ.
Enter the Key inbetween 1 to 26 : 3
The Decrypted Text is: a Lazy dOg 1 juMps oveR Sleeping Fox Near riVer Next To lOG.

"""