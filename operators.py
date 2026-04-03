import bpy
from .function import create_brushes_from_folder

class BRUSHLAB_OT_Generate(bpy.types.Operator):
    bl_idname = "brushlab.generate"
    bl_label = "Generate"

    def execute(self, context):
        s = context.scene

        create_brushes_from_folder(
            folder_path=s.brushlab_folder_path,
            extension=s.brushlab_file_ext,
            use_subfolders=s.brushlab_use_subfolders,
            mapping=s.brushlab_mapping,
            stroke=s.brushlab_stroke,
            isVDM=s.brushlab_is_VDM,
            useSubfolderNameAsPrefix=s.brushlab_use_subfolder_name_as_prefix
        )

        self.report({'INFO'}, "Brush generation complete!")
        return {'FINISHED'}

classes = [BRUSHLAB_OT_Generate]
