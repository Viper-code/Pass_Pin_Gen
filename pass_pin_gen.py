import string
import random
import time

password = ""
pin = ""
nitro = ""

start = input('''\nHello and welcome to the password and pin generator made by Shujah
                           Type  "pin" to gen a 4 number pin
                           Type "pass" to gen a password where you can choose how much digit
                           it has and if it has letters number or only nums/letters

                    Please type here: ''')
if start.lower() == 'pass':
    num_letter = input('Please enter if you want your password to have "num", or "letters" or "both" type (num/letters/both): ')
    if num_letter.lower() == "num":
        how_many_num1 = input('How many digits do you want?We advice you to choose from 7 - 128: ')
        print('PROCESSING...')
        time.sleep(1.5)
        pass_gen1 = "".join(random.choices(string.digits, k = int(how_many_num1)))
        print(f'Here is your password\n {pass_gen1}')
        digit_pass_save = input('Do you want to save this password? (y/n):')
        if digit_pass_save == "y":
            where3 = input(f'Where Do you want to save the password {pass_gen1}, type a name for example pin.txt, you must have txt in the end or this process will fail: ')
            print('SAVING...')
            time.sleep(1.5)
            digit_file_saving = open(where3, 'w')
            digit_file_saving.write(f'Password(s):\n{"".join(pass_gen1)}\n remember if you regenerate it will write over this!')
            print('Saved Password in Pass_Digit.txt')
    if num_letter.lower() == "letters":
        how_many_letters1 = input('How many letters do you want in your password?We advice you to choose from 7 - 128: ')
        print('PROCESSING...')
        time.sleep(1.5)
        letters_gen1 = "".join(random.choices(string.ascii_letters, k = int(how_many_letters1)))
        print(f'Here is your password\n {letters_gen1}')
        letters_pass_save = input('Do you want to save this password? (y/n):')
        if letters_pass_save == "y":
            where2 = input(f'Where Do you want to save the password {letters_gen1}, type a name for example pin.txt, you must have txt in the end or this process will fail: ')
            print('SAVING...')
            time.sleep(1.5)
            letters_file_saving = open(where2, 'w')
            letters_file_saving.write(f'Password(s):\n{"".join(letters_gen1)}\n remember if you regenerate it will write over this!')
            print(f'Saved Password in the file {where2}')        
    if num_letter.lower() == "both":
        how_many_both1 = input('How many Digit/Letters you want in your password?We advice you to pick from 2 - 128, and this will double so if u pick 7 it will make a password with 14 digits so think wisely: ')
        print('PROCESSING...')
        time.sleep(1.5)
        l=random.choices(string.ascii_lowercase, k=int(how_many_both1))
        d=random.choices(string.digits, k=int(how_many_both1))
        both_gen =l+d
        random.shuffle(both_gen)
        print(f'Here is your password\n {"".join(both_gen)} it has {int(how_many_both1) * 2} letters/digits in it!')
        both_pass_save = input('Do you want to save this password? (y/n):')
        if both_pass_save == "y":
            where1 = input(f'Where Do you want to save the password {both_gen}, type a name for example pin.txt, you must have txt in the end or this process will fail: ')
            print('SAVING...')
            time.sleep(1.5)
            Both_file_saving = open(where1, 'w')
            Both_file_saving.write(f'Password(s):\n{"".join(both_gen)}\nremember if you regenerate it will write over this!')
            print(f'Saved Password in the file {where1}')
if start.lower() == 'pin':
    pin_start = input('Should I start the process of making a 4 digit pin?(y/n): ')
    if pin_start.lower() == 'y':
        print('PROCESSING...')
        time.sleep(1.5)
        pin_gen = "".join(random.choices(string.digits, k = 4))
        print(f'Here is your pin\n {pin_gen}\n ')
        save1 = input('Do you want to save this pin? (y/n): ')
        if save1 == "y" or "yes":
            #create_use_file1 = input('Do you want to create a txt document with the pin?Or save it somwhere alse (y/n): ')
            #if create_use_file1 == "n" or "no":
                #tell_file = input('Please tell your file file location for example "C:\Users\Boby\Desktop\Codes" or if you dont know how go to google and type "how to find path" then look for a article/vid that explains good: ')
            where = input(f'Where Do you want to save the pin {pin_gen}, type a name for example pin.txt, you must have txt in the end or this process will fail: ')
            print('SAVING...')
            time.sleep(1.5)
            txtFile = open( where, 'w')
            txtFile.write(f'Here are your pin(s):\n{pin_gen}\n remember if you regenerate it will write over this!')
            print(f'Done saving in the File {where}') 
if start.lower() == 'nitro':
    print('Coming soon\nThis will be fake nitro not real to prank ur friends')
                  
input('Please Press ENTER To EXIT')