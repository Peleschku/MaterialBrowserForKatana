from __future__ import absolute_import

from PyQt5 import(
    QtCore,
    QtWidgets,
)

import QT4Widgets, QT4FormWidgets
importUtils
from Katana import (
    UI4,
    NodegraphAPI,
)

import UI4.FormMaster.PythonValuePolicy
from . import ScriptActions as SA

from functools import partial
from collections import OrderedDict

class MaterialExportEditor(QtWidgets.QWidget):
    def __init__(self, parent, node):
        node.upgrade()
        self.__node = node

        QtWidgets.QWidget.__init__(self, parent)
        QtWidgets.QVBoxLayout(self)

        self.__frozen = True
        self.__updateTabOnIdle = False

        # getting the widget factory
        factory = UI4.FormMaster.ParameterWidgetFactory
        # parameters to make (matches the ones specified in .Node)
        params = ['exportLocation', 'exportFormat']
        groupPolicyData = {
            '__childOrder': params,
        }

        # creating group policy to store parameter policies in
        groupPolicy = UI4.FormMaster.PythonValuePolicy.PythonValuePOlicy(
            'hiddenGroup', groupPolicyData)
        groupPolicy.getWidgetHints()['hideTitle'] = True

        # adding the Parameters
        for param in params:
            policy = UI4.FormMaster.CreateParameterPolicy(
                None, self.__node.getParameter(param))
            groupPolicy.addChildPolicy(policy)

        # build the widget
        w = factory.buildWidget(self, groupPolicy)
        # adding to the layout
        self.layout().addWidget(w)
