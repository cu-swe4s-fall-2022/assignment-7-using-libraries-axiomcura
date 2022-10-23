import pickle
import unittest

import numpy as np

import data_processor as dp


class TestMatrixGeneration(unittest.TestCase):
    def test_make_matrix_1(self) -> None:
        """makes matrix with integer"""

        # setting input parameters
        n_rows = 10
        n_cols = 10

        # loading true matrix
        with open("single_mat.pickle", "wb") as f:
            true_mat = pickle.load(f)

        # generating test matrix
        test_mat = dp.get_random_matrix(n_rows, n_cols)

        # checking shape, and data type
        self.assertEqual(type(true_mat), type(test_mat))
        self.assertEqual(true_mat.shape, test_mat.shape)

    def test_make_matrix_2(self) -> None:
        """Make matrix with 1 non integer types"""

        # setting input parameters
        n_rows = 10.0
        n_cols = 10

        # test
        self.assertRaises(TypeError, dp.get_random_matrix, n_rows, n_cols)

    def test_make_matrix_3(self) -> None:
        """Make matrix with 2 non integer types"""

        # setting input parameters
        n_rows = 10.0
        n_cols = 10.0

        # test
        self.assertRaises(TypeError, dp.get_random_matrix, n_rows, n_cols)

    def test_make_matrix_4(self) -> None:
        """Make matrix with string number types"""

        # setting input parameters
        n_rows = "10"
        n_cols = "10"

        # test
        self.assertRaises(TypeError, dp.get_random_matrix, n_rows, n_cols)

    def test_make_matrix_5(self) -> None:
        """Make matrix with row numbers lower than 0"""

        # setting input parameters
        n_rows = -1
        n_cols = 10

        # test
        self.assertRaises(ValueError, dp.get_random_matrix, n_rows, n_cols)

    def test_make_matrix_5(self) -> None:
        """Make matrix with column numbers lower than 0"""

        # setting input parameters
        n_rows = 10
        n_cols = -1

        self.assertRaises(ValueError, dp.get_random_matrix, n_rows, n_cols)

    def test_making_multiple_matrix(self) -> None:
        """Generates 100 matrices and checks for type and shape. There is a
        10% probability where one of the inputs will be a float"""

        # simulating 100 matrices generation
        for _ in range(100):

            # setting float probability
            floats_exists = False
            float_proba_threshold = 0.10
            n_rows_float_proba = round(np.random.random(), 3)
            n_cols_float_proba = round(np.random.random(), 3)

            # setting parameters
            n_rows = np.random.randint(1, 100)
            n_cols = np.random.randint(1, 100)

            # change parameters to float based on probability
            if n_rows_float_proba < 0.10:
                n_rows = np.random.random() * 100
                floats_exists = True
            if n_cols_float_proba < float_proba_threshold:
                n_cols = np.random.random() * 100
                floats_exists = True

            # if the a float type is present, check for exception raises
            if floats_exists is True:

                # reset float exist state
                floats_exists = False

                # create matrix with float types
                self.assertRaises(
                    TypeError, dp.get_random_matrix, n_rows, n_cols
                )

            else:

                # setting truths
                true_shape = (n_rows, n_cols)
                true_type_str = "<class 'numpy.ndarray'>"

                matrix = dp.get_random_matrix(n_rows, n_cols)
                test_type_str = str(type(matrix))
                test_shape = matrix.shape

                # testing
                self.assertEqual(true_shape, test_shape)
                self.assertEqual(true_type_str, test_type_str)


    @classmethod
    def setUp(cls) -> None:

        # generating file names
        cls.single_mat = "single_mat.pickle"

        # generating datasets
        with open(cls.single_mat, "wb") as mat_file:
            mat = np.random.rand(10, 10)
            pickle.dump(mat, mat_file)
