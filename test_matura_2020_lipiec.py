from unittest import TestCase
from matura_2020_lipiec import matura_2020_lipiec


class TestMatura2020Lipiec(TestCase):
    def test_zadanie_1(self):
        expected1 = """GYJ959787
JOK786969"""
        gotten1 = matura_2020_lipiec().zadanie4_1()
        self.assertEqual(expected1,gotten1)
    def test_zadanie_2(self):
        expected2 = """MBF340043
JKJ452719
GFG148345
AXA231829
KIK866983
LOL695279"""
        gotten2 = matura_2020_lipiec().zadanie4_2()
        self.assertEqual(expected2,gotten2)
        print(gotten2)
    def test_zadanie_3(self):
        expected3 = """LIK235378
MBF340043
HFG378931
KIJ511146
NUK840936
OKH427482
RTS278686"""
        gotten3 = matura_2020_lipiec().zadanie4_3()
        self.assertEqual(expected3,gotten3)