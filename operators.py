import bpy
from .function import create_stencil_brushes_from_jpg

class BRUSHLAB_OT_Generate(bpy.types.Operator):
    bl_idname = "brushlab.generate"
    bl_label = "Generate"
    bl_description = "Generate brushes from selected folder"

    def execute(self, context):
        scene = context.scene
        path = scene.brushlab_folder_path
        self.report({'INFO'}, f"BrushLab button pressed! Path: {path}")
        print(f"BrushLab button pressed! Path: {path}")

        create_stencil_brushes_from_jpg(path)

        return {'FINISHED'}

# List of classes in this file
classes = [BRUSHLAB_OT_Generate]
