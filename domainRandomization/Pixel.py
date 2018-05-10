import bpy
from bpy_extras.view3d_utils import location_3d_to_region_2d


def view3d_find():
    # returns first 3d view, normally we get from context
    for area in bpy.context.window.screen.areas:
        if area.type == 'VIEW_3D':
            v3d = area.spaces[0]
            rv3d = v3d.region_3d
            for region in area.regions:
                if region.type == 'WINDOW':
                    return region, rv3d
    return None, None


def view3d_camera_border(scene, region, rv3d):
    obj = scene.camera
    cam = obj.data
    frame = cam.view_frame(scene)
    # move into object space
    frame = [obj.matrix_world * v for v in frame]
    # move into pixelspace
    frame_px = [location_3d_to_region_2d(region, rv3d, v) for v in frame]
    return frame_px

def initialPix():
    bpy.context.scene.camera = bpy.data.objects['Camera']


    area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
    area.spaces[0].region_3d.view_perspective = 'CAMERA'
    region, rv3d = view3d_find()
    # put the region into camera perspective
    rv3d.view_perspective = 'CAMERA'

    frame_px = view3d_camera_border(bpy.context.scene, region, rv3d)
    print("Camera frame:", frame_px)

    blc = min(frame_px)
    cambounds = [v - blc for v in frame_px]
    print("camera is on screen as :", max(cambounds))

def pixelfind(id=""):
    print("\n\n")
    bpy.context.scene.camera = bpy.data.objects['Camera']


    area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
    area.spaces[0].region_3d.view_perspective = 'CAMERA'
    region, rv3d = view3d_find()
    # put the region into camera perspective
    rv3d.view_perspective = 'CAMERA'

    frame_px = view3d_camera_border(bpy.context.scene, region, rv3d)
    print("Camera frame:", frame_px)

    blc = min(frame_px)
    cambounds = [v - blc for v in frame_px]
    print("camera is on screen as :", max(cambounds))
    ratio = 227 / max(cambounds[0])
    print("ratio is ", ratio)
    bpy.ops.object.select_all(action='DESELECT')
    if id == "":
        obj = bpy.data.objects["Plane"]
    else:
        obj = bpy.data.objects[id]  # the context object.
    obj.select = True
    objloc = location_3d_to_region_2d(
        region,
        rv3d,
        obj.matrix_world.to_translation()) - blc
    print("Objects Location", objloc, "FIXED", [v * ratio for v in objloc])

    bounding_box = [v[:] for v in obj.bound_box]
    bbox_px = [location_3d_to_region_2d(region, rv3d, v)
               - blc for v in bounding_box]

    min_x = min(v.x for v in bbox_px)
    max_x = max(v.x for v in bbox_px)
    min_y = min(v.y for v in bbox_px)
    max_y = max(v.y for v in bbox_px)
    bbox_width = max_x - min_x
    bbox_height = max_y - min_y

    print("bbox_width", bbox_width*ratio)
    print("bbox_height", bbox_height*ratio)
    print(min_x*ratio, max_x*ratio,min_y*ratio,max_y*ratio,bbox_width*ratio,bbox_height*ratio)

    mw = obj.matrix_world
    # global vert locs
    verts = [mw * v.co for v in obj.data.vertices]
    # vert locations in "region camera coords"
    verts_px = [location_3d_to_region_2d(region, rv3d, v)
                - blc for v in verts]
    min_xs = min(v.x for v in verts_px)
    max_xs = max(v.x for v in verts_px)
    min_ys = min(v.y for v in verts_px)
    max_ys = max(v.y for v in verts_px)
    pixel_width = max_xs - min_xs
    pixel_height = max_ys - min_ys
    print(min_xs*ratio, max_xs*ratio,min_ys*ratio,max_ys*ratio,pixel_width*ratio,pixel_height*ratio)
    bpy.ops.object.select_all(action='DESELECT')
pixelfind(id="QuarterInAW")