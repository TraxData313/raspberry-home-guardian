import os
print()
print()
print()

# - Create the ./media folder:
print("Creating the media folder...")
if not os.path.exists('media'):
    os.mkdir('./media');
    print("- Done!")
else:
    print("- ./media already exists, passing this step")

# - Create the settings file:
print()
print()
print("Setting up bucket name...")
bucket_name = input("- Please enter the S3 bucket name: ")
saveFile = open('./settings.txt', 'w')
saveFile.write('Bucket name:')
saveFile.write('\n')
saveFile.write(str(bucket_name))
saveFile.close()
print()
print("Success! bye")
print()

