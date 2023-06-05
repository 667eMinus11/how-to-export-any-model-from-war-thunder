bl_info = {
    "name": "Delete All Materials",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Object > Delete All Materials",
    "description": "Deletes all materials from the scene, including unused materials",
    "category": "Object",
}

import bpy


class DeleteAllMaterialsOperator(bpy.types.Operator):
    """Operator to delete all materials from the scene, including unused materials"""
    bl_idname = "object.delete_all_materials"
    bl_label = "Delete All Materials"
    
    def execute(self, context):
        # Iterate over each material in the scene
        for material in bpy.data.materials:
            if material is not None:
                bpy.data.materials.remove(material)
        
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(DeleteAllMaterialsOperator.bl_idname)


def register():
    bpy.utils.register_class(DeleteAllMaterialsOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(DeleteAllMaterialsOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
