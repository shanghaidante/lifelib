import os.path
import pickle
import pathlib

from lifelib.projects.simplelife import simplelife
from tests.data.generate_testdata import round_signif

model = simplelife.build(load_saved=False)

testdata = \
    str(pathlib.Path(__file__).parents[1].joinpath('data/data_simplelife'))


def test_simpleflie():
    data = []
    proj = model.Projection
    for i in range(10, 301, 10):
        data.append(round_signif(proj(i).pv_NetLiabilityCashflow(0), 10))

    with open(testdata, 'rb') as file:
        data_saved = pickle.load(file)

    assert data == data_saved


