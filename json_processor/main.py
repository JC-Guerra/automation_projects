import json
import os

def get_file_name():
    try:
        #setting path
        script_dir = os.path.dirname(os.path.realpath(__file__))
        all_files = os.listdir(script_dir)

        # file_name = 'sample.json'
        # file_path = os.path.join(script_dir, file_name)

        #listing json files to show user
        json_files = [file for file in all_files if file.endswith(".json")]

        print('List of JSON files in the folder:')
        for index, file in enumerate(json_files, 1):
            print(f'{index}. {file}')

        #return selected file
        selected_index = int(input('Enter the number of corresponding to the JSON file: ')) - 1
        selected_file = json_files[selected_index]

        file_name = os.path.join(script_dir, selected_file)
        return file_name

    except FileNotFoundError:
        print(f'Error: File not found at {file_path}')
    except Exception as e:
        print(f'An unexpected error occured in get_file_name: {e}')

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        initial_value = data['person'][0]['first_name']
        data['person'][0]['first_name'] = 'Jonathan'

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Changed first_name from {initial_value} to {data['person'][0]['first_name']}")
    except json.decoder.JSONDecodeError as e:
        print(f'Error decoding JSON: {e}')
    except Exception as e:
        print(f'An unexpected error occured: {e}')

def main():
    file_name = get_file_name()
    read_json(file_name)

if __name__ == "__main__":
    main()