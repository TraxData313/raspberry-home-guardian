import os


# - Create the ./media folder:


# - Create the settings file:
bucket_name = input("Enter your S3 bucket name: ")
saveFile = open('./settings.txt', 'w')
saveFile.write('Bucket name:')
saveFile.write('\n')
saveFile.write(str(bucket_name))
saveFile.close()
print()
print("Success! bye")
print()

