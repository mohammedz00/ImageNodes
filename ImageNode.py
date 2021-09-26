
bl_info = {
    "name": "Shader Library",
    "author": "Zenudeen Shehbaz",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D",
    "description": "Adds often used image nodes",
    "warning": "",
    "wiki_url": "",
    "category": "Add Image Nodes",
}


#Import bpy

import bpy


#Creating main panel


class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Image Texture"
    bl_idname = "PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Image Texture"

    def draw(self, context):
        layout = self.layout
        

        
        row = layout.row()
        row.label(text = 'Image')
        row.operator('shader.image_operator')
        
        
        
class Shader_OT_Image(bpy.types.Operator):
    bl_label = "Image"
    bl_idname = 'shader.image_operator'
    
    def execute(self,context):
        
        #Creating new shader and calling it Image
        material_image = bpy.data.materials.new(name = 'Image')
        #Enabling use nodes
        material_image.use_nodes = True
        material_image.node_tree.nodes.remove(material_image.node_tree.nodes.get('Principled BSDF'))
        #Creating a reference to the Material Output
        material_output = material_image.node_tree.nodes.get('Material Output')
        #Set location of node
        material_output.location = (500, 500)
        
        # Adding Image Texture node

        image_node = material_image.node_tree.nodes.new('ShaderNodeTexImage')
#       Setting location of node
        image_node.location = (-1000, 600)
 
        image_node.select = False
        
   
   
        # Adding Color Ramp node

        colorramp_node = material_image.node_tree.nodes.new('ShaderNodeValToRGB')
#       Setting location of node
        colorramp_node.location = (-500, 400)
        colorramp_node.select = False


        # Adding 2nd Color Ramp node
        
        colorrampp_node = material_image.node_tree.nodes.new('ShaderNodeValToRGB')
#       Setting location of node
        colorrampp_node.location = (-600, 0)
#        default selection is off
        colorrampp_node.select = False
        
        
        
        
        # Adding Bump node
        
        bump_node = material_image.node_tree.nodes.new('ShaderNodeBump')
#       Setting location of node
        bump_node.location = (-200, 100)
#         default selection is off
        bump_node.select = False
        
        
        
        
        # Adding PRINCIPLED node
        
        principled_node = material_image.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
#       Roughness and metallic default values set
        principled_node.inputs[4].default_value = 0.000
        principled_node.inputs[7].default_value = 0.500
#       Setting location of node
        principled_node.location = (100, 650)
#        default selection is off
        principled_node.select = False
        
        
        
#        Node Links
        
        material_image.node_tree.links.new(image_node.outputs[0], principled_node.inputs[0])
        material_image.node_tree.links.new(image_node.outputs[0], colorramp_node.inputs[0])
        material_image.node_tree.links.new(image_node.outputs[0], colorrampp_node.inputs[0])
        material_image.node_tree.links.new(colorrampp_node.outputs[0], bump_node.inputs[2])
        material_image.node_tree.links.new(colorramp_node.outputs[0], principled_node.inputs[7])
        material_image.node_tree.links.new(bump_node.outputs[0], principled_node.inputs[20])
        material_image.node_tree.links.new(principled_node.outputs[0], material_output.inputs[0])
                
                
 
        
        bpy.context.object.active_material = material_image




        
        return {'FINISHED'}
        
        
        
        
        
def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(Shader_OT_Image)
    


def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(Shader_OT_Image)


if __name__ == "__main__":
    register()
