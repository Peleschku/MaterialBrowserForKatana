from __future__ import absolute_import

from Katana import NodeGraphAPI

def getRefNode(gnode, key):
    p = gnode.getParameter('node_'+key)
    if not p:
        return None
    
    return NodeGraphAPI.GetNode(p.getValue(0))

def AddNodeRefParam(destNode, paramName, node):
    param = destNode.getParameter(paramName)
    if not param:
        param = destNode.getParameters().createChildString(param)

        param.setExpression('getNode(%r).getNodeName()' % node.param)