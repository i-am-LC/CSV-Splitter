import sys

# Ask the user for the file location
file_location = input('Enter the file location: ')

# Check if the user provided a valid file location
if not file_location:
    print('Provide a valid file location.')
    sys.exit()

try:
    # Open the file provided by the user
    with open(file_location, 'r', encoding='utf-8', errors='replace') as file:
        csvfilename = file.readlines()

        # Store the header
        header = csvfilename[0]

        # Remove the header from the list
        csvfilename = csvfilename[1:]

        # Ask the user for the number of records per file
        while True:
            try:
                record_per_file = int(input('Enter the number of records per file: '))
                if record_per_file > 0:
                    break
                else:
                    print('Number of records per file must be a positive integer.')
            except ValueError:
                print('Please enter a valid positive integer.')

        file = 1
        for j in range(0, len(csvfilename), record_per_file):
            # Create slices of records for each file
            write_file = csvfilename[j:j + record_per_file]

            # Insert the header at the beginning of each write_file
            write_file.insert(0, header)

            # Create a new file with a name like "output1.csv", "output2.csv", etc.
            output_filename = f"output{file}.csv"
            with open(output_filename, 'w') as output_file:
                output_file.writelines(write_file)

            file += 1

    print(f'Successfully split the file into {file - 1} parts.')

except FileNotFoundError:
    print(f'File not found: {file_location}')
except Exception as e:
    print(f'An error occurred: {str(e)}')