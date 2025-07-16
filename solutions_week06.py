def load_to_list(filepath:str) -> list[float]:
    """Reads a file and copies each line to a list element. The file must
    contain one numeric value per line. The file is passed to this 
    method as a full filepath string."""
    # List to receive contents from the file
    data = []
    # Establish a connection to the file
    with open(filepath, "r") as file:
        # Scan the file, one line at a time
        for data_entry in file: 
            # There may be empty lines in the file, check first
            if data_entry:
                # Convert the contents of the line into a float value
                temperature = float(data_entry)
                # Add the value to the list
                data.append(temperature)
    # Done
    return data
    # end method load_to_list

def descriptive_statistics(data: list[float]) -> None:
    """Displays basic descriptive statistics for data presented as a list."""
    # First we make sure that the presented list is not empty
    if data:
        # Initialize accumulator and extrema
        sum = 0
        min = data[0]
        max = data[0]
        # Consider every item in the data set
        for value in data:
            # Update the sum -- for averaging
            sum += value
            # Test for a new min value
            if value < min:
                min = value 
            # Test for a new max value
            if value > max:
                max = value
        # Display the findings
        print(f"\nThere are {len(data)} values in the data source.")
        print(f"The average value is {sum/len(data):.2f}")
        print(f"The highest value is {max} and the smallest value is {min}.\n")
    else:
        print("Data source is empty.")
    # end method descriptive_statistics


def apply_markup(filepath:str) -> None:
    """Process a text file with simple markup. There are two markup tags to
    consider: a dot as the first character of a word coverts the word to upper
    case. An underscore converts the word to a spaced out emphasis."""
    # Connect to the file.
    with open(filepath, 'r') as file:
        # Read every line in the file
        for line in file:
            # Split the contents of the line into strings separated by spaces.
            words = line.split()
            # Initialize the output line
            output_line = ''
            # For every string in the current line
            for word in words:
                # If the string starts with either of the markup tags
                if word.startswith('.') or word.startswith('_'):
                    # Obtain a copy of the string without the tag
                    rest = word[1:]
                    # Markup applies only to alphabetical content, so let's
                    # check first, otherwise skip to the next string
                    if rest.isalpha():
                        # OK, now check the markup tag
                        if word[0] == '.':
                            # OK, convert the non-taged string into upper case and
                            # add it to the output line
                            output_line = output_line + rest.upper() + ' '
                        else:
                            # Since there are only two tags and we are here because
                            # the tag is not a "." it must be an "_". Process the
                            # string character-by-character and create a spaced-out
                            # version of it. Then add it to the output line
                            spaced_out = ' '
                            for c in rest:
                                spaced_out += c+' '
                            output_line = output_line + spaced_out+' '
                    else:
                        # We are here because the current string is not
                        # alphabetical. Therefore it can be added as
                        # is to the output line as is.
                        output_line = output_line + word + ' '
                else:
                    # We are here because the current string does not start
                    # with a formatting tag. Therefore it can be added as
                    # is to the output line as is.
                    output_line = output_line+ word+' '
            # Print the current line, formatted
            print(output_line)
    # end method apply_markup
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
l=load_to_list("data/temperatures.txt")
print(l)
descriptive_statistics(l)
apply_markup("data/markup.txt")