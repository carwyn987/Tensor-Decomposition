import sys
import os
import unittest

# Add lib to modules path irrespective of cwd
sys.path.insert(0, os.path.join("/", *os.path.realpath(__file__).split("/")[:-2]))
from lib import convert

# (X,Y,Z) --> (Lat,Lon,Alt)
# (2,2,2) dec. sig. figs. --> (7,7,2) sig.figs.
# Data from reputible online source
test_ecef_to_lla_data = {
    (6378137, 0, 0): (0, 0, 0),
    (-1890786.68, 5194893.71, -3170393.24): (-30, 110, 39),
    (-111671.17, 1949.23, 6355776.63): (89, 179, -1),
}


def test_ECEFtoLLA():
    for ecef in test_ecef_to_lla_data:

        lla_point = convert.ECEFtoLLA(list(ecef))
        ecef_point = test_ecef_to_lla_data[ecef]

        # Approximate equality to 0.01
        delta = 0.01

        unittest.TestCase().assertAlmostEqual(lla_point[0], ecef_point[0], delta=delta)
        unittest.TestCase().assertAlmostEqual(lla_point[1], ecef_point[1], delta=delta)
        unittest.TestCase().assertAlmostEqual(lla_point[2], ecef_point[2], delta=delta)
