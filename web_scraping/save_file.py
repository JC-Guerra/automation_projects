from datetime import datetime as dt
import os

def write_file(content):
    #write values to text file
    filename = f"{dt.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    file_path = os.path.join("created_files", filename)
    with open(file_path, 'w') as file:
        print(f"I'm inside open method, content: {content}")
        file.write(content)