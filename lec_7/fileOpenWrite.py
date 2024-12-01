import os

def main():
    while True:
        try:
            filename = input ("Enter the filename: ").strip()
            if not filename:
                raise ValueError("Filename is empty")
            
            with open(filename, 'r') as file :
                content = file.read()
                print(f"\nFile content: {content}")
                break
        except FileNotFoundError:
            print("File not found: ")
        except ValueError as ve:
            print(f"Error: {ve}")

    
    while True:
        writeOption = input("\nDo you want to write to a file (yes/no): ").strip().lower()
        if writeOption in ['yes', 'no']:
            break
        print ("Please enter yes or no")

    if writeOption == 'yes':
        while True:
            overwriteOption = input("Write to the same or a new file?(same/new): ").strip().lower()
            if overwriteOption in ['same', 'new']:
                print("OK")
                break
            else:
                print ("Please enter same or new: ")

        if overwriteOption == 'same':
                 writeFileName = filename
        else:
            while True:
                writeFileName = input("Enter the name of the new file: ").strip()
                if writeFileName:
                    break
                print("Filename is empty")

        try:
            contentToWrite = input("Enter the content to write: ")
            with open(writeFileName, 'w') as file :
                file.write(contentToWrite)
        except  Exception as e:
            print(f"There is an error while writing: {e}")
        finally:
            print(f"Content successfully written and The file '{writeFileName}' has been closed")


if __name__ == "__main__":
    main()