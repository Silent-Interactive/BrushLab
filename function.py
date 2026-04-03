import os
import bpy

def create_brushes_from_folder(folder_path, extension='ALL', use_subfolders=True, mapping='AREA_PLANE', stroke='ANCHORED', isVDM=True, useSubfolderNameAsPrefix=True):
    if not folder_path or not os.path.exists(folder_path):
        print("Invalid folder path!")
        return

    files_to_process = []

    if use_subfolders:
        for root, dirs, files in os.walk(folder_path):
            for f in files:
                files_to_process.append((os.path.join(root, f), root))
    else:
        files_to_process = [(os.path.join(folder_path, f), folder_path)
                            for f in os.listdir(folder_path)
                            if os.path.isfile(os.path.join(folder_path, f))]

    for file_path, current_dir in files_to_process:
        file_name = os.path.basename(file_path)
        ext = os.path.splitext(file_name)[1].lower()

        if extension != 'ALL' and ext != extension:
            continue

        if ext not in ['.jpg', '.jpeg', '.png', '.exr', '.tiff', '.tif', '.bmp']:
            continue

        base_name = os.path.splitext(file_name)[0]
        brush_name = base_name

        if useSubfolderNameAsPrefix and use_subfolders:
            root_norm = os.path.normpath(folder_path)
            current_norm = os.path.normpath(current_dir)

            if current_norm != root_norm:
                subfolder_name = os.path.basename(current_norm)
                brush_name = f"{subfolder_name}_{base_name}"

        try:
            brush = bpy.data.brushes.new(name=brush_name, mode='SCULPT')
            img = bpy.data.images.load(file_path)
            tex = bpy.data.textures.new(name=brush_name + "_Tex", type='IMAGE')
            tex.image = img
            brush.texture = tex

            if hasattr(brush, "texture_slot"):
                brush.texture_slot.map_mode = mapping

            brush.stroke_method = stroke

            if hasattr(brush, "use_color_as_displacement"):
                brush.use_color_as_displacement = isVDM

            # Asset Marking
            if brush.asset_data is None:
                brush.asset_mark()
                # Use the original image as the asset preview
                with bpy.context.temp_override(id=brush):
                    bpy.ops.ed.lib_id_load_custom_preview(filepath=file_path)

            print(f"Successfully Created: {brush_name}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")
