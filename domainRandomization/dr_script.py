# import the enviroment randomization function file
import sys
import os
sys.path.append("/home/ez/DR2/domainRandomization")
import pby_fun as fun
import texture_test as tex
from random import randint
from math import pi

# Delete excess materials
# for material in bpy.data.materials:
#     if not material.users:
#         bpy.data.materials.remove(material)
def add_random_shape(R=[2,6], size=[.5, 1], range_theta=[0,pi/2], range_phi=[0,pi/2]):
    i = randint(1,2)
    if i is 1:
        fun.create_random_cube(R=R,size=size);
    elif i is 2:
        fun.create_random_sphere(R=R,size=size);


def makeascene(val=0):
    # remove all object from current scene
    fun.clean_up_scene()
    fun.create_flat_background()


if __name__ == "__main__":
    # the number of scenes
    N = 10
    ncams = 2
    N = int(N/ncams)

    for i in range(N):
        # create a scene
        makeascene()
        
        j = randint(0,5)
        p = 1
        # add objects randomly
        if i<N/2:
            # add j random shapes
            for k in range(j):
                add_random_shape()
        else:
            # add rowdy and add j random shapes with textures
            # fun.import_rowdy(filename="rowdy.STL",
            # fun.import_rowdy(filename="fastener1.stl",
            fun.import_rowdy(filename="QuarterInAW.stl",
                    R=[4,6],
                    range_theta=[-0.7853981634,2.3561944902],
                    range_phi=[0,1.25],
                    size=0.1)
            for k in range(j-1):
                add_random_shape()
        fun.randomize_texture()
        # now that the scene has been created we need to now render the scene
        for k in range(p):
            fun.create_lamp(R=15,
                    range_theta=[0,3.14159265],
                    range_phi=[0,1.5707963268])
            
        for k in range(ncams):
            fun.create_camera()
            # if k == 0:
            #     if i<N/2:
            #         fun.render_scene(id="",ofilename="drimages/not_rowdy/set"+str(i)+"_image"+str(k)+".png")
            #     else:
            #         fun.render_scene(id="",ofilename="drimages/rowdy/set"+str(i)+"_image"+str(k)+".png")
            # else:
            #     if i<N/2:
            #         fun.render_scene(id=".00"+str(k),ofilename="drimages/not_rowdy/set"+str(i)+"_image"+str(k)+".png")
            #     else:
            #         fun.render_scene(id=".00"+str(k),ofilename="drimages/rowdy/set"+str(i)+"_image"+str(k)+".png")
