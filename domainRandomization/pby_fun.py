import bpy
import os
import random as rand
from numpy.linalg import norm
import texture_test as tex
from math import sin, cos, pi, asin, acos, atan2


def create_random_cube(
        objID='',
        R=[0, 1],
        range_theta=[0, 2 * pi],
        range_phi=[0, pi],
        size=[0.01, 0.03]
):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    theta = ((range_theta[1] - range_theta[0]) * rand.random() + range_theta[0]);
    phi = ((range_phi[1] - range_phi[0]) * rand.random() + range_phi[0]);
    # R = R[0] + (R[1] - R[0]) * rand.random()
    # x = R*cos(theta)*sin(phi)
    # y = R*sin(theta)*sin(phi)
    # z= 3*30.48
    R = rand.uniform(size[0], size[1])
    x = rand.uniform(-14.6, 14.6)
    y = rand.uniform(-14.6, 14.6)
    z = 3 * 30.48+R

    loc = (x, y, z)

    # create a cube object
    bpy.ops.mesh.primitive_cube_add(
        location=loc,
        radius=R
    )
    bpy.ops.transform.rotate(
        value=rand.random() * 3.14,
        axis=(rand.random(), rand.random(), rand.random()),
        constraint_orientation='GLOBAL',
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1
    )

    # create and add a texture and color
    mat=bpy.data.materials.new('Matty')
    mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    bpy.data.objects['Cube'].data.materials.append(mat)
    # mat = tex.createMaterials()
    # bpy.data.objects['Cube'].data.materials.append(mat)
    # if not len(objID):
    #     mat = bpy.data.materials['Material']
    #     mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     # mat = tex.createMaterials()
    #     bpy.data.objects['Cube'].data.materials.append(mat)
    #     # print(objID, 'hello')
    # else:
    #     mat = bpy.data.materials['Material.'+objID]
    #     mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     # mat = tex.createMaterials()
    #     bpy.data.objects['Cube.'+objID].data.materials.append(mat)
    # #     print(objID)


def create_random_sphere(
        objID='',
        R=[0.0, 1.0],
        range_theta=[0, 2 * pi],
        range_phi=[0, pi],
        size=[0.01, 0.03]
):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    theta = ((range_theta[1] - range_theta[0]) * rand.random() + range_theta[0]);
    phi = ((range_phi[1] - range_phi[0]) * rand.random() + range_phi[0]);
    R = R[0] + (R[1] - R[0]) * rand.random()
    # x = R*cos(theta)*sin(phi)
    # y = R*sin(theta)*sin(phi)
    # z = 3*30.48
    R = rand.uniform(size[0], size[1])
    x = rand.uniform(-14.6, 14.6)
    y = rand.uniform(-14.6, 14.6)
    z = 3 * 30.48+R
    # z = R*cos(phi)
    loc = (x, y, z)

    # create a cube object
    bpy.ops.mesh.primitive_uv_sphere_add(
        location=loc,
        size=R
    )
    bpy.ops.transform.rotate(
        value=rand.random() * 3.14,
        axis=(rand.random(), rand.random(), rand.random()),
        constraint_orientation='GLOBAL',
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1
    )

    # create and add a texture and color
    mat=bpy.data.materials.new('Matty')
    mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    bpy.data.objects['Sphere'].data.materials.append(mat)
    # if not len(objID):
    #     mat = bpy.data.materials['Material']
    #     mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     # mat = tex.createMaterials()
    #     bpy.data.objects['Sphere'].data.materials.append(mat)
    # else:
    #     mat = bpy.data.materials['Material.'+objID]
    #     mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     # mat = tex.createMaterials()
    #     bpy.data.objects['Sphere.' + objID].data.materials.append(mat)


