from __future__ import absolute_import

import Katana
from . import v1 as MaterialExporter

if MaterialExporter:
    PluginRegistry = [
        ("SuperTool", 2, "MaterialExporter",
            (MaterialExporter.MaterialExportNode,
                MaterialExporter.GetEditor)),
                
    ]