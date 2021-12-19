def boston_info(description: str):
    """[summary]

    Args:
        description (str): [description]
    """
    text_file = open("boston_housing_decsription.txt", "w")
    text_file.write(description)