def create_random_cylinder(
        objID='',
        R=[0.0, 1.0],
        range_theta=[0, 2 * pi],
        range_phi=[0, pi],
        size=[0.01, 0.03]
):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and
    """
    theta = ((range_theta[1] - range_theta[0]) * rand.random() + range_theta[0]);
    phi = ((range_phi[1] - range_phi[0]) * rand.random() + range_phi[0]);
    R = R[0] + (R[1] - R[0]) * rand.random()
    # x = R*cos(theta)*sin(phi)
    # y = R*sin(theta)*sin(phi)
    # z = 3*30.48
    R = rand.uniform(size[0], size[1])
    D = rand.uniform(size[0], size[1])
    x = rand.uniform(-14.6, 14.6)
    y = rand.uniform(-14.6, 14.6)
    z = 3 * 30.48+R
    # z = R*cos(phi)
    loc = (x, y, z)

    # create a cube object
    bpy.ops.mesh.primitive_cylinder_add(
        location=loc,
        radius=R,
        depth=D
    )
    bpy.ops.transform.rotate(
        value=rand.random() * 3.14,
        axis=(rand.random(), rand.random(), rand.random()),
        constraint_orientation='GLOBAL',
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1
    )

    # create and add a texture and color
    mat=bpy.data.materials.new('Matty')
    mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    bpy.data.objects['Cylinder'].data.materials.append(mat)
    # if not len(objID):
    #     mat = bpy.data.materials['Material']
    #     mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     # mat = tex.createMaterials()
    #     bpy.data.objects['Cylinder'].data.materials.append(mat)
    # else:
    #     mat = bpy.data.materials['Material.'+objID]
    #     mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     # mat = tex.createMaterials()
    #     bpy.data.objects['Cylinder.' + objID].data.materials.append(mat)


def create_random_cone(
        objID='',
        R=[0.0, 1.0],
        range_theta=[0, 2 * pi],
        range_phi=[0, pi],
        size=[0.01, 0.03]
):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and
    """
    theta = ((range_theta[1] - range_theta[0]) * rand.random() + range_theta[0]);
    phi = ((range_phi[1] - range_phi[0]) * rand.random() + range_phi[0]);
    R = R[0] + (R[1] - R[0]) * rand.random()
    # x = R*cos(theta)*sin(phi)
    # y = R*sin(theta)*sin(phi)
    # z = 3*30.48
    R = rand.uniform(size[0], size[1])
    x = rand.uniform(-14.6, 14.6)
    y = rand.uniform(-14.6, 14.6)
    z = 3 * 30.48
    # z = R*cos(phi)
    loc = (x, y, z)

    # create a cube object
    bpy.ops.mesh.primitive_cone_add(
        location=loc,
        radius1=R,
        radius2=0.001,
        depth=rand.uniform(size[0], size[1])
    )
    bpy.ops.transform.rotate(
        value=rand.random() * 3.14,
        axis=(rand.random(), rand.random(), rand.random()),
        constraint_orientation='GLOBAL',
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1
    )

    # create and add a texture and color
    mat=bpy.data.materials.new('Matty')
    mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    bpy.data.objects['Cone'].data.materials.append(mat)
    # if not len(objID):
    #     mat = bpy.data.materials['Material']
    #     mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     # mat = tex.createMaterials()
    #     bpy.data.objects['Cone'].data.materials.append(mat)
    # else:
    #     mat = bpy.data.materials['Material.'+objID]
    #     mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
    #     # mat = tex.createMaterials()
    #     bpy.data.objects['Cone.' + objID].data.materials.append(mat)

