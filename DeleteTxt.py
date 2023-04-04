import os

file_path = "/Users/user/Documents"
#you may want to change path to Desktop,Downloads etc

if os.path.exists(file_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith(".txt"):
                os.remove(os.path.join(root, file))
    print("All .txt files in", file_path, "and its subdirectories have been deleted.")
else:
    print(file_path, "does not exist.")
