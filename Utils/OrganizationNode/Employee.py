# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/21 11:54
# __fileName__ : GoldenCoordinateV2 Employee.py
# __devIDE__ : PyCharm
from Utils.OrganizationNode.Composite import Composite

class Employee(Composite):
    def __init__(self, data):
        super().__init__(data)

