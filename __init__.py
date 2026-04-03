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

def register():
    print("BrushLab enabled")


def unregister():
    print("BrushLab disabled")
