#Write a program that copies the contents of one text file to another.
src_file = input("Enter the source file name: ")
dst_file = input("Enter the destination file name: ")

with open(src_file, 'r') as src:
    with open(dst_file, 'w') as dst:
        dst.write(src.read())

print(f"Contents of {src_file} copied to {dst_file}")