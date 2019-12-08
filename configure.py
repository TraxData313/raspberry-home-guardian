import os
print()
print()
print()

# Defining the needed functions:

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

    
def change_aws_settings():
    # - Create the ~/.aws directory:
    print()
    print("- Creating directory ~/.aws:")
    os.mkdir('~/.aws')
    print("- Done!")
    # - Set the region:
    print()
    try:
        aws_region = raw_input("- Please enter your aws region (example: eu-west-1): ")
    except:
        aws_region = input("- Please enter your aws region (example: eu-west-1): ")
    aws_region_formated = "region=" + aws_region
    outputFile = "~/.aws/config"
    saveFile = open(outputFile, 'w')
    saveFile.write('[default]')
    saveFile.write('\n')
    saveFile.write(str(aws_region_formated))
    saveFile.close()
    print("- AWS region set to {}".format(aws_region))
    
    # - Set the aws_access_key_id and the aws_secret_access_key:
    print()
    try:
        aws_access_key_id = raw_input("- Please enter your aws_access_key_id: ")
    except:
        aws_access_key_id = input("- Please enter your aws_access_key_id: ")
    aws_access_key_id_formated = "aws_access_key_id = " + aws_access_key_id
    
    try:
        aws_secret_access_key = raw_input("- Please enter your aws_secret_access_key: ")
    except:
        aws_secret_access_key = input("- Please enter your aws_secret_access_key: ")
    aws_secret_access_key_formated = "aws_secret_access_key = " + aws_secret_access_key
    outputFile = "~/.aws/credentials"
    saveFile = open(outputFile, 'w')
    saveFile.write('[default]')
    saveFile.write('\n')
    saveFile.write(str(aws_access_key_id_formated))
    saveFile.write('\n')
    saveFile.write(str(aws_secret_access_key_formated))
    saveFile.close()
    print("- aws_access_key_id {}".format(aws_access_key_id))
    print("- aws_secret_access_key {}".format(aws_secret_access_key))
    
    
    
    
    
    
    
# STEPS:



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


    
# - STEP 4: Set AWS Credentials:
print()
print()
print("Setting up AWS Credentials...")
if os.path.exists('~/.aws') == True:
    
    # - Show and prompt to change it:
    print("- The ~/.aws folder that contains the settings exists.")
    try:
        change_it = raw_input("- Do you want to change settings? (y/n): ")
    except:
        change_it = input("- Do you want to change settings? (y/n): ")
    
    if change_it == 'y':
        change_aws_settings()
        
    elif change_it == 'n':
        print("- OK. Leaving current settings.")
        
    else:
        print()
        print("- ERROR")
        print("- Wrong input! Answer y for yes or n for no. Please rerun the program.")
        print()
        pi_over_zero = 3.14/0
        
else:
    change_aws_settings()
    
    
    
# - STEP 4: Initialize the arm_state:
arm_state = 1 # UNARMED
state_file = 'arm_state.txt'
print()
print()
print('- Initializing the arm state file...')
functions.save_state(state_file, arm_state)
print('- Done! Raspberry is unarmed!')