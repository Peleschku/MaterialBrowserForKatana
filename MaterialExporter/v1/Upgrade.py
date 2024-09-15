from __future__ import absolute_import

from .Node import MaterialExportNode

def GetEditor():
    from .Editor import MaterialExportEditor
    return MaterialExportEditor