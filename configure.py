import os
print()
print()
print()


def change_bucket_name():
    try:
        bucket_name = raw_input("- Please enter the S3 bucket name: ")
    except:
        bucket_name = input("- Please enter the S3 bucket name: ")
    saveFile = open('./settings.txt', 'w')
    saveFile.write('Bucket name:')
    saveFile.write('\n')
    saveFile.write(bucket_name)
    saveFile.write('\n')
    saveFile.close()
    print()
    print("- Success!")
    print()

    
    
    

# - STEP 1: Create the ./media folder:
print("Creating the media folder...")
if not os.path.exists('media'):
    os.mkdir('./media');
    print("- Done!")
else:
    print("- ./media already exists, passing this step")

    

# - STEP 2: Create the settings file:
print()
print()
print("Setting up bucket name...")
if os.path.exists('settings.txt') == True:
    # - Recover the bucket name from the settings file:
    bucket_name = open('settings.txt', 'r').readlines()
    bucket_name = str(bucket_name[1])
    bucket_name = bucket_name[:-1]
    
    # - Show and prompt to change it:
    print("- Current bucket name is < {} >".format(bucket_name))
    try:
        change_it = raw_input("- Do you want to change it? (y/n): ")
    except:
        change_it = input("- Do you want to change it? (y/n): ")
    
    if change_it == 'y':
        change_bucket_name()
        
    elif change_it == 'n':
        print("- OK. Leaving bucket name {}".format(bucket_name))
        
    else:
        print()
        print("- ERROR")
        print("- Wrong input! Answer y for yes or n for no. Please rerun the program.")
        print()
        pi_over_zero = 3.14/0
        
else:
    change_bucket_name()


# - STEP 3: Initialize the arm_state:
arm_state = 1 # UNARMED
state_file = 'arm_state.txt'
print('- Initializing the arm state file...')
functions.save_state(state_file, arm_state)
print('- Done! Raspberry is unarmed!')