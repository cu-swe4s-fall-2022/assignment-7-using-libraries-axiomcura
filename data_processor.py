import numpy as np


def get_random_matrix(num_rows: int, num_columns: int) -> np.ndarray:
    """Generates a random matrix that is sampled from a uniform range (0, 1] with

    Parameters:
    ----------
    num_rows : int
        Number of rows in your matrix
    num_columns : int
        Number of columns in your matrix

    Returns:
    -------
    np.ndarray
        Randomly generated matrix based on user provided dimensions.

    Raises:
    ------
    TypeError
        Raised if either num_rows or num_columns are not integer types
    ValueError
        Raised if either num_rows or num_columns are less than 0
    """

    # type checking
    if not isinstance(num_rows, int):
        e_msg = f"num_rows must be a integer not {type(num_rows)}"
        raise TypeError(e_msg)
    elif not isinstance(num_columns, int):
        e_msg = f"num_columns must be an integer not {type(num_rows)}"
        raise TypeError(e_msg)

    # checking num_rows and num_columns values
    if num_rows < 0:
        raise ValueError("Number of rows must be positive")
    elif num_columns < 0:
        raise ValueError("Number of columns must be positive")

    # generating matrix
    matrix = np.random.rand(num_rows, num_columns)

    return matrix


def get_file_dimensions(file_name):
    return (0, 0)


def write_matrix_to_file(num_rows, num_columns, file_name):
    return None