def create_flat_background():
    """
    create a background composed of 3 planes
    """
    N = 30.48 / 2
    bpy.ops.mesh.primitive_plane_add(
        radius=N,
        enter_editmode=False,
        location=(0, 0, 6 * N),
        rotation=(0, 0, 0),
        layers=(
            True, False, False, False, False,
            False, False, False, False, False,
            False, False, False, False, False,
            False, False, False, False, False
        )
    )
    N = 30.48 / 2
    bpy.ops.mesh.primitive_plane_add(
        radius=N * 4,
        enter_editmode=False,
        location=(0, 0, 6 * N - 0.02),
        rotation=(0, 0, 0),
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
        Rx=[.5*30.48, 30.48],
        Ry=[-0.25 * 30.48, 0.25 * 30.48],
        Rz=[3.75 * 30.48, 4.25 * 30.48],
        view_range=[60, 70]
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
    x = rand.uniform(Rx[0], Rx[1])
    y = rand.uniform(Ry[0], Ry[1])
    z = rand.uniform(Rz[0], Rz[1])
    # x= 30.48
    # y=0
    # z = 4*30.48
    zz = z - 3 * 30.48
    R = norm([x, y, zz], ord=2)
    # print(theta)
    cam_object.location = (x, y, z)

    # set up camera focal properties
    cam_object.data.stereo.convergence_distance = 10000
    cam_object.data.angle = ((view_range[1] - view_range[0]) * rand.random() + view_range[0]) * pi / 180
    cam_object.data.stereo.interocular_distance = 0.3

    # Aim camera at the origin
    zang = atan2(y, x)
    # xang = acos(z/R)
    xang = acos(zz / R)
    # print(xang,zang)
    # print(zang*180/pi,xang*180/pi)
    # print(x,y,xang)
    # if ( z<0):
    #     cam_object.rotation_euler = (xang, 0, pi-zang)
    # elif(x>0 and y>0 and z>0):
    cam_object.rotation_euler = (xang - 5 * pi / 180, 0, pi / 2 + zang)
    # else:
    #     cam_object.rotation_euler = (xang, 0, -zang)

    cam_object.select = False

    return cam_object


def create_lamp(
        R=10 * 30.48,
        range_theta=[0, 2*pi],
        range_phi=[0, pi/4]):
    scene = bpy.context.scene
    intensity = rand.uniform(0.3, 0.5)
    # Create new lamp datablock
    lamp_data = bpy.data.lamps.new(name="New Lamp", type='AREA')

    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)

    # Link lamp object to the scene so it'll appear in this scene
    scene.objects.link(lamp_object)


    # Place lamp to a specified location
    theta = ((range_theta[1] - range_theta[0]) * rand.uniform(0, 1) + range_theta[0]);
    phi = ((range_phi[1] - range_phi[0]) * rand.uniform(0, 1) + range_phi[0]);
    # theta = 1/4*pi
    # phi = pi/3
    x = R * sin(phi) * cos(theta)
    y = R * sin(phi) * sin(theta)
    z = R * cos(phi)
    # print(theta, theta * 180 / pi)
    # print(phi, phi * 180 / pi)
    lamp_object.data.use_specular = 0
    lamp_object.data.color = (1, 0.95, 0.3)
    lamp_object.location = (x, y, z)
    lamp_object.rotation_euler = (phi+rand.gauss(0, 0.17), 0, theta + pi / 2+rand.gauss(0, 0.17))
    lamp_object.data.energy = intensity
    lamp_object.data.distance = 300
    lamp_object.data.gamma = 0.9
    lamp_object.data.shadow_method = "RAY_SHADOW"
    lamp_object.data.shape = "SQUARE"
    lamp_object.data.size = 30.48 * 8
    # And finally select it make active
    lamp_object.select = True

    scene.objects.active = lamp_object
    ######

    # Create new lamp datablock
    lamp_data2 = bpy.data.lamps.new(name="New Lamp2", type='AREA')

    # Create new object with our lamp datablock
    lamp_object2 = bpy.data.objects.new(name="New Lamp2", object_data=lamp_data2)

    # Link lamp object to the scene so it'll appear in this scene
    scene.objects.link(lamp_object2)


    # theta = ((range_theta[1] - range_theta[0]) * rand.uniform(0, 1) + range_theta[0]);
    # phi = ((range_phi[1] - range_phi[0]) * rand.uniform(0, 1) + range_phi[0]);
    x = R * sin(pi/2) * cos(theta+pi)
    y = R * sin(pi/2) * sin(theta+pi)
    z = R * cos(pi/2)+7*30.48
    Rr = norm([x, y, z], ord=2)
    xang = acos(z/Rr)
    lamp_object2.data.use_specular = 0
    lamp_object2.data.color = (0.5, 0.95, 1)
    lamp_object2.location = (x, y, z)
    lamp_object2.rotation_euler = (xang+rand.gauss(0, 0.08), 0, theta-pi/2+rand.gauss(0, 0.08))
    lamp_object2.data.energy = -2.9167*intensity+1.625
    lamp_object2.data.distance = 300
    lamp_object2.data.gamma = 0.9
    lamp_object2.data.shadow_method = "NOSHADOW"
    lamp_object2.data.shape = "SQUARE"
    lamp_object2.data.size = 30.48 * 5


    scene.objects.active = lamp_object2
    return scene


