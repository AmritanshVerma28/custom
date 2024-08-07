import pickle

def save(obj, file_path):
    """
    Save a Python object to a pickle file.

    :param obj: Python object to be saved
    :param file_path: Path where the pickle file will be saved
    """
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)

def load(file_path):
    """
    Read a Python object from a pickle file and print the type of the data.

    :param file_path: Path to the pickle file
    :return: The Python object read from the pickle file
    """
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
        print(f'The type of the data is: {type(data)}')
        return data

def concater(dfs,axis=1):
    dfs_new = []
    for df in dfs:
        df.reset_index(inplace=True,drop=True)
        dfs_new.append(df)
    op = pd.concat(dfs_new,axis=1)
    return op
