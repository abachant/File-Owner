def group_by_owners(text_input):
    """Organize a dictionary of files by their authors"""
    text_output = {}

    if type(text_input) is dict:
        # Switch the keys and values
        for key, value in text_input.items():
            text_output[value] = [key]
        # Cycle through keys and remove redundancies
        for i in text_output:
            for x in text_output:
                if x != i:
                    text_output[x] = []
        # Add all values to their respective keys
        for key, value in text_input.items():
            text_output[value].append(key)

    else:
        print("Please make sure your text files are listed in a dictionary.")
    print(text_output)
