import bpy

class BRUSHLAB_PT_SidePanel(bpy.types.Panel):
    bl_label = "BrushLab"
    bl_idname = "BRUSHLAB_PT_sidepanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BrushLab"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        col = layout.column(align=True)
        col.label(text="Folder Settings:")
        col.prop(scene, "brushlab_folder_path", text="")
        col.prop(scene, "brushlab_use_subfolders")
        col.prop(scene, "brushlab_is_VDM")
        col.prop(scene, "brushlab_use_subfolder_name_as_prefix")

        col.prop(scene, "brushlab_file_ext")

        layout.separator()

        col = layout.column(align=True)
        col.label(text="Brush Settings:")
        col.prop(scene, "brushlab_mapping")
        col.prop(scene, "brushlab_stroke")

        layout.separator()
        layout.operator("brushlab.generate", text="Generate Brushes", icon='BRUSH_DATA')

classes = [BRUSHLAB_PT_SidePanel]
