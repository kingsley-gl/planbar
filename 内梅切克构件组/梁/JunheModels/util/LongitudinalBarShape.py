# -*- coding: utf-8 -*-
# @Time    : 2017/08/11
# @Author  : kingsley kuang
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : LongitudinalBarShape.py 樑源码文件
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

print("Loading LongitudinalBarShape.py")



class LongitudinalSteel(object):
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


    def shape_steel(self,length,vertical=False):
        self._shape_props.prop_bending_shape_type = AllplanReinf.BendingShapeType.LongitudinalBar
        point_list = []
        if vertical:
            point_list.append((AllplanGeo.Point3D(self._cover.bottom,0,0),0))
            point_list.append((AllplanGeo.Point3D(length - self._cover.top,0,0),0))  
        else:
            point_list.append((AllplanGeo.Point3D(self._cover.left,0,0),0))
            point_list.append((AllplanGeo.Point3D(length - self._cover.right,0,0),0))  

        shape_build = AllplanReinf.ReinforcementShapeBuilder()
        shape_build.AddPoints(point_list)

        shape = shape_build.CreateShape(self._shape_props)
        if vertical:
            angle = RotationAngles(0,-90,0)
            shape.Rotate(angle)
        if shape.IsValid():
            return shape

    def shape_extend_steel(self,length,extend=0,left=0,right=0,extend_side=0,vertical=False):
        '''
        extend_side:
            vertical
            0 - both 
            1 - bottom extend
            2 - top extend
            horizontal
            0 - both
            1 - left extend
            2 - right extend
        '''
        self._shape_props.prop_bending_shape_type = AllplanReinf.BendingShapeType.LongitudinalBar
        point_list = []
        if vertical:
            if extend_side == 1:
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length - self._cover.top,0,0),0))  
            elif extend_side == 2:
                point_list.append((AllplanGeo.Point3D(self._cover.bottom,0,0),0))
                point_list.append((AllplanGeo.Point3D(length + extend,0,0),0))  
            elif extend_side == 3:
                point_list.append((AllplanGeo.Point3D(-left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length + right,0,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length + extend,0,0),0))

        else:
            if extend_side == 1:
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length - self._cover.right,0,0),0))  
            elif extend_side == 2:
                point_list.append((AllplanGeo.Point3D(self._cover.left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length + extend,0,0),0)) 
            elif extend_side == 3:
                point_list.append((AllplanGeo.Point3D(-left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length + right,0,0),0)) 
            else:
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length + extend,0,0),0))  

        shape_build = AllplanReinf.ReinforcementShapeBuilder()
        shape_build.AddPoints(point_list)

        shape = shape_build.CreateShape(self._shape_props)
        if vertical:
            angle = RotationAngles(0,-90,0)
            shape.Rotate(angle)
        if shape.IsValid():
            return shape

    def shape_anchor_steel(self,length,anchor,bend_position,bend_length,bend_width,anchor_side,mirror=False,vertical=False):
        '''
        anchor_side:
            vertical
            0 - both 
            1 - bottom extend
            2 - top extend
            horizontal
            0 - both
            1 - left extend
            2 - right extend
        '''
        self._shape_props.prop_bending_shape_type = AllplanReinf.BendingShapeType.LongitudinalBar
        point_list = []

        if vertical:
            head_cover = self._cover.bottom
            end_cover = self._cover.top
        else:
            head_cover = self._cover.left
            end_cover = self._cover.right

        if anchor_side == 1:
            if not mirror:
                point_list.append((AllplanGeo.Point3D(-anchor,bend_width,0),0))
                point_list.append((AllplanGeo.Point3D(-bend_length-bend_position,bend_width,0),0))
                point_list.append((AllplanGeo.Point3D(-bend_position,0,0),0))
                point_list.append((AllplanGeo.Point3D(length-end_cover,0,0),0))  
            else:
                point_list.append((AllplanGeo.Point3D(-anchor,-bend_width,0),0))
                point_list.append((AllplanGeo.Point3D(-bend_length-bend_position,-bend_width,0),0))
                point_list.append((AllplanGeo.Point3D(-bend_position,0,0),0))
                point_list.append((AllplanGeo.Point3D(length-end_cover,0,0),0))

        elif anchor_side == 2:
            if not mirror:
                point_list.append((AllplanGeo.Point3D(head_cover,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+bend_position,0,0),0))  
                point_list.append((AllplanGeo.Point3D(length+bend_position+bend_length,bend_width,0),0))  
                point_list.append((AllplanGeo.Point3D(length+anchor,bend_width,0),0))  
            else:
                point_list.append((AllplanGeo.Point3D(head_cover,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+bend_position,0,0),0))  
                point_list.append((AllplanGeo.Point3D(length+bend_position+bend_length,-bend_width,0),0))  
                point_list.append((AllplanGeo.Point3D(length+anchor,-bend_width,0),0)) 
        else:
            if not mirror:
                point_list.append((AllplanGeo.Point3D(-anchor,bend_width,0),0))
                point_list.append((AllplanGeo.Point3D(-bend_length-bend_position,bend_width,0),0))
                point_list.append((AllplanGeo.Point3D(-bend_position,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+bend_position,0,0),0))  
                point_list.append((AllplanGeo.Point3D(length+bend_position+bend_length,bend_width,0),0))  
                point_list.append((AllplanGeo.Point3D(length+anchor,bend_width,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(-anchor,-bend_width,0),0))
                point_list.append((AllplanGeo.Point3D(-bend_length-bend_position,-bend_width,0),0))
                point_list.append((AllplanGeo.Point3D(-bend_position,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+bend_position,0,0),0))  
                point_list.append((AllplanGeo.Point3D(length+bend_position+bend_length,-bend_width,0),0))  
                point_list.append((AllplanGeo.Point3D(length+anchor,-bend_width,0),0))


        shape_build = AllplanReinf.ReinforcementShapeBuilder()
        shape_build.AddPoints(point_list)

        shape = shape_build.CreateShape(self._shape_props)
        if vertical:
            angle = RotationAngles(0,-90,0)
            shape.Rotate(angle)
        if shape.IsValid():
            return shape
        

    def shape_hook_steel(self,length,hook,extend=0,degrees=90,hook_side=0,left=0,right=0,rotate=0,mirror=False,vertical=False):
        '''
        hook_side:
            vertical
            0 - both 
            1 - bottom extend
            2 - top extend
            3 - bottom,top input extend
            horizontal
            0 - extend para both
            1 - left extend
            2 - right extend

            3 - left,right input extend
            4 - left hook right input
            5 - left input right hook
        '''
        self._shape_props.prop_bending_shape_type = AllplanReinf.BendingShapeType.Stirrup 

        self._shape_props.prop_bending_roller = math.pi*self._shape_props.prop_diameter/10     
        point_list = []  

        if vertical:
            head_cover = self._cover.bottom
            end_cover = self._cover.top
        else:
            head_cover = self._cover.left
            end_cover = self._cover.right


        radian = math.radians(180-degrees)
        print('radian',self._shape_props.prop_bending_roller)
        if hook_side == 1:
            if mirror:
                point_list.append((AllplanGeo.Point3D(-extend-math.cos(radian)*hook,-hook,0),0))
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length-end_cover,0,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(-extend-math.cos(radian)*hook,hook,0),0))
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length-end_cover,0,0),0))
        elif hook_side == 2:
            if mirror:
                point_list.append((AllplanGeo.Point3D(head_cover,0,0),0))
                point_list.append((AllplanGeo.Point3D(length,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend+math.cos(radian)*hook,-hook,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(head_cover,0,0),0))
                point_list.append((AllplanGeo.Point3D(length,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend+math.cos(radian)*hook,hook,0),0))
        elif hook_side == 3:
            if mirror:
                point_list.append((AllplanGeo.Point3D(-left-math.cos(radian)*hook,-hook,0),0))
                point_list.append((AllplanGeo.Point3D(-left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right+math.cos(radian)*hook,-hook,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(-left-math.cos(radian)*hook,hook,0),0))
                point_list.append((AllplanGeo.Point3D(-left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right+math.cos(radian)*hook,hook,0),0))
        elif hook_side == 4:
            if mirror:
                point_list.append((AllplanGeo.Point3D(-left-math.cos(radian)*hook,-hook,0),0))
                point_list.append((AllplanGeo.Point3D(-left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right,0,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(-left-math.cos(radian)*hook,hook,0),0))
                point_list.append((AllplanGeo.Point3D(-left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right,0,0),0))
        elif hook_side == 5:
            if mirror:
                point_list.append((AllplanGeo.Point3D(-left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right+math.cos(radian)*hook,-hook,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(-left,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+right+math.cos(radian)*hook,hook,0),0))
        else:
            if mirror:
                point_list.append((AllplanGeo.Point3D(-extend-math.cos(radian)*hook,-hook,0),0))
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend+math.cos(radian)*hook,-hook,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(-extend-math.cos(radian)*hook,hook,0),0))
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend+math.cos(radian)*hook,hook,0),0))

        shape_build = AllplanReinf.ReinforcementShapeBuilder()
        shape_build.AddPoints(point_list)

        shape = shape_build.CreateShape(self._shape_props)
        if vertical:
            angle = RotationAngles(rotate,-90,0)
        else:
            angle = RotationAngles(rotate,0,0)
        shape.Rotate(angle)
        if shape.IsValid():
            return shape