import bpy
from .operators import BRUSHLAB_OT_Generate

class BRUSHLAB_PT_SidePanel(bpy.types.Panel):
    bl_label = "BrushLab Panel"
    bl_idname = "BRUSHLAB_PT_sidepanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BrushLab"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Select Folder:")
        layout.prop(scene, "brushlab_folder_path", text="")

        layout.operator("brushlab.generate", text="Generate")

# List of classes in this file
classes = [BRUSHLAB_PT_SidePanel]
