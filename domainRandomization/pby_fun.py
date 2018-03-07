import bpy
import os
import random as rand
import texture_test as tex
from math import sin, cos, pi, asin, acos, atan2

def create_random_cube(
        objID='', 
        R=[0,1],
        range_theta=[0,2*pi], 
        range_phi=[0,pi],
        size = [0.01, 0.03]
        ):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    theta = ((range_theta[1]-range_theta[0])*rand.random()+range_theta[0]); 
    phi = ((range_phi[1]-range_phi[0])*rand.random()+range_phi[0]);
    R = R[0]+(R[1]-R[0])*rand.random()
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    loc = (x,y,z)

    # create a cube object
    bpy.ops.mesh.primitive_cube_add( 
        location= loc,
        radius=rand.uniform(size[0], size[1])
        )
    bpy.ops.transform.rotate(
            value=rand.random()*3.14, 
            axis=(rand.random(),rand.random(), rand.random()),
            constraint_orientation='GLOBAL',
            mirror=False,
            proportional='DISABLED',
            proportional_edit_falloff='SMOOTH',
            proportional_size=1
            )
    

    # create and add a texture and color
    # bpy.ops.material.new()
    # mat = tex.createMaterials()
    # bpy.data.objects['Cube'].data.materials.append(mat)
    # if not len(objID):
    #     # mat = bpy.data.materials['Material']
    #     # mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     mat = tex.createMaterials()
    #     bpy.data.objects['Cube'].data.materials.append(mat)
    #     print(objID, 'hello')
    # else:
    #     # mat = bpy.data.materials['Material.'+objID]
    #     # mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     mat = tex.createMaterials()
    #     bpy.data.objects['Cube.'+objID].data.materials.append(mat)
    #     print(objID)

def create_random_sphere(
        objID='', 
        R=[0.0,1.0],
        range_theta=[0,2*pi], 
        range_phi=[0,pi],
        size = [0.01, 0.03]
        ):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    theta = ((range_theta[1]-range_theta[0])*rand.random()+range_theta[0]); 
    phi = ((range_phi[1]-range_phi[0])*rand.random()+range_phi[0]);
    R = R[0]+(R[1]-R[0])*rand.random()
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    loc = (x,y,z)    
    
    # create a cube object
    bpy.ops.mesh.primitive_ico_sphere_add( 
        location= loc,
        size=rand.uniform(size[0], size[1])
        )
    bpy.ops.transform.rotate(
            value=rand.random()*3.14, 
            axis=(rand.random(),rand.random(), rand.random()),
            constraint_orientation='GLOBAL',
            mirror=False,
            proportional='DISABLED',
            proportional_edit_falloff='SMOOTH',
            proportional_size=1
            )
    

    # create and add a texture and color
    bpy.ops.material.new()
    if not len(objID):
        # mat = bpy.data.materials['Material']
        # mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
        mat = tex.createMaterials()
        bpy.data.objects['Icosphere'].data.materials.append(mat)
    else:
        # mat = bpy.data.materials['Material.'+objID]
        # mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
        mat = tex.createMaterials()
        bpy.data.objects['Icosphere.'+objID].data.materials.append(mat)


def create_flat_background():
    """
    create a background composed of 3 planes
    """
    N = 30.48
    bpy.ops.mesh.primitive_plane_add( 
            radius=N, 
            enter_editmode=False, 
            location=(0,0,0),
            rotation=(0,0,0),
            layers=(
                 True, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False
                )
            )

def clean_up_scene():
    for scene in bpy.data.scenes:

        for obj in scene.objects:
            scene.objects.unlink(obj)

    # only worry about data in the startup scene
    for bpy_data_iter in (
        bpy.data.objects,
        bpy.data.meshes,
        bpy.data.lamps,
        bpy.data.cameras,
        ):
        for id_data in bpy_data_iter:
            bpy_data_iter.remove(id_data)
    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 0.01


