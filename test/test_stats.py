import unittest
from stats import stats
import numpy as np

class TestComStats(unittest.TestCase):

    def setUp(self):
        self.input_set = np.array([
            [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
            [2, 1, 2, 3, 3, 0, 1, 0, 0, 0, 4, 1, 2, 4, 4],
            [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [3, 0, 1, 3, 0, 0, 2, 1, 2, 3, 3, 1, 0, 0, 2]
        ])
        self.weights = np.array([1, 0.1, 0.2, 0.3, 2, 0.1, 0.1, 2, 0.1, 0.1])

    def test_unweighted_t_test(self):
        expected_p_values = [[ 1.        ,  0.00353093,  1.        ,  0.00961514],
                             [ 0.00353093,  1.        ,  0.00353093,  0.43711409],
                             [ 1.        ,  0.00353093,  1.        ,  0.00961514],
                             [ 0.00961514,  0.43711409,  0.00961514,  1.        ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.t_test(self.input_set)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_unweighted_t_test_one_sided(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.t_test(self.input_set, None, {'paired': False, 'equal_variance': False}, True)
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_unweighted_t_test_equal_variance(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.t_test(self.input_set, None, {'paired': False, 'equal_variance': True}, False)
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_unweighted_t_test_equal_variance_one_sided(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.t_test(self.input_set, None, {'paired': False, 'equal_variance': True}, True)
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_weighted_t_test(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.t_test(self.input_set, self.weights, {'paired': False, 'equal_variance': False})
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())


    def test_weighted_t_test_one_sided(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.t_test(self.input_set, self.weights, {'paired': False, 'equal_variance': False}, True)
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_paired_t_test(self):
        expected_p_values = [[     np.nan,  0.00284684,  1.        ,  0.00168927],
                             [ 0.00284684,      np.nan,  0.00946889,  0.4242752 ],
                             [ 1.        ,  0.00946889,      np.nan,  0.01599862],
                             [ 0.00168927,  0.4242752 ,  0.01599862,      np.nan]]
        expected_scores = [[     np.nan, -3.60906033,  0.        , -3.87298335],
                           [ 3.60906033,      np.nan,  3.00438276,  0.82305489],
                           [ 0.        , -3.00438276,      np.nan, -2.73861279],
                           [ 3.87298335, -0.82305489,  2.73861279,      np.nan]]
        p_values, scores = stats.t_test(self.input_set, None, {'paired': True, 'equal_variance': False})
        print("test_paired_t_test", p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_paired_t_test_one_sided(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.t_test(self.input_set, None, {'paired': True, 'equal_variance': False}, True)
        print(" test_paired_t_test_one_sided")
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_percentage_t_test(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.percentage_t_test(self.input_set)
        print(" test_percentage_t_test")
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_percentage_t_test_one_sided(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.percentage_t_test(self.input_set, None, {'distribution': 't'}, True)
        print(" test_percentage_t_test_one_sided")
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_weighted_percentage_t_test_one_sided(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.percentage_t_test(self.input_set, self.weights, {'distribution': 't'}, True)
        print(" test_weighted_percentage_t_test_one_sided")
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_weighted_percentage_t_test_z_distribution(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.percentage_t_test(self.input_set, self.weights, {'distribution': 'z'})
        print(" test_weighted_percentage_t_test_z_distribution")
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())

    def test_weighted_percentage_t_test_one_sided_z_distribution(self):
        expected_p_values = [[ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00176546,  0.5       ,  0.00176546,  0.21855705],
                             [ 0.5       ,  0.00176546,  0.5       ,  0.00480757],
                             [ 0.00480757,  0.21855705,  0.00480757,  0.5       ]]
        expected_scores = [[ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 3.38132124,  0.        ,  3.38132124,  0.78881064],
                           [ 0.        , -3.38132124,  0.        , -2.88675135],
                           [ 2.88675135, -0.78881064,  2.88675135,  0.        ]]
        p_values, scores = stats.percentage_t_test(self.input_set, self.weights, {'distribution': 'z'}, True)
        print(" test_weighted_percentage_t_test_one_sided_z_distribution")
        print(p_values)
        print(scores)
        self.assertTrue((p_values.round(8) == expected_p_values).all())
        self.assertTrue((scores.round(8) == expected_scores).all())