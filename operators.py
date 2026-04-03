import bpy

class BRUSHLAB_OT_ButtonOperator(bpy.types.Operator):
    bl_idname = "brushlab.button_operator"
    bl_label = "Press Me"
    bl_description = "This is a test button"

    def execute(self, context):
        self.report({'INFO'}, "BrushLab button pressed!")
        print("BrushLab button pressed!")
        return {'FINISHED'}

# List of classes in this file
classes = [BRUSHLAB_OT_ButtonOperator]
