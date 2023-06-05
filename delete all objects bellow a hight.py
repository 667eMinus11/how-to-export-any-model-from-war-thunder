bl_info = {
    "name": "Delete Objects Below Height",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "3D View > Object > Delete Objects Below Height",
    "description": "Delete objects below a certain height",
    "category": "Object"
}

import bpy

def delete_objects_below_height(threshold_height):
    scene = bpy.context.scene
    objects_to_delete = []

    for obj in scene.objects:
        if obj.type == 'MESH' and obj.location.z < threshold_height:
            objects_to_delete.append(obj)

    bpy.ops.object.select_all(action='DESELECT')

    for obj in objects_to_delete:
        obj.select_set(True)

    bpy.ops.object.delete()

class DeleteObjectsBelowHeightOperator(bpy.types.Operator):
    bl_idname = "object.delete_objects_below_height"
    bl_label = "Delete Objects Below Height"
    bl_options = {'REGISTER', 'UNDO'}

    threshold_height: bpy.props.FloatProperty(
        name="Threshold Height",
        description="Delete objects below this height",
        default=5.0,
        min=0.0
    )

    def execute(self, context):
        delete_objects_below_height(self.threshold_height)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(DeleteObjectsBelowHeightOperator.bl_idname)

def register():
    bpy.utils.register_class(DeleteObjectsBelowHeightOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(DeleteObjectsBelowHeightOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
