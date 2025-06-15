# task 1
try:
    file1 = open('sample.txt', 'r')
    print("Reading file content:")
    for line in file1:
        print(line.strip())
    file1.close()
except FileNotFoundError:
    print("Error: 'sample.txt' does not exist.")

#task2
user_input = input("Enter some text to write to the file:")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

additional_input = input("Enter more text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())


