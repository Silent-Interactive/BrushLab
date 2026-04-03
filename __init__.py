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

    # Existing path property
    bpy.types.Scene.brushlab_folder_path = bpy.props.StringProperty(
        name="Folder Path",
        subtype='DIR_PATH'
    )

    # NEW: File type filter
    bpy.types.Scene.brushlab_file_ext = bpy.props.EnumProperty(
        name="File Type",
        items=[
            ('ALL', "All Images", "Process all supported images"),
            ('.jpg', "JPG", ""),
            ('.png', "PNG", ""),
            ('.exr', "EXR", ""),
            ('.tiff', "TIFF", "")
        ],
        default='ALL'
    )

    bpy.types.Scene.brushlab_use_subfolders = bpy.props.BoolProperty(
        name="Include Subfolders",
        default=True
    )

    bpy.types.Scene.brushlab_is_VDM = bpy.props.BoolProperty(
            name="VDM",
            default=True
    )

    bpy.types.Scene.brushlab_use_subfolder_name_as_prefix = bpy.props.BoolProperty(
            name="Use subfolder name as prefix",
            default=True
    )

    bpy.types.Scene.brushlab_mapping = bpy.props.EnumProperty(
        name="Mapping",
        items=[
            ('AREA_PLANE', "Area Plane", ""),
            ('TILED', "Tiled", ""),
            ('STENCIL', "Stencil", ""),
            ('RANDOM', "Random", "")
        ],
        default='AREA_PLANE'
    )

    bpy.types.Scene.brushlab_stroke = bpy.props.EnumProperty(
        name="Stroke",
        items=[
            ('ANCHORED', "Anchored", ""),
            ('SPACE', "Space", ""),
            ('DRAG_DOT', "Drag Dot", ""),
            ('AIRBRUSH', "Airbrush", "")
        ],
        default='ANCHORED'
    )

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.brushlab_folder_path
    del bpy.types.Scene.brushlab_file_ext
    del bpy.types.Scene.brushlab_use_subfolders
    del bpy.types.Scene.brushlab_mapping
    del bpy.types.Scene.brushlab_stroke
