import caesar_cipher #must match the ACTUAL filename
import transposition_cipher
import affineCipher, affineHacker
import simpleSubCipher, simpleSubHacker
import vigenereCipher, vigenereHacker, vigenereDictionaryHacker

def selection():
    user_input = input("Choose type of decryption:\n" +
                            "1. Caesar, Encrypt (ce)\n" +
                            "2. Caesar, Decrypt (cd)\n" +
                            "3. Caesar, Hack (ch)\n\n" +
                            "4. Transposition, Encrypt (te)\n" +
                            "5. Transposition, Decrypt (td)\n" +
                            "6. Transposition, Hack (th)\n\n" +
                            "7. Affine, Encrypt (ae)\n" +
                            "8. Affine, Decrypt (ad)\n" +
                            "9. Affine, Hack (ah)\n\n" +
                            "10. Substitution, Encrypt (se)\n" +
                            "11. Substitution, Decrypt (sd)\n" +
                            "12. Substitution, Hack (sh)\n\n" +
                            "13. Vigenere, Encrypt (ve)\n" +
                            "14. Vigenere, Decrypt (vd)\n" +
                            "15. Vigenere, Hack (vh)\n\n" +
                            "99. Quit\n>> ").title().strip()
    return user_input

def to_continue():
    input("Press Enter to continue>> ")

plain_text_message = "Enter plaintext for encryption:\n>> "
cipher_text_decrypt = "Enter ciphertext for decryption:\n>> "
cipher_text_hack = "Enter ciphertext to be hacked:\n>> "

print("Welcome to Mr. Schnaars' encryption program!\n")
print("Type 'Quit' to exit at any time.\n")

user_input = '' #initially user_input is just an empty string

while user_input.title().strip() != 'Quit': #as long as they don't type 'Quit'
    #instructions...
    user_input = selection()
    caesar_key = "Enter a key (must be 1-25):\n>> "
    numeric_key_error = "ValueError: key must be numeric."
    alpha_key_error = "Error: not a valid substitution key."
    
    if user_input in ['Quit', '99', 'Exit'] or user_input.startswith('Q'):
        user_input = 'Quit'
   
###############################################################################
#                               CAESAR BRANCH
################################################################################ 
    elif user_input in ['Caesar, Encrypt', 'Ce','1', '1.']:
        plain_text = input(plain_text_message).upper()
        valid = True
        while valid:
            try:
                key = int(input(caesar_key).strip())
                print(caesar_cipher.caesar_encrypt(key, plain_text))
                to_continue()
                valid = False
            except ValueError:
                print(numeric_key_error)
                continue

    elif user_input in ['Caesar, Decrypt', 'Cd', '2', '2.']:
        cipher_text = input(cipher_text_decrypt).upper()
        valid = True
        while valid:
            try:
                key = int(input(caesar_key).strip())
                print(caesar_cipher.caesar_decrypt(key, cipher_text))
                to_continue()
                valid = False
            except ValueError:
                print(numeric_key_error)
                continue

    elif user_input in ['Caesar, Hack', 'Ch', '3', '3.']:
        cipher_text = input(cipher_text_hack)
        caesar_cipher.cc_hack(cipher_text)
        to_continue()

###############################################################################
#                               TRANSPOSITION BRANCH
################################################################################        
    elif user_input in ['Transposition, Encrypt', 'Te', '4', '4.']:
        plain_text = input(plain_text_message)
        valid = True
        while valid:
            try:
                print("Enter a key between 2 and", int(len(plain_text)/2))
                key = int(input("Key>> ").strip())
                print(transposition_cipher.transposition_encrypt(key, plain_text))
                to_continue()
                valid = False
            except ValueError:
                print(numeric_key_error)
                continue

    elif user_input in ['Transposition, Decrypt', 'Td', '5', '5.']:
        cipher_text = input(cipher_text_decrypt)
        valid = True
        while valid:
            try:
                key = int(input("Enter encryption key.\n>> ").strip())
                print(transposition_cipher.transposition_decrypt(key, cipher_text))
                to_continue()
                valid = False
            except ValueError:
                print(numeric_key_error)
                continue

    elif user_input in ['Transposition, Hack', 'Th', '2', '2.']:
        cipher_text = input(cipher_text_hack)
        print(transposition_cipher.transposition_hack(cipher_text))
        to_continue()

###############################################################################
#                               AFFINE BRANCH
################################################################################        
    elif user_input in ['Affine, Encrypt', 'Affine', 'Ae', '7', '7.']:
        plain_text = input(plain_text_message)
        valid = True
        while valid:
            have_key = input("Do you have an encryption key already?\nY/N>> ").upper().strip()
            if have_key.startswith("Y"):
                try:
                    key = int(input("Enter key>> ").strip())
                    print(affineCipher.encryptMessage(key, plain_text))
                    to_continue()
                    valid = False
                except ValueError:
                    print(numeric_key_error)
                    continue
            elif have_key.startswith("N"):
                key = affineCipher.getRandomKey()
                print("Your key is:\n>> ", key)
                to_continue()
                print(affineCipher.encryptMessage(key, plain_text))
                valid = False
            else:
                print("Please make a valid selection.")

    elif user_input in ['Affine, Decrypt', 'Ad', '8', '8.']:
        cipher_text = input(cipher_text_decrypt)
        valid = True
        while valid:
            try:
                key = int(input("Enter encryption key:\n>> ").strip())
                print(affineCipher.decryptMessage(key, cipher_text))
                to_continue()
                valid = False
            except ValueError:
                print(numeric_key_error)
                continue

    elif user_input in ['Affine, Hack', 'Ah', '3', '3.']:
        cipher_text = input(cipher_text_hack)
        print(affineHacker.hackAffine(cipher_text))
        to_continue()

