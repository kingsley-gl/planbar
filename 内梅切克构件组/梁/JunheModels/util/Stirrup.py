# -*- coding: utf-8 -*-
# @Time    : 2017/08/11
# @Author  : kingsley kuang
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : Stirrup.py 箍筋文件
# @Software: 
# @Function: 

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Utility as AllplanUtility          # allplan util library


import StdReinfShapeBuilder.GeneralReinfShapeBuilder as GeneralShapeBuilder
import StdReinfShapeBuilder.LinearBarPlacementBuilder as LinearBarBuilder


from StdReinfShapeBuilder.ConcreteCoverProperties import ConcreteCoverProperties as ConProperties
from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties as ReinforceProperties
from StdReinfShapeBuilder.RotationAngles import RotationAngles
import math

print("Loading Stirrup.py")

class Stirrup(object):
    def __init__(self,cover,rebar_prop):
        '''
        cover = [left,right,top,bottom]
        rebar_prop = [diameter,bending_roller,steel_grade,concrete_grade,bending_shape_type,mesh_type,mesh_bending_direction]
        '''
        if isinstance(cover, dict):
            self._cover = ConProperties(**cover)
        elif isinstance(cover, list):
            self._cover = ConProperties(*cover)
        else:
            self._cover = cover


        if isinstance(rebar_prop, dict):
            self._shape_props =  ReinforceProperties.rebar(**rebar_prop)
        elif isinstance(rebar_prop, list):
            self._shape_props =  ReinforceProperties.rebar(*rebar_prop)
        else:
            self._shape_props = rebar_prop


    def shape_open_stirrup(self,height,width,extend=500,hook=100,open_side=1,degrees=90,vertical=False):
        point_list = []

        radian = math.radians(180-degrees)
        if open_side == 1:
            point_list.append((AllplanGeo.Point3D(height+extend-math.cos(radian)*hook-self._cover.top,width-hook-self._cover.left,0),0))
            point_list.append((AllplanGeo.Point3D(height+extend-self._cover.top,width-self._cover.left,0),0)) 
            point_list.append((AllplanGeo.Point3D(self._cover.bottom,width-self._cover.left,0),0))
            point_list.append((AllplanGeo.Point3D(self._cover.bottom,self._cover.right,0),0))  
            point_list.append((AllplanGeo.Point3D(height+extend-self._cover.top,self._cover.right,0),0))
            point_list.append((AllplanGeo.Point3D(height+extend-math.cos(radian)*hook-self._cover.top,self._cover.right+hook,0),0))
        if open_side == 2:
            point_list.append((AllplanGeo.Point3D(self._cover.bottom+hook,width+extend-self._cover.left-math.cos(radian)*hook,0),0)) 
            point_list.append((AllplanGeo.Point3D(self._cover.bottom,width+extend-self._cover.left,0),0))
            point_list.append((AllplanGeo.Point3D(self._cover.bottom,self._cover.right,0),0))  
            point_list.append((AllplanGeo.Point3D(height-self._cover.top,self._cover.right,0),0))
            point_list.append((AllplanGeo.Point3D(height-self._cover.top,width+extend-self._cover.left,0),0))
            point_list.append((AllplanGeo.Point3D(height-hook-self._cover.top,width+extend-self._cover.left-math.cos(radian)*hook,0),0))
        if open_side == 3: 
            point_list.append((AllplanGeo.Point3D(self._cover.bottom-extend+math.cos(radian)*hook,hook+self._cover.right,0),0))
            point_list.append((AllplanGeo.Point3D(self._cover.bottom-extend,self._cover.right,0),0))  
            point_list.append((AllplanGeo.Point3D(height-self._cover.top,self._cover.right,0),0))
            point_list.append((AllplanGeo.Point3D(height-self._cover.top,width-self._cover.left,0),0))
            point_list.append((AllplanGeo.Point3D(self._cover.bottom-extend,width-self._cover.left,0),0))
            point_list.append((AllplanGeo.Point3D(self._cover.bottom-extend+math.cos(radian)*hook,width-hook-self._cover.left,0),0))
        if open_side == 4:
            point_list.append((AllplanGeo.Point3D(height-self._cover.top-hook,self._cover.right-extend+math.cos(radian)*hook,0),0))
            point_list.append((AllplanGeo.Point3D(height-self._cover.top,self._cover.right-extend,0),0))
            point_list.append((AllplanGeo.Point3D(height-self._cover.top,width-self._cover.left,0),0))
            point_list.append((AllplanGeo.Point3D(self._cover.bottom,width-self._cover.left,0),0))
            point_list.append((AllplanGeo.Point3D(self._cover.bottom,self._cover.right-extend,0),0))
            point_list.append((AllplanGeo.Point3D(self._cover.bottom+hook,self._cover.right-extend+math.cos(radian)*hook,0),0))



        shape_build = AllplanReinf.ReinforcementShapeBuilder()
        shape_build.AddPoints(point_list)

        shape = shape_build.CreateShape(self._shape_props)
        if vertical:
            angle = RotationAngles(0,-90,0)
            shape.Rotate(angle)
        if shape.IsValid():
            return shape       

    def shape_stirrup(self,length,width,extend=0,extend_side=1,vertical=False):
        point_list = []

        self._shape_props.prop_bending_shape_type = AllplanReinf.BendingShapeType.OpenStirrup
        stirrup = AllplanReinf.StirrupType.Normal
        if not vertical:
            left = self._cover.left
            right = self._cover.right
            top = self._cover.top
            bottom = self._cover.bottom
        else:
            left = self._cover.bottom
            right = self._cover.top
            top = self._cover.right
            bottom = self._cover.left


        if extend_side == 1:
            point_list.append((AllplanGeo.Point3D(left,width-top,0),0))
            point_list.append((AllplanGeo.Point3D(left,bottom,0),0))
            point_list.append((AllplanGeo.Point3D(length+extend-right,bottom,0),0))
            point_list.append((AllplanGeo.Point3D(length+extend-right,width-top,0),0))
            point_list.append((AllplanGeo.Point3D(left,width-top,0),0))

        elif extend_side == 2:
            point_list.append((AllplanGeo.Point3D(left,width+extend-top,0),0))
            point_list.append((AllplanGeo.Point3D(left,bottom,0),0))
            point_list.append((AllplanGeo.Point3D(length-right,bottom,0),0))
            point_list.append((AllplanGeo.Point3D(length-right,width+extend-top,0),0))
            point_list.append((AllplanGeo.Point3D(left,width+extend-top,0),0))
        elif extend_side == 3:
            point_list.append((AllplanGeo.Point3D(left-extend,width-top,0),0))
            point_list.append((AllplanGeo.Point3D(left-extend,bottom,0),0))
            point_list.append((AllplanGeo.Point3D(length-right,bottom,0),0))
            point_list.append((AllplanGeo.Point3D(length-right,width-top,0),0))
            point_list.append((AllplanGeo.Point3D(left-extend,width-top,0),0))
        elif extend_side == 4:
            point_list.append((AllplanGeo.Point3D(left,width-top,0),0))
            point_list.append((AllplanGeo.Point3D(left,bottom-extend,0),0))
            point_list.append((AllplanGeo.Point3D(length-right,bottom-extend,0),0))
            point_list.append((AllplanGeo.Point3D(length-right,width-top,0),0))
            point_list.append((AllplanGeo.Point3D(left,width-top,0),0))

        shape_build = AllplanReinf.ReinforcementShapeBuilder()
        shape_build.AddPoints(point_list)
        shape = shape_build.CreateStirrup(self._shape_props,stirrup)


        if vertical:
            angle = RotationAngles(0,-90,0)
            shape.Rotate(angle)
        if shape.IsValid():
            return shape


    def shape_tie_steel(self,length,width,rotate,hook=100,degrees=90):

        self._shape_props.prop_bending_shape_type = AllplanReinf.BendingShapeType.OpenStirrup
        self._shape_props.prop_bending_roller = math.pi*self._shape_props.prop_diameter/100


        #
        args = {'length':length,
                'width':width,
                'shape_props':self._shape_props,
                'concrete_cover_props':self._cover,
                'model_angles':rotate,
                'start_hook':hook,
                'end_hook':hook,
                'start_hook_angle':degrees,
                'end_hook_angle':degrees}

        shape = GeneralShapeBuilder.create_open_stirrup(**args)
        if shape.IsValid():
            return shape