def create_camera(
        R=8,
        range_theta=[0,2*pi], 
        range_phi=[0,pi],
        view_range=[40,50]
        ):
    scene = bpy.context.scene

    # create camera datablock
    cam_data = bpy.data.cameras.new(name="Camera")

    # create camera object with the camera data block
    cam_object = bpy.data.objects.new(name="Camera", object_data=cam_data)

    # Link camera object to the scene so it'll appear in the scene
    scene.objects.link(cam_object)
    cam_object.select = True

    # Place the camera in a random location within the given range
    theta = ((range_theta[1]-range_theta[0])*rand.random()+range_theta[0]); 
    phi = ((range_phi[1]-range_phi[0])*rand.random()+range_phi[0]);
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    cam_object.location = (x,y,z)

    # set up camera focal properties
    cam_object.data.stereo.convergence_distance = 10000
    cam_object.data.angle = ((view_range[1]-view_range[0])*rand.random()+view_range[0])*pi/180
    cam_object.data.stereo.interocular_distance = 0.3
    
    # Aim camera at the origin
    zang = atan2(y,x)
    xang = acos(z/R)
    if ( z<0):
        cam_object.rotation_euler = (xang, 0, pi-zang)
    elif(x>0 and y>0 and z>0):
        cam_object.rotation_euler = (xang, 0, pi/2+zang)
    else:
        cam_object.rotation_euler = (xang, 0, -zang)

    cam_object.select = False

    return cam_object

def create_lamp( 
        R=15*30.48,
        range_theta=[0,2*pi], 
        range_phi=[0,pi],
        intensity = 5):
    scene = bpy.context.scene

    # Create new lamp datablock
    lamp_data = bpy.data.lamps.new(name="New Lamp", type='AREA')

    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)

    # Link lamp object to the scene so it'll appear in this scene
    scene.objects.link(lamp_object)

    # Place lamp to a specified location
    theta = ((range_theta[1]-range_theta[0])*rand.random()+range_theta[0]); 
    phi = ((range_phi[1]-range_phi[0])*rand.random()+range_phi[0]);
    # x = R*cos(theta)*sin(phi)
    # y = R*sin(theta)*sin(phi)
    # z = R*cos(phi)
    lamp_object.location = (0,0,30.48*10)
    lamp_object.data.energy = intensity
    lamp_object.data.distance =90
    lamp_object.data.gamma = 0.9
    lamp_object.data.shadow_method = "RAY_SHADOW"
    lamp_object.data.shape= "RECTANGLE"
    lamp_object.data.size = 30.48*3
    lamp_object.data.size_y=30.48/2
    # And finally select it make active
    lamp_object.select = True
    scene.objects.active = lamp_object

    return scene
    
def render_scene( id="", ofilename='image'+str(id)+".png"):
    bpy.context.scene.render.resolution_x = 227
    bpy.context.scene.render.resolution_y = 227
    bpy.context.scene.render.resolution_percentage = 100

    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.camera = bpy.data.objects['Camera'+str(id)]
    bpy.data.scenes['Scene'].render.filepath = ofilename
    bpy.ops.render.render(write_still=True)

def randomize_texture():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            mat = tex.createMaterials()
            # mat = bpy.data.materials.new(name='Material')
            # mat.diffuse_color = (rand.random(), rand.random(), rand.random())
            # tex = bpy.data.textures.new("SomeName", 'IMAGE')
            # slot = mat.texture_slots.add()
            # slot.texture = tex
            # obj.data.materials.append(mat)
            # bpy.ops.object.material_slot_remove()
            obj.data.materials.append(mat)
            
def import_rowdy(filename="RowdyWalker#6",
        R=[0,10],
        range_theta=[0,2*pi], 
        range_phi=[0,pi],
        size=[0.03,0.01]):
    # import rowdy in to the blender scene
    # print(filename)
    bpy.ops.import_mesh.stl(filepath=filename)
    filename = os.path.splitext(filename)[0]
    # print(filename)
    # capitalize the filename for some fkin reason
    obj = bpy.data.objects[filename]#.capitalize()]

    # scale the rowdy to an appropriate size
    obj.scale *= size[0] + (size[1]-size[0])*rand.random()

    # randomize the orientations of rowdy
    obj.rotation_euler = (pi*rand.random(), pi*rand.random(), pi*rand.random())

    # place the rowdy within the given bounds
    theta = ((range_theta[1]-range_theta[0])+range_theta[0])*rand.random(); 
    phi = ((range_phi[1]-range_phi[0])+range_phi[0])*rand.random();
    R = R[0]+(R[1]-R[0])*rand.random()
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    obj.location = (x,y,z)

