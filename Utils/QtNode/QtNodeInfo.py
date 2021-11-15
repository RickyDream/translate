# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/15 15:45
# __fileName__ : GoldenCoordinateV2 QtNodeInfo.py
# __devIDE__ : PyCharm



from PySide2 import QtWidgets as qtw



class QtNodeInfo():

    def _getParents(self,widget:qtw.QWidget):
        parents = []
        parent = widget.parent()
        if parent:
            parents.append(parent)
            parents.extend(self._getParents(parent))
        return parents

    def getParents(self, widget):
        self._parents = self._getParents(widget)
        return self._parents
    def getParent(self):
        if not self._parents:
            return None
        else:
            for parent in self._parents:
                if parent.objectName().isupper():
                    return parent

qtNodeInfo = QtNodeInfo()



