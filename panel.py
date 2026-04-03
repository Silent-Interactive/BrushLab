import bpy
from .operators import BRUSHLAB_OT_ButtonOperator

class BRUSHLAB_PT_SidePanel(bpy.types.Panel):
    bl_label = "BrushLab"
    bl_idname = "BRUSHLAB_PT_sidepanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BrushLab"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Welcome to BrushLab!")
        layout.operator("brushlab.button_operator", text="Dont do it!")

# List of classes in this file
classes = [BRUSHLAB_PT_SidePanel]