###############################################################################
#                               SUBSTITUTION BRANCH
################################################################################                        
    elif user_input in ['Substitution, Encrypt', 'Substitution', 'Se', '10', '10.']:
        plain_text = input(plain_text_message)
        valid = True
        while valid:
            have_key = input("Do you have an encryption key already?\nY/N>> ").upper().strip()
            if have_key.startswith("Y"):
                key = input("Enter key:\n>> ").upper().strip()
                if simpleSubCipher.keyIsValid(key):
                    print(simpleSubCipher.encryptMessage(key, plain_text))
                    valid = False
                else:
                    print(alpha_key_error)
            elif have_key.startswith("N"):
                key = simpleSubCipher.getRandomKey()
                print("Your key is:\n>> ", key)
                to_continue()
                print(simpleSubCipher.encryptMessage(key, plain_text))
                to_continue()
                valid = False
            else:
                print("Please make a valid selection.")

    elif user_input in ['Substitution, Decrypt', 'Sd', '11', '11.']:
        cipher_text = input(cipher_text_decrypt)
        valid = True
        while valid:
            key = input("Enter encryption key:\n>> ").strip().upper()
            if simpleSubCipher.keyIsValid(key):
                print(simpleSubCipher.decryptMessage(key, cipher_text))
                to_continue()
                valid = False
            else:
                print(alpha_key_error)

    elif user_input in ['Substitution, Hack', 'Sh', '12', '12.']:
        cipher_text = input(cipher_text_hack)
        letter_mapping = simpleSubHacker.hackSimpleSub(cipher_text)
        print("\nLetter Mapping:\n", letter_mapping)
        print("\nOriginal Ciphertext:\n", cipher_text)
        hacked, key = simpleSubHacker.decryptWithCipherletterMapping(cipher_text, letter_mapping)
        print("\nHacked Message:\n", hacked)
        print("\nProposed Key: ", key)
        to_continue()
        #need to add a loop/option here where I can go directly to the sub-cipher decrypt and try the 
        #new key and add in letters as I see fit    

###############################################################################
#                               VIGENERE BRANCH
################################################################################        
    elif user_input in ['Vigenere, Encrypt', 'Vigenere', 'Ve', '13', '13.']:    
        plain_text = input(plain_text_message)
        valid = True
        while valid:
            key = input("Enter encryption key:\n>> ").upper().strip()
            if vigenereCipher.keyIsValid(key):
                print(vigenereCipher.encrypt(key, plain_text))
                to_continue()
                valid = False
            else:
                print(alpha_key_error)
            
    elif user_input in ['Vigenere, Decrypt', 'Vd', '14', '14.']:
        cipher_text = input(cipher_text_decrypt)
        valid = True
        while valid:
            key = input("Enter encryption key:\n>> ")
            if vigenereCipher.keyIsValid(key):
                print(vigenereCipher.decrypt(key, cipher_text))
                to_continue()
                valid = False
            else:
                print(alpha_key_error)

    elif user_input in ['Vigenere, Hack', 'Vh', '15', '15.']:
        cipher_text = input(cipher_text_hack)
        valid = True
        while valid:
            user_input = input("Attempt hack utilizing a dictionary hack or brute-force hack?\n>> ")
            if user_input.upper().startswith('D'):
                print(vigenereDictionaryHacker.hackVigenereDictionary(cipher_text))
                to_continue()
                valid = False
            elif user_input.upper().startswith('B'):
                print(vigenereHacker.hackVigenere(cipher_text))
                to_continue()
                valid = False
            else:
                print("Error: choice must be 'dictionary' or 'brute-force'.")

    elif user_input == 'Ta':
        cipher_text = input(cipher_text_hack)
        print(caesar_cipher.cc_hack(cipher_text))
        to_continue()
        print(transposition_cipher.transposition_hack(cipher_text))
        to_continue()
        print(affineHacker.hackAffine(cipher_text))
        to_continue()
        letter_mapping = simpleSubHacker.hackSimpleSub(cipher_text)
        print("\nLetter Mapping:\n", letter_mapping)
        print("\nOriginal Ciphertext:\n", cipher_text)
        hacked, key = simpleSubHacker.decryptWithCipherletterMapping(cipher_text, letter_mapping)
        print("\nHacked Message:\n", hacked)
        print("\nProposed Key: ", key)
        to_continue()
        print(vigenereDictionaryHacker.hackVigenereDictionary(cipher_text))
        to_continue()
        print(vigenereHacker.hackVigenere(cipher_text))
        to_continue()        
        
    
    else: #output when user types an invalid choice
        print("Error: make a valid selection.")