import caesar_cipher #must match the ACTUAL filename
import transposition_cipher
import affineCipher
import simpleSubCipher


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
                            "4. Substitution Cipher\n" +
                            "5. Vigenere\n" +
                            "99. .. (to return to main menu)\n >> ").title().strip()
    return user_input


print("Welcome to Mr. Schnaars' encryption program!\n" + 
        "Please choose whether you would like to encrypt or decrypt.\n" + 
        "Then you will be asked to choose a type of cipher.\n")

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
#
################################################################################
    
    elif user_input in ['Encrypt', '1', '1.']:
        user_input = cipher_selection()
        
        if user_input in ['Caesar', '1', '1.']:
            valid = True
            while valid:
                try:
                    key = int(input("Please choose a key, 1-25.\n").strip())
                    plain_text = input("Please enter your message.\n").upper()
                    print(caesar_cipher.caesar_encrypt(key, plain_text))
                    valid = False
                except ValueError:
                    print("Caesar cipher keys must be numeric.")
                    continue
        
        elif user_input in ['Transposition', '2', '2.']:
            valid = True
            while valid:
                try:
                    plain_text = input("Please enter your message.\n")
                    print("Choose a key between 1 and", int(len(plain_text)/2))
                    key = int(input("Key: ").strip())
                    print(transposition_cipher.transposition_encrypt(key, plain_text))
                    valid = False
                except ValueError:
                    print("Transposition keys must be numeric.")
                    continue
        
        elif user_input in ['Affine', '3', '3.']:
            plain_text = input("Please enter your message.\n")
            have_key = input("Do you have an encryption key already?\nY/N: ").upper().strip()
            if have_key in ['Y', 'YES']:
                key = int(input("Enter key: ").strip())
                print(affineCipher.encryptMessage(key, plain_text))
            elif have_key in ['N', 'NO']:
                key = affineCipher.getRandomKey()
                print("Your key is:", key)
                print(affineCipher.encryptMessage(key, plain_text))
            else:
                print("Please make a valid selection.")
                        
        elif user_input in ['Substitution Cipher', '4', '4.']:
            plain_text = input("Please enter your message:\n>> ")
            have_key = input("Do you have an encryption key already?\nY/N: ").upper().strip()
            if have_key in ['Y', 'YES']:
                key = input("Enter key:\n>> ").upper().strip()
                print(simpleSubCipher.encryptMessage(key, plain_text))
            elif have_key in ['N', 'NO']:
                key = simpleSubCipher.getRandomKey()
                print("Your key is:", key)
                print(simpleSubCipher.encryptMessage(key, plain_text))
            else:
                print("Please make a valid selection.")
        
        elif user_input in ['Vigenere', '5', '5.']:    
            plain_text = input("Please enter your message:\n>> ")
            key = input("Enter your key:\n>> ")
            
        else:
            print("Sorry, that was not a valid selection.")
            user_input = cipher_selection()                   
    
################################## DECRYPT BRANCH ##############################
    elif user_input == 'Decrypt':
        user_input = input("Choose type of decryption:\n" +
                            "1. Caesar\n" +
                            "2. Transposition\n" +
                            "3. Affine\n" +
                            "4. Substitution Cipher\n").title().strip()
        
        if user_input in ['Caesar', '1', '1.']:
            key = int(input("Please choose a key, 1-25.\n").strip())
            cipher_text = input("Please enter your message.\n").upper()
            print(caesar_cipher.caesar_decrypt(key, cipher_text))
        
        elif user_input in ['Transposition', '2', '2.']:
            cipher_text = input("Please enter your message.\n")
            key = int(input("Please enter your encryption key.\n").strip())
            print(transposition_cipher.transposition_decrypt(key, cipher_text))
        
        elif user_input in ['Affine', '3', '3.']:
            cipher_text = input("Please enter your encrypted message.\n")
            key = int(input("Enter key: ").strip())
            print(affineCipher.decryptMessage(key, cipher_text))
            
        elif user_input in ["Substitution Cipher", "Substitution", "4", "4."]:
            cipher_text = input("Please enter your encrypted message.\n")
            key = input("Enter key: ").strip().upper()
            print(simpleSubCipher.decryptMessage(key, cipher_text))
        
        else:
            print("Sorry, that was not a valid selection.")

################################## HACK BRANCH #################################        
    elif user_input == 'Hack' or user_input == '3':
        user_input = cipher_selection()
        
        if user_input in ['Caesar', '1', '1.']:
            cipher_text = input("Please enter your message.\n")
            caesar_cipher.cc_hack(cipher_text)
        
        elif user_input in ['Transposition', '2', '2.']:
            cipher_text = input("Please enter your message.\n")
            transposition_cipher.transposition_hack(cipher_text)
        
        #elif 
        
        else:
            print("Sorry, that was not a valid selection.")

################################## INVALID OPTIONS #############################        
    else: #output when user types an invalid choice
        print("Sorry, that is not a valid option.")


