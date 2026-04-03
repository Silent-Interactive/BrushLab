import bpy

class BRUSHLAB_OT_Generate(bpy.types.Operator):
    bl_idname = "brushlab.generate"
    bl_label = "Generate"
    bl_description = "Generate brushes from selected folder"

    def execute(self, context):
        scene = context.scene
        path = scene.brushlab_folder_path
        self.report({'INFO'}, f"BrushLab button pressed! Path: {path}")
        print(f"BrushLab button pressed! Path: {path}")
        return {'FINISHED'}

# List of classes in this file
classes = [BRUSHLAB_OT_Generate]
