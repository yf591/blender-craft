import bpy

# Clear existing objects (optional)
if bpy.context.mode == 'OBJECT':
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
elif bpy.context.mode == 'EDIT': # If in edit mode, switch to object mode first
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
cube = bpy.context.active_object
if cube: # Check if an object is active/selected
    cube.name = "MyCube"

    # Create and apply material
    mat = bpy.data.materials.new(name="BlueMaterial")
    mat.use_nodes = True
    principled_bsdf = mat.node_tree.nodes.get('Principled BSDF')
    if principled_bsdf:
        principled_bsdf.inputs['Base Color'].default_value = (0.0, 0.3, 0.8, 1.0)  # Blue color (RGBA)

    # Apply material to the object
    if not cube.data.materials:
        cube.data.materials.append(mat)
    else:
        cube.data.materials[0] = mat

# Change viewport shading to Material Preview
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.shading.type = 'MATERIAL'
                break
        break

print("Blue cube created!")