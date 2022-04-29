''' This file contains test functions for the network generator '''
import pytest
from pandas.testing import assert_frame_equal
import pandas as pd
import pandas.testing
import numpy as np
import src.network_generator.network_generator as ng




class TestClass:
    def test_drop_nas_df(self):
        df = pd.DataFrame({
            'column1': [1, 2, np.NaN, '', 'test']
        })
        expected = pd.DataFrame({
            'column1': [1.0, 2.0, 'test']
        })

        actual = ng.drop_nas_df(df)
        np.array_equal(expected, actual)

    def test_lemmatize_with_postag(self):
        sentence = 'sorry missed dinner you well celebrate shortly enjoy trip much love meema'
        expected = 'sorry miss dinner you well celebrate shortly enjoy trip much love meema'
        lemmatized_list = ng.lemmatize_with_postag(sentence)
        assert expected == lemmatized_list


