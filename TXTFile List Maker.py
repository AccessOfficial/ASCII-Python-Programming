# Code used to make list for the animation script so you dont have to manually add each txt file

filenames = []

# input number of txt files in range
new_filenames = [f"{i}.txt" for i in range(1, 26)]

filenames.extend(new_filenames)

print(filenames)