def render_scene(id="", ofilename='image' + str(id) + ".png"):
    bpy.context.scene.render.resolution_x = 227
    bpy.context.scene.render.resolution_y = 227
    bpy.context.scene.render.resolution_percentage = 100

    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.camera = bpy.data.objects['Camera' + str(id)]
    bpy.data.scenes['Scene'].render.filepath = ofilename
    bpy.ops.render.render(write_still=True)


def randomize_texture():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            # mat = tex.createMaterials()
            mat = bpy.data.materials.new(name='Material')
            mat.diffuse_color = (rand.random(), rand.random(), rand.random())
            # tex = bpy.data.textures.new("SomeName", 'IMAGE')
            # slot = mat.texture_slots.add()
            # slot.texture = tex
            # obj.data.materials.append(mat)
            bpy.ops.object.material_slot_remove()
            obj.data.materials.append(mat)


def import_rowdy(filename="RowdyWalker#6",
                 R=[0, 10],
                 range_theta=[0, 2 * pi],
                 range_phi=[0, pi],
                 size=[0.1]):  # actual size 0.075 scale
    # import rowdy in to the blender scene
    # print(filename)
    bpy.ops.import_mesh.stl(filepath=filename)
    filename = os.path.splitext(filename)[0]
    # # print(filename)
    # # capitalize the filename for some fkin reason
    obj = bpy.data.objects[filename]  # .capitalize()]
    ################
    # print(filename)
    # o = bpy.context.object=bpy.data.objects[filename]  # active object
    # print(o)
    mw = obj.matrix_world  # Active object's world matrix
    glob_vertex_coordinates = [mw * v.co for v in obj.data.vertices]  # Global coordinates of vertices

    bpy.ops.object.mode_set(mode='EDIT')  # Change mode of selected object to Edit mode
    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False,type='VERT')  # Set the type in Edit mode to Vertices
    bpy.ops.mesh.select_all(action='DESELECT')  # Deselect all
    bpy.ops.object.mode_set(mode='OBJECT')  # Change mode of selected object to Object mode

    # Find the lowest Z value amongst the object's verts
    minZ = min([co.z for co in glob_vertex_coordinates])

    # Select all the vertices that are on the lowest Z
    for v in obj.data.vertices:
        if (mw * v.co).z == minZ:
            v.select = True

    bpy.ops.object.mode_set(mode='EDIT')  # Change mode of selected object to Edit mode
    # print(bpy.context.area)
    current_area_type = bpy.context.area.type  # Save the current area type to a variable
    area = bpy.context.area  # Change the area to 3D view in order to get rid of wrong context error
    old_type = area.type  # Change the area to 3D view in order to get rid of wrong context error
    area.type = 'VIEW_3D'  # Change the area to 3D view in order to get rid of wrong context error
    bpy.ops.view3d.snap_cursor_to_selected()  # Move the cursor to selected
    bpy.ops.object.mode_set(mode='OBJECT')  # Set the mode back to Object mode
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')  # Move the selected object origing's to the 3D cursor's location
    bpy.context.area.type = current_area_type  # Set the area type back to what it was before changing it to 3D view
    ###################

    # print(obj.dimensions)
    # bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    # scale the rowdy to an appropriate size

    obj.scale = [0.1, 0.1, 0.1]
    # randomize the orientations of rowdy
    obj.rotation_euler = (pi, 0, pi * rand.random())
    # place the rowdy within the given bounds
    # theta = ((range_theta[1]-range_theta[0])+range_theta[0])*rand.random();
    # phi = ((range_phi[1]-range_phi[0])+range_phi[0])*rand.random();
    # R = R[0]+(R[1]-R[0])*rand.random()
    x = rand.randint(-5, 5)*2.54
    y = rand.randint(-5, 5)*2.54
    z = (36 + 0.498) * 30.48 / 12
    # z = R*cos(phi)
    obj.location = (x, y, z)
