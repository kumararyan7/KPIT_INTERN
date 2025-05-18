def process_strings(input_list):
    # Validation: Check if all elements in the input list are strings
    if not all(isinstance(item, str) for item in input_list):
        raise TypeError("All elements in the input list must be strings.")

    # Sort the input list in ascending order
    sorted_list = sorted(input_list, key=lambda x: x.lower())

    # Filter out strings that are digits or have a length less than 5 characters
    filtered_list = [s for s in sorted_list if not s.isdigit() and len(s) >= 5]

    # Calculate the length of each string in the filtered list
    length_list = [len(s) for s in filtered_list]

    # Calculate the sum of the lengths of all strings in the filtered list
    sum_length = sum(length_list)

    # Find the string with the maximum length in the original input list
    max_length_string = max(input_list, key=len)

    # Replace all occurrences of "ion" with "ment" in the original input list
    modified_list = [s.replace("ion", "ment") for s in input_list]

    # Return all results as a 
    return {
        "sorted_list": sorted_list,
        "filtered_list": filtered_list,
        "length_list": length_list,
        "sum_length": sum_length,
        "max_length_string": max_length_string,
        "modified_list": modified_list,
    }


# Input
input_data = ["hello world", "12345", "abcdef", "defghi jklmno", "pqrstuionized", "ionizationmentallity"]
input_data1= ["hello world", "2345","welcome","kpit","ionized","ionization123"]
# Process 
result = process_strings(input_data)
result1 = process_strings(input_data1)
# Print the results
for key, value in result.items():
    print(f"{key}: {value}")


for key, value in result1.items():
    print(f"{key}: {value}")
    


















