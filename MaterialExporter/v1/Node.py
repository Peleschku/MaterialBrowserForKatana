from __future__ import absolute_import

import logging
from collections import OrderedDict

import Utils
from Katana import NodegraphAPI

from .Upgrade import Upgrade
from . import ScriptActions as SA

log = logging.getLogger("MaterialExport.Node")

attrTypes = {'IntAttribute':'integer', 'DoubleAttribute':'double',
             'FloatAttribute':'float'
}

inTime = NodegraphAPI.getRootNode().getParameter('inTime').getValue(0)

class MaterialExportNode(NodegraphAPI.SuperTool):
    def __init__(self):

        self.addInputPort('in')
        self.addOutputPort('out')

        
        rootParameters = self.getParameters()
        rootParameters.createChildNumber('version', 1)

        #specifying if saving as a .klf or .usda file
        rootParameters.createChildString('exportFormat', '')
        # specifying location to save material to
        rootParameters.createChildString('exportLocation', '')


        self.__buildDefaultNetwork()

    def __buildDefaultNetwork(self):

        # spacing to be used for layout within the node
        # TODO: swap this out with auto layout later
        yspacing = -50
        xspacing = 100

        dotNode = NodegraphAPI.CreateNode('dot', self)
        self.getSendPort(self.getPortByIndex(0).getName()).connect(
            dotNode.getInputPortByIndex(0))
        
        ''' TODO: set up if statement where a LookfileBake node is made if
         .klf is selected, or a UsdMaterialBake if .usda/.usd/.usdz is selected
         in the UI
        '''



