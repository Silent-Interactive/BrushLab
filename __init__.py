bl_info = {
    "name": "BrushLab",
    "author": "Silent Interactive, Aman",
    "description": "Create sculpt brushes and asset-ready tools from image files",
    "location": "View3D > Sidebar > BrushLab",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "category": "Sculpt",
}

import bpy
from . import panel, operators

classes = operators.classes + panel.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.brushlab_folder_path = bpy.props.StringProperty(
        name="Folder Path",
        description="Select folder for BrushLab",
        subtype='DIR_PATH'
    )
    print("BrushLab enabled")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.brushlab_folder_path
    print("BrushLab disabled")

if __name__ == "__main__":
    register()
