# import bpy
#
# from bpy_extras.view3d_utils import location_3d_to_region_2d
#
#
# def view3d_find():
#     # returns first 3d view, normally we get from context
#     for area in bpy.context.window.screen.areas:
#         if area.type == 'VIEW_3D':
#             area.spaces[0].region_3d.view_perspective = 'CAMERA'
#             v3d = area.spaces[0]
#             rv3d = v3d.region_3d
#             for region in area.regions:
#                 if region.type == 'WINDOW':
#                     return region, rv3d
#     return None, None
#
#
# def view3d_camera_border(scene):
#     obj = scene.camera
#     cam = obj.data
#     frame = cam.view_frame(scene)
#     # move into object space
#     frame = [obj.matrix_world * v for v in frame]
#     # move into pixelspace
#     frame_px = [location_3d_to_region_2d(region, rv3d, v) for v in frame]
#     return frame_px
#
# region, rv3d = view3d_find()
#  # put the region into camera perspective
# rv3d.view_perspective = 'CAMERA'
# frame_px = view3d_camera_border(bpy.context.scene)
# print("Camera frame:", frame_px)
#
#
# # this is the camera bounds
# blc = min(frame_px)
# cambounds = [v - blc for v in frame_px]
# print("camera is on screen as :", max(cambounds))
# ratio = [224/max(cambounds[0]), 227/max(cambounds[1])]
#     #######################################################
# # object location
# obj = bpy.data.objects["QuarterInAW"] # the context object.
# obj.select = True
# print(bpy.data.objects["QuarterInAW"])
# #print("obj", obj)
# #print("Location 3d to 2d:", location_3d_to_region_2d(region,rv3d,obj.matrix_world.to_translation()))
# #print("BLC:", blc)
# objloc = location_3d_to_region_2d(region,rv3d,obj.matrix_world.to_translation()) - blc
# #print("objloc:",objloc)
#
# bounding_box = [v[:] for v in obj.bound_box]
# #print("bbox",bounding_box)
# bbox_px = [location_3d_to_region_2d(region, rv3d, v) - blc for v in bounding_box]
# #print("bbox_pix",bbox_px,type(bbox_px))
# min_x = min(v.x for v in bbox_px)*ratio[0]
# max_x = max(v.x for v in bbox_px)*ratio[0]
# min_y = min(v.y for v in bbox_px)*ratio[1]
# max_y = max(v.y for v in bbox_px)*ratio[1]
# bbox_width = (max_x - min_x)
# bbox_height = (max_y - min_y)
# #print("bbox_width",bbox_width)
# #print("bbox_width",bbox_width)
# #print("min_x",min_x)
# #print("max_y",max_y)
#
# #... etc to get the coords of bbox.
# #print("obj verts",obj.data.vertices[0])
# mw = obj.matrix_world
# #global vert locs
# verts = [mw * v.co for v in obj.data.vertices]
# # vert locations in "region camera coords"
# verts_px = [location_3d_to_region_2d(region, rv3d, v) - blc for v in verts]
# #print(verts_px)
#
# print(bbox_height)
# print(bbox_width)
# #print(verts_px)
# #print((verts_px[1][0])
# max_vertx = max(v.x for v in verts_px)
# max_verty = max(v.y for v in verts_px)
# min_vertx = min(v.x for v in verts_px)
# min_verty = min(v.y for v in verts_px)
# max_vertx = max_vertx*ratio[0]
# max_verty = max_verty*ratio[1]
# min_vertx = min_vertx*ratio[0]
# min_verty = min_verty*ratio[1]
# print(max_vertx,min_vertx,max_verty,min_verty,max_vertx-min_vertx,max_verty-min_verty)
# print(blc)
#################################################

import bpy

from bpy_extras.view3d_utils import location_3d_to_region_2d


def pixelfind(id=""):
    bpy.context.scene.camera = bpy.data.objects['Camera' + str(id)]
    # for area in bpy.context.screen.areas:
    #     if area.type == 'VIEW_3D':
    #         area.spaces[0].region_3d.view_perspective = 'CAMERA'
    #         break
    region, rv3d = view3d_find()
    # put the region into camera perspective
    rv3d.view_perspective = 'CAMERA'


    frame_px = view3d_camera_border(bpy.context.scene,region,rv3d)
    print("Camera frame:", frame_px)

    # this is the camera bounds
    blc = min(frame_px)
    cambounds = [v - blc for v in frame_px]
    print("camera is on screen as :", max(cambounds))
    ratio = [227 / max(cambounds[0]), 227 / max(cambounds[1])]
    #######################################################
    # object location
    obj = bpy.data.objects["QuarterInAW"]  # the context object.
    obj.select = True
    print(bpy.data.objects["QuarterInAW"])
    # print("obj", obj)
    # print("Location 3d to 2d:", location_3d_to_region_2d(region,rv3d,obj.matrix_world.to_translation()))
    # print("BLC:", blc)
    objloc = location_3d_to_region_2d(region, rv3d, obj.matrix_world.to_translation()) - blc
    # print("objloc:",objloc)

    bounding_box = [v[:] for v in obj.bound_box]
    # print("bbox",bounding_box)
    bbox_px = [location_3d_to_region_2d(region, rv3d, v) - blc for v in bounding_box]
    # print("bbox_pix",bbox_px,type(bbox_px))
    min_x = min(v.x for v in bbox_px) * ratio[0]
    max_x = max(v.x for v in bbox_px) * ratio[0]
    min_y = min(v.y for v in bbox_px) * ratio[1]
    max_y = max(v.y for v in bbox_px) * ratio[1]
    bbox_width = (max_x - min_x)
    bbox_height = (max_y - min_y)
    print("bbox_width",bbox_width)
    print("bbox_height",bbox_height)
    print("min_x",min_x)
    print("max_y",max_y)

    # ... etc to get the coords of bbox.
    # print("obj verts",obj.data.vertices[0])
    mw = obj.matrix_world
    # global vert locs
    verts = [mw * v.co for v in obj.data.vertices]
    # vert locations in "region camera coords"
    verts_px = [location_3d_to_region_2d(region, rv3d, v) - blc for v in verts]
    # print(verts_px)

    print(bbox_height)
    print(bbox_width)
    # print(verts_px)
    # print((verts_px[1][0])
    max_vertx = max(v.x for v in verts_px)
    max_verty = max(v.y for v in verts_px)
    min_vertx = min(v.x for v in verts_px)
    min_verty = min(v.y for v in verts_px)
    max_vertx = max_vertx * ratio[0]
    max_verty = max_verty * ratio[1]
    min_vertx = min_vertx * ratio[0]
    min_verty = min_verty * ratio[1]
    print(max_vertx, min_vertx, max_verty, min_verty, max_vertx - min_vertx, max_verty - min_verty)
    print(blc)


def view3d_find():
    # returns first 3d view, normally we get from context
    for area in bpy.context.window.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'
            v3d = area.spaces[0]
            rv3d = v3d.region_3d
            for region in area.regions:
                if region.type == 'WINDOW':
                    return region, rv3d
    return None, None


def view3d_camera_border(scene,region,rv3d):
    obj = scene.camera
    cam = obj.data
    frame = cam.view_frame(scene)
    # move into object space
    frame = [obj.matrix_world * v for v in frame]
    # move into pixelspace
    frame_px = [location_3d_to_region_2d(region, rv3d, v) for v in frame]
    return frame_px
