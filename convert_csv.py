import csv

# Define the input and output file names
input_file = 'training_dataset_short.csv'
output_file = 'output.txt'

# Open the input CSV file for reading
with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    
    # Open the output file for writing
    with open(output_file, mode='w', encoding='utf-8') as output:
        # Process each row in the CSV file
        for row in csvreader:
            # Extract the columns
            column_1 = row[0]
            column_2 = row[1]
            
            # Write the formatted string to the output file
            output.write(f"<SFT>### Human: {column_1} ### Assistant: {column_2}\n")

