import sys
import os
import bpy
import Pixel as pix



def initialPix():
    bpy.context.scene.camera = bpy.data.objects['Camera']


    area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
    area.spaces[0].region_3d.view_perspective = 'CAMERA'
    region, rv3d = pix.view3d_find()
    # put the region into camera perspective
    rv3d.view_perspective = 'CAMERA'

    frame_px = pix.view3d_camera_border(bpy.context.scene, region, rv3d)
    print("Camera frame:", frame_px)