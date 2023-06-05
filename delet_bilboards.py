bl_info = {
    "name": "Delete billboards",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 5, 1),
    "location": "3D View > Object > Delete billboards with 100 or fewer vertices",
    "description": "Delete billboards with 100 or fewer vertices",
    "category": "Object"
}
import bpy


def delete_billboards(vertex_lim):
    bpy.ops.object.select_all(action='DESELECT')

    # Select all objects
    bpy.ops.object.select_by_type(type='MESH')
    
    # Delete billboards with 4 or fewer vertices
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            vertex_count = len(obj.data.vertices)
            if vertex_count <= vertex_lim:
                obj.select_set(True)
            else:
                obj.select_set(False)

    bpy.ops.object.delete()


class DeleteBillboardsOperator(bpy.types.Operator):
    bl_idname = "object.delete_billboards"
    bl_label = "Delete Billboards"
    bl_description = "Delete billboards with 100 or fewer vertices"
    bl_options = {'REGISTER', 'UNDO'}
    print("hi")
    vertex_lim: bpy.props.FloatProperty(
        name="Vertex Threshold",
        description="Delete objects below this vertex count",
        default=100,
        min=0.0
    )
    def execute(self, context):
        delete_billboards(self.vertex_lim)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(DeleteBillboardsOperator.bl_idname)
def register():
    bpy.utils.register_class(DeleteBillboardsOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(DeleteBillboardsOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()