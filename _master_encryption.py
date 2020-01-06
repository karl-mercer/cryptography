import caesar_cipher #must match the ACTUAL filename
import transposition_cipher
import affineCipher, affineHacker
import simpleSubCipher
import vigenereCipher, vigenereHacker, vigenereDictionaryHacker

def type_selection():
    user_input = input("Choose type of decryption:\n" +
                            "1. Encrypt\n" +
                            "2. Decrypt\n" +
                            "3. Hack\n" +
                            "99. Quit\n>> ").title().strip()
    return user_input

def cipher_selection():
    user_input = input("Choose type of encryption:\n" +
                            "1. Caesar\n" +
                            "2. Transposition\n" +
                            "3. Affine\n" +
                            "4. Substitution\n" +
                            "5. Vigenere\n" +
                            "99. .. (return up a level)\n>> ").title().strip()
    return user_input

def to_continue():
    input("Press Enter to continue>> ")

print("Welcome to Mr. Schnaars' encryption program!\n")

print("Type 'Quit' to exit at any time.\n")

user_input = '' #initially user_input is just an empty string

while user_input.title().strip() != 'Quit': #as long as they don't type 'Quit'
    #instructions...
    user_input = type_selection()
    
    if user_input in ['Quit', '99', 'Exit']:
        user_input = 'Quit'
   

###############################################################################
#
#                               ENCRYPT BRANCH
################################################################################
    
    elif user_input in ['Encrypt', '1', '1.']:
        user_input = cipher_selection()
        
        if user_input in ['Caesar', '1', '1.']:
            plain_text = input("Please enter your message.\n>> ").upper()
            valid = True
            while valid:
                try:
                    key = int(input("Please choose a key, 1-25.\nKey>> ").strip())
                    print(caesar_cipher.caesar_encrypt(key, plain_text))
                    to_continue()
                    valid = False
                except ValueError:
                    print("ValueError: Caesar cipher keys must be numeric.")
                    continue
        
        elif user_input in ['Transposition', '2', '2.']:
            plain_text = input("Please enter your message.\n>> ")
            valid = True
            while valid:
                try:
                    print("Choose a key between 1 and", int(len(plain_text)/2))
                    key = int(input("Key>> ").strip())
                    print(transposition_cipher.transposition_encrypt(key, plain_text))
                    to_continue()
                    valid = False
                except ValueError:
                    print("ValueError: Transposition keys must be numeric.")
                    continue
        
        elif user_input in ['Affine', '3', '3.']:
            plain_text = input("Please enter your message.\n>> ")
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
                        print("Affine keys must be numeric.")
                        continue
                elif have_key.startswith("N"):
                    key = affineCipher.getRandomKey()
                    print("Your key is:", key)
                    to_continue()
                    print(affineCipher.encryptMessage(key, plain_text))
                    valid = False
                else:
                    print("Please make a valid selection.")
                        
        elif user_input in ['Substitution Cipher', '4', '4.']:
            plain_text = input("Please enter your message:\n>> ")
            valid = True
            while valid:
                have_key = input("Do you have an encryption key already?\nY/N>> ").upper().strip()
                if have_key.startswith("Y"):
                    key = input("Enter key:\n>> ").upper().strip()
                    if simpleSubCipher.keyIsValid(key):
                        print(simpleSubCipher.encryptMessage(key, plain_text))
                        valid = False
                    else:
                        print("Error: not a valid key.\nCheck that key contains all letters in the alphabet and has no duplicate letters.")
                elif have_key.startswith("N"):
                    key = simpleSubCipher.getRandomKey()
                    print("Your key is:", key)
                    to_continue()
                    print(simpleSubCipher.encryptMessage(key, plain_text))
                    valid = False
                else:
                    print("Please make a valid selection.")
        
        elif user_input in ['Vigenere', '5', '5.']:    
            plain_text = input("Please enter your message:\n>> ")
            valid = True
            while valid:
                key = input("Enter your key:\n>> ").upper().strip()
                if vigenereCipher.keyIsValid(key):
                    print(vigenereCipher.encrypt(key, plain_text))
                    to_continue()
                    valid = False
                else:
                    print("Error: Vigenere cipher keys may only contain letters.")
            
        else:
            print("Sorry, that was not a valid selection.")
            user_input = cipher_selection()                   

    
###############################################################################
#
#                               DECRYPT BRANCH
#
###############################################################################
    elif user_input in ['Decrypt', '2', '2.']:
        user_input = cipher_selection()
        
        if user_input in ['Caesar', '1', '1.']:
            key = int(input("Please choose a key, 1-25.\nKey>> ").strip())
            cipher_text = input("Please enter your message.\n>> ").upper()
            print(caesar_cipher.caesar_decrypt(key, cipher_text))
        
        elif user_input in ['Transposition', '2', '2.']:
            cipher_text = input("Please enter your message.\n>> ")
            key = int(input("Please enter your encryption key.\nKey>> ").strip())
            print(transposition_cipher.transposition_decrypt(key, cipher_text))
        
        elif user_input in ['Affine', '3', '3.']:
            cipher_text = input("Please enter your encrypted message.\n>> ")
            key = int(input("Please enter your encryption key.\nKey>> ").strip())
            print(affineCipher.decryptMessage(key, cipher_text))
            
        elif user_input in ["Substitution Cipher", "Substitution", "4", "4."]:
            cipher_text = input("Please enter your encrypted message.\n>> ")
            key = input("Please enter your encryption key.\nKey>> ").strip().upper()
            print(simpleSubCipher.decryptMessage(key, cipher_text))

        elif user_input in ['Vigenere', '5', '5.']:
            cipher_text = input("Please enter your encrypted message.\n>> ")
            key = input("Please enter your encryption key.\n>> ")
            print(vigenereCipher.decrypt(key, cipher_text))
        
        else:
            print("Sorry, that was not a valid selection.")

###############################################################################
#
#                               HACK BRANCH
#
###############################################################################
    elif user_input in ['Hack', '3', '3.']:
        user_input = cipher_selection()
        
        if user_input in ['Caesar', '1', '1.']:
            cipher_text = input("Please enter your message to be hacked.\n>> ")
            caesar_cipher.cc_hack(cipher_text)
        
        elif user_input in ['Transposition', '2', '2.']:
            cipher_text = input("Please enter your message to be hacked.\n>> ")
            transposition_cipher.transposition_hack(cipher_text)
        
        elif user_input in ['Affine', '3', '3.']:
            cipher_text = input("Please enter your message to be hacked.\n>> ")
            print(affineHacker.hackAffine(cipher_text))

        elif user_input in ['Substitution', '4', '4.']:
            pass

        elif user_input in ['Vigenere', '5', '5.']:
            cipher_text = input("Please enter your message to be hacked.\n>> ")
            user_input = input("Would you like to perform a dictionary hack or a brute-force hack?\n>> ")
            if user_input.upper().startswith('D'):
                print(vigenereDictionaryHacker.hackVigenereDictionary(cipher_text))
            elif user_input.upper().startswith('B'):
                print(vigenereHacker.hackVigenere(cipher_text))
            else:
                print("Sorry, that was not a valid selection.")
        
        else:
            print("Sorry, that was not a valid selection.")

################################## INVALID OPTIONS #############################        
    else: #output when user types an invalid choice
        print("Sorry, that is not a valid option.")



