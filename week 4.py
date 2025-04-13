def read_and_mofify_file():
    input_file_name = input("Enter the name of the file you want to read: ")

    try:
        with open(input_file_name, 'r') as file:
            data=file.read()
    except FileNotFoundError:
        print(f"File {input_file_name} not found.")
        return
    

#writing the modified version to a new file
    output_file_name = input("Enter the name of the file you want to write: ")
    with open(output_file_name, 'w') as file:
        # reversing order of characters in the file
        file.write(data[::-1])
        print(f"File {output_file_name} has been created with modified content.")
