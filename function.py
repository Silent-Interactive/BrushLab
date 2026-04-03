import os
import bpy

def create_stencil_brushes_from_jpg(folder_path):
    if not folder_path or not os.path.exists(folder_path):
        print("Invalid folder path!")
        return

    jpg_files = [f for f in os.listdir(folder_path)
                 if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(".jpg")]

    if not jpg_files:
        print("No .jpg files found in folder!")
        return

    for file_name in jpg_files:
        file_path = os.path.join(folder_path, file_name)
        brush_name = os.path.splitext(file_name)[0]

        brush = bpy.data.brushes.new(name=brush_name, mode='SCULPT')
        img = bpy.data.images.load(file_path)
        tex = bpy.data.textures.new(name=brush_name + "_Tex", type='IMAGE')
        tex.image = img

        brush.texture = tex

        if hasattr(brush, "texture_slot"):
            brush.texture_slot.map_mode = 'AREA_PLANE'
            brush.stroke_method = 'ANCHORED'

        if brush.asset_data is None:
            brush.asset_mark()

        print(f"Created stencil brush: {brush_name}")
