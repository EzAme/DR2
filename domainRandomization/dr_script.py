# import the enviroment randomization function file
import sys
import os
import bpy
sys.path.append("/home/ez/DR2/domainRandomization")
import pby_fun as fun
import Pixel as pix
import texture_test as tex
from random import randint
from math import pi
import csv
import datetime as dt
# Delete excess materials
# for material in bpy.data.materials:
#     if not material.users:
#         bpy.data.materials.remove(material)
def add_random_shape(R=[2,6], size=[.5, 1], range_theta=[0,pi/2], range_phi=[0,pi/2]):
    i = randint(1,4)
    if i is 1:
        fun.create_random_cube(R=R,size=size);
    elif i is 2:
        fun.create_random_sphere(R=R,size=size);
    elif i is 3:
        fun.create_random_cylinder(R=R,size=size);
    elif i is 4:
        fun.create_random_cone(R=R, size=size);


def makeascene(val=0):
    # remove all object from current scene
    fun.clean_up_scene_init()
    fun.import_rowdy(filename="QuarterInAW.stl",
                     R=[4, 6],
                     range_theta=[-0.7853981634, 2.3561944902],
                     range_phi=[0, 1.25],
                     size=0.1)
    fun.create_flat_background()
    # for area in bpy.context.screen.areas:
    #     if area.type == 'VIEW_3D':
    #         area.spaces[0].region_3d.view_perspective = 'CAMERA'
    #         break
# def importSTL():
#     fun.import_rowdy(filename="QuarterInAW.stl",
#                      R=[4, 6],
#                      range_theta=[-0.7853981634, 2.3561944902],
#                      range_phi=[0, 1.25],
#                      size=0.1)

def make_csv(val=0):
    if val == 1:
        with open('drimages/Position/' + ctime + '.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(pos)
if __name__ == "__main__":

    # the number of scenes
    ctime=str(dt.datetime.now())
    N = 2
    ncams = 1
    N = int(N/ncams)
    makeascene()

    for i in range(N):
        # create a scene
        p = 1
        j = randint(0, 7)
        fun.clean_up_scene()
        pos=fun.move_obj(filename="QuarterInAW.stl")



        for k in range(j-1):
            add_random_shape()
        fun.randomize_texture()
        # now that the scene has been created we need to now render the scene
        for k in range(p):
            fun.create_lamp(R=10*30.48,
                    range_theta=[0,2*3.14159265],
                    range_phi=[0,3.14159265/4])


        for k in range(ncams):
            fun.create_camera()
            area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
            area.spaces[0].region_3d.view_perspective = 'CAMERA'


            make_csv(val=0)
            if k == 0:
                fun.render_scene(id="", ofilename="drimages/pos/" + ctime + "/set" + str(i) + "_image" + str(k) + ".png")

            else:
                fun.render_scene(id="", ofilename="drimages/pos/" + ctime + "/set" + str(i) + "_image" + str(k) + ".png")

            # fun.clear_camera()
            #print(x, y, width, height)
            # print(fun.view3d_find())
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        #input("\nINPUT\n")

        pix.pixelfind("QuarterInAW")