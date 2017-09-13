# -*- coding: utf-8 -*-
# @Time    : 2017/08/11
# @Author  : kingsley kuang
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : beam_chn_std.py 樑源码文件
# @Software: 
# @Function: 
"""
Example Script for beam
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Utility as AllplanUtility          
import NemAll_Python_Palette as AllplanPalette


import StdReinfShapeBuilder.GeneralReinfShapeBuilder as GeneralShapeBuilder
import StdReinfShapeBuilder.LinearBarPlacementBuilder as LinearBarBuilder


from StdReinfShapeBuilder.ConcreteCoverProperties import ConcreteCoverProperties
from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties
from StdReinfShapeBuilder.RotationAngles import RotationAngles
import GeometryValidate as GeometryValidate

from HandleDirection import HandleDirection
from HandleProperties import HandleProperties
from PythonPart import View2D3D, PythonPart   
import logging
import math        


# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='e:\\myapp.log',
#                     filemode='w')

print ('Loading beam.py ' )



#程序接口
def check_allplan_version(build_ele, version):
    """
    Check the current Allplan version                 

    Args:
        build_ele:  the building element.
        version:   the current Allplan version

    Returns:
        True/False if version is supported by this script
    """

    # Delete unused arguments
    del build_ele
    del version

    # Support all versions
    return True
#程序接口
def move_handle(build_ele, handle_prop, input_pnt, doc):
    """
    Modify the element geometry by handles           

    Args:
        build_ele:  the building element.
        handle_prop handle properties
        input_pnt:  input point
        doc:        input document
    """

    build_ele.change_property(handle_prop, input_pnt)
    return create_element(build_ele, doc)
#程序接口
def create_element(build_ele, doc):
    """
    Creation of element

    Args:
        build_ele: the building element.            
        doc:       input document
    Return:
        tuple of element_list and handle_list
    """
    

    

    element = Beam(doc)
 
    return element.create(build_ele)




class Beam(object):
    '''
    Definition of class Beam
    梁构件类
    '''
    def __init__(self, doc):
        '''
        Initialisation of class Beam
        初始化函数
        Args:
            doc: Input document
            文档输入
        '''
        self.model_ele_list = None
        self.handle_list = []
        self.document = doc


        #获取画笔信息
        self.texturedef = None

        self.com_prop = AllplanBaseElements.CommonProperties()
        self.com_prop.GetGlobalProperties()
        
    def data_read(self,build_dict):

        for key,value in build_dict.items():
            self.__dict__[key] = value

    def create(self, build_ele):
        '''
        Create the elements
        构造物件函数
        Args:
            build_ele: the building element
            .pyp文件输入参数，build_ele代表整个.pyp文件的信息句柄

        Returns:
            tuple with created elements and handles.
            被创造元素以及其句柄，由元祖打包返回
        '''

        self.data_read(build_ele.get_parameter_dict())
        self.texturedef = AllplanBasisElements.TextureDefinition(self.Surface)

        polyhedron = self.create_geometry()
        reinforcement = self.create_reinforcement()

        views = [View2D3D(polyhedron)]
        
        pythonpart = PythonPart ("Beam",                                             #ID
                                 parameter_list = build_ele.get_params_list(),          #.pyp 参数列表
                                 hash_value     = build_ele.get_hash(),                 #.pyp 哈希值
                                 python_file    = build_ele.pyp_file_name,              #.pyp 文件名
                                 views          = views,                                #图形视图
                                 reinforcement  = reinforcement,                        #增强构建
                                 common_props   = self.com_prop)                        #格式参数



        # self.create_handle()

        self.model_ele_list = pythonpart.create()

        return (self.model_ele_list, self.handle_list)

    def create_geometry(self):
        '''
        Create the element geometries
        构建元素几何图形函数
        return 图形list
        '''

        #point
        rectangle = self.shape_cuboid(self.Length,self.Width,self.Height)

        cutter = self.shape_cuboid(self.CutLength,self.Width,self.Height,sX=self.CutPosition)

        slot_head = self.shape_cuboid(self.SlotLength,
                                        self.Width - 2*self.SlotSide,
                                        self.Height - self.SlotBottom,
                                        sY=self.SlotSide,sZ=self.SlotBottom)

        slot_tail = self.shape_cuboid(self.SlotLength,
                                        self.Width - 2*self.SlotSide,
                                        self.Height - self.SlotBottom,
                                        sX=self.Length-self.SlotLength,sY=self.SlotSide,sZ=self.SlotBottom)


        key_slot_1 = self.shape_keyslot(self.KeyslotThick,
                                        self.Width - 2*self.KeyslotSide,
                                        self.KeyslotHeight,
                                        self.KeyslotEdge,
                                        False,
                                        self.SlotLength,
                                        self.KeyslotSide,
                                        self.KeyslotBottom)

        key_slot_2 = self.shape_keyslot(self.KeyslotThick,
                                        self.Width - 2*self.KeyslotSide,
                                        self.KeyslotHeight,
                                        self.KeyslotEdge,
                                        True,
                                        self.CutPosition - self.KeyslotThick,
                                        self.KeyslotSide,
                                        self.KeyslotBottom)

        key_slot_3 = self.shape_keyslot(self.KeyslotThick,
                                        self.Width - 2*self.KeyslotSide,
                                        self.KeyslotHeight,
                                        self.KeyslotEdge,
                                        False,
                                        self.CutPosition + self.CutLength,
                                        self.KeyslotSide,
                                        self.KeyslotBottom)


        key_slot_4 = self.shape_keyslot(self.KeyslotThick,
                                        self.Width - 2*self.KeyslotSide,
                                        self.KeyslotHeight,
                                        self.KeyslotEdge,
                                        True,
                                        self.Length - self.SlotLength - self.KeyslotThick,
                                        self.KeyslotSide,
                                        self.KeyslotBottom)

        err,rectangle = AllplanGeo.MakeSubtraction(rectangle,cutter)
        err,rectangle = AllplanGeo.MakeSubtraction(rectangle,slot_head)
        err,rectangle = AllplanGeo.MakeSubtraction(rectangle,slot_tail)
        err,rectangle = AllplanGeo.MakeSubtraction(rectangle,key_slot_1)
        err,rectangle = AllplanGeo.MakeSubtraction(rectangle,key_slot_2)
        err,rectangle = AllplanGeo.MakeSubtraction(rectangle,key_slot_3)
        err,rectangle = AllplanGeo.MakeSubtraction(rectangle,key_slot_4)


        return [AllplanBasisElements.ModelElement3D(self.com_prop,self.texturedef, rectangle)]




    def create_reinforcement(self):
        '''
        Create the reinforcement element
        构造并添加增强构建函数

        Args:
            build_ele: build_ele.get_parameter_dict()
            build_ele: .pyp文件内的 Name标签的参数字典
        '''
        reinforcement = []
        self.cut_pos_1 = self.CutPosition - self.EndCover  #左段切口位置
        self.last_pos_1 = int((self.CutPosition - self.SlotLength) / self.StirDistance)\
                         * self.StirDistance + self.HeadCover #左段最后一根箍筋位置
        self.cut_pos_2 = self.Length - self.SlotLength - (self.CutPosition + self.CutLength)\
                         - self.HeadCover - self.EndCover - self.StirDiameter #右段切口位置
        self.last_pos_2 = int((self.Length - self.SlotLength - (self.CutPosition + self.CutLength)\
                         - self.HeadCover - self.EndCover - self.StirDiameter) / self.StirDistance)\
                          * self.StirDistance #右段最后一根箍筋位置
        if self.StirVisual:
            reinforcement += self.create_stirrup()
        if self.LongbarVisual:
            reinforcement += self.create_long_steel()
        if self.WaistVisual:
            reinforcement += self.create_waist_steel()
        if self.TieBarVisual:
            reinforcement += self.create_tie_steel()

        return reinforcement

    def shape_cuboid(self,length,width,height,sX=0,sY=0,sZ=0,rX=0,rY=0,rZ=0):

        axis = AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(rX+sX,rY+sY,rZ+sZ),
                                            AllplanGeo.Vector3D(1,0,0),
                                            AllplanGeo.Vector3D(0,0,1))

        args = {'placement':axis,
                'length':length,
                'width':width,
                'height':height}

        shape = AllplanGeo.BRep3D.CreateCuboid(**args)
        return shape

    def shape_keyslot(self,length,width,height,edge,mirror=False,rX=0,rY=0,rZ=0,sX=0,sY=0,sZ=0):
        #bevel_edge = math.sqrt(self.KeyslotEdge^2 + self.KeyslotThick^2) #斜边

        if mirror:
            base_pol1 = AllplanGeo.Polygon3D()
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY+edge,rZ+sZ+edge)
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY+width-edge,rZ+sZ+edge)
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY+width-edge,rZ+sZ+height-edge)
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY+edge,rZ+sZ+height-edge)
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY+edge,rZ+sZ+edge)

            base_pol2 = AllplanGeo.Polygon3D()
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY,rZ+sZ)
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY+width,rZ+sZ)
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY+width,rZ+sZ+height)
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY,rZ+sZ+height)
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY,rZ+sZ)

        else:
            base_pol1 = AllplanGeo.Polygon3D()
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY,rZ+sZ)
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY+width,rZ+sZ)
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY+width,rZ+sZ+height)
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY,rZ+sZ+height)
            base_pol1 += AllplanGeo.Point3D(rX+sX,rY+sY,rZ+sZ)

            #----------------------------------

            base_pol2 = AllplanGeo.Polygon3D()
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY+edge,rZ+sZ+edge)
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY+width-edge,rZ+sZ+edge)
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY+width-edge,rZ+sZ+height-edge)
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY+edge,rZ+sZ+height-edge)
            base_pol2 += AllplanGeo.Point3D(rX+sX+length,rY+sY+edge,rZ+sZ+edge)



        if not GeometryValidate.is_valid(base_pol1):
            return
        if not GeometryValidate.is_valid(base_pol2):
            return 

        err,shape = AllplanGeo.CreatePolyhedron(base_pol1,base_pol2)
        err,shape = AllplanGeo.CreateBRep3D(shape)
        return shape



    def shape_stirrup(self):
        '''
        箍筋建模函数
        Args:
            build_ele: build_ele.get_parameter_dict()
            build_ele: .pyp文件内的 Name标签的参数字典
        '''
        #参数
        bending_shape_type = AllplanReinf.BendingShapeType.Stirrup
        rebar_prop = {  'diameter':self.StirDiameter,
                        'bending_roller':math.pi * self.StirBendDia / 4,
                        'steel_grade':self.StirSteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':bending_shape_type}      



        model_angles = RotationAngles(0,-90,0)

        #保护层混凝土属性
        concrete_props = ConcreteCoverProperties.all(self.ConcreteCover)
        #箍筋属性
        shape_props = ReinforcementShapeProperties.rebar(**rebar_prop)

        #建立箍筋模型
        shape = GeneralShapeBuilder.create_stirrup(self.Height+self.StirExtendLength,
                                                   self.Width,
                                                   model_angles,
                                                   shape_props,
                                                   concrete_props,
                                                   AllplanReinf.StirrupType.Column)
        return shape

    def shape_longitudinal_steel(self,bar_diameter,length,extend=0,bend_flag=False):
        '''
        纵筋建模函数
        
        Args:

        '''


        point_list = []

        if bend_flag:
            shape_type = AllplanReinf.BendingShapeType.Freeform
            if self.AnchorHeadBend:
                point_list.append((AllplanGeo.Point3D(-extend,self.B_VertAnchor,0),0))
                point_list.append((AllplanGeo.Point3D(-self.A_Anchor-self.B_HoriAnchor,self.B_VertAnchor,0),0))
                point_list.append((AllplanGeo.Point3D(-self.A_Anchor,0,0),0))
                point_list.append((AllplanGeo.Point3D(0,0,0),0))
                point_list.append((AllplanGeo.Point3D(length,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend,0,0),0))

            if self.AnchorTailBend:
                point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
                point_list.append((AllplanGeo.Point3D(length,0,0),0))
                point_list.append((AllplanGeo.Point3D(length+self.A_Anchor,0,0),0))    
                point_list.append((AllplanGeo.Point3D(length+self.A_Anchor+self.B_HoriAnchor,self.B_VertAnchor,0),0))
                point_list.append((AllplanGeo.Point3D(length+extend,self.B_VertAnchor,0),0))
        else:
            shape_type = AllplanReinf.BendingShapeType.LongitudinalBar
            point_list.append((AllplanGeo.Point3D(-extend,0,0),0))
            point_list.append((AllplanGeo.Point3D(length+extend,0,0),0))  

        shape_build = AllplanReinf.ReinforcementShapeBuilder()
        shape_build.AddPoints(point_list)

        rebar_prop = {  'diameter':bar_diameter,
                        'bending_roller':0,
                        'steel_grade':self.BarSteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type': shape_type}        
        shape_props = ReinforcementShapeProperties.rebar(**rebar_prop)
        shape = shape_build.CreateShape(shape_props)
        angle = RotationAngles(90,0,0)
        shape.Rotate(angle)
        return shape 

    def shape_waist_steel(self,bar_diameter,point_f,point_t,extend=0,mirror=False):

        point_list = []

        if mirror:
            point_list.append((AllplanGeo.Point3D(point_f-extend,0,0),0))
            point_list.append((AllplanGeo.Point3D(point_t,0,0),0))
        else:
            point_list.append((AllplanGeo.Point3D(point_f,0,0),0))
            point_list.append((AllplanGeo.Point3D(point_t+extend,0,0),0))

        shape_type = AllplanReinf.BendingShapeType.Freeform
        shape_build = AllplanReinf.ReinforcementShapeBuilder()
        shape_build.AddPoints(point_list)        
        rebar_prop = {  'diameter':bar_diameter,
                        'bending_roller':0,
                        'steel_grade':self.WaistBarGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type': shape_type}        
        shape_props = ReinforcementShapeProperties.rebar(**rebar_prop)
        shape = shape_build.CreateShape(shape_props)
        return shape

    def shape_tie_steel(self,length,width):

        bending_shape_type = AllplanReinf.BendingShapeType.OpenStirrup
        rebar_prop = {  'diameter':self.TieBarDia,
                        'bending_roller':0,
                        'steel_grade':self.TieBarGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':bending_shape_type}      

        angle = RotationAngles(90,0,90)

        #保护层混凝土属性
        concrete_props = ConcreteCoverProperties.all(self.ConcreteCover)

        #箍筋属性
        shape_props = ReinforcementShapeProperties.rebar(**rebar_prop)

        #
        args = {'length':length,
                'width':width,
                'shape_props':shape_props,
                'concrete_cover_props':concrete_props,
                'model_angles':angle,
                'start_hook':100,
                'end_hook':100,
                'start_hook_angle':-45,
                'end_hook_angle':-45}

        shape = GeneralShapeBuilder.create_open_stirrup(**args)

        return shape

    def create_handle(self):
        '''
        Create handle
        创建可拉动游标句柄

        '''
        self.handle_list.append(
            HandleProperties("Height",
                                AllplanGeo.Point3D(0, 0, self.Height),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Height", HandleDirection.z_dir)],
                                HandleDirection.z_dir,
                                True))

        self.handle_list.append(
            HandleProperties("Width",
                                AllplanGeo.Point3D(0, self.Width, 0),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Width", HandleDirection.y_dir)],
                                HandleDirection.y_dir,
                                True))

        self.handle_list.append(
            HandleProperties("Length",
                                AllplanGeo.Point3D(self.Length, 0, 0),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Length", HandleDirection.x_dir)],
                                HandleDirection.x_dir,
                                True))

    def create_stirrup(self):

        stirrup_list = []
        point_f_1 = AllplanGeo.Point3D(self.SlotLength,0,0)
        point_t_1 = AllplanGeo.Point3D(self.CutPosition,0,0)


        #构模
        shape_stirrup = self.shape_stirrup()                                                               #箍筋
        

        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                          shape_stirrup,
                                                                                          point_f_1,
                                                                                          point_t_1,
                                                                                          self.HeadCover,
                                                                                          self.EndCover,
                                                                                          self.StirDistance,
                                                                                          3))
        self.cut_pos_1 = self.CutPosition - self.EndCover  #切口位置
        self.last_pos_1 = int((self.CutPosition - self.SlotLength) / self.StirDistance) * self.StirDistance + self.HeadCover #最后一根箍筋位置

        #判断间距添加箍筋
        if self.cut_pos_1 - self.last_pos_1 > self.StirDistance / 2 \
        and self.cut_pos_1 - self.last_pos_1 < self.StirDistance + self.StirDiameter:
            point_cnt_1 = AllplanGeo.Point3D(self.last_pos_1 + self.StirDistance / 2,0,0)
            point_cnt_2 = AllplanGeo.Point3D(self.cut_pos_1,0,0)
            vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.StirDistance / 2,0,0))
            s_shape = AllplanReinf.BendingShape(shape_stirrup)
            s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.cut_pos_1,0,0)))
            stirrup_list.append(AllplanReinf.BarPlacement(0,1,vec,point_cnt_1,point_cnt_2,s_shape))


        point_f_2 = AllplanGeo.Point3D(self.CutPosition + self.CutLength,0,0)
        point_t_2 = AllplanGeo.Point3D(self.Length - self.SlotLength,0,0)

        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(1,
                                                                                          shape_stirrup,
                                                                                          point_t_2,
                                                                                          point_f_2,
                                                                                          self.HeadCover,
                                                                                          self.EndCover,
                                                                                          self.StirDistance,
                                                                                          3))



        if self.cut_pos_2 - self.last_pos_2 > self.StirDistance / 2 \
        and self.cut_pos_2 - self.last_pos_2 < self.StirDistance + self.StirDiameter:
            point_cnt_3 = AllplanGeo.Point3D(self.CutPosition + self.CutLength,0,0)
            point_cnt_4 = AllplanGeo.Point3D(self.Length - self.SlotLength,0,0)
            vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.StirDistance / 2,0,0))
            s_shape = AllplanReinf.BendingShape(shape_stirrup)
            s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.CutPosition + self.CutLength + self.EndCover,0,0)))
            stirrup_list.append(AllplanReinf.BarPlacement(0,1,vec,point_cnt_3,point_cnt_4,s_shape))



        return stirrup_list

    def create_long_steel(self):
        steel_list = []
        if self.AnchorBend:
            fst_shape = self.shape_longitudinal_steel(self.FirstDia,self.Length,self.AnchorBendLength,self.AnchorBend)
        else:
            fst_shape = self.shape_longitudinal_steel(self.FirstDia,self.Length,self.AnchorLength)
        cover = self.ConcreteCover + self.FirstDia/2 + self.StirDiameter
        fst_point_f = AllplanGeo.Point3D(0,0,cover)
        fst_point_t = AllplanGeo.Point3D(0,self.Width,cover)
        steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,fst_shape,fst_point_f,fst_point_t,cover,cover,self.FirstNum))

        other_shape = self.shape_longitudinal_steel(self.OtherDia,self.Length,-self.SlotLength - self.OtherHeadCover)
        distance = 0
        for num in range(self.LongBarLines - 1):
            distance += self.BarDistance
            oth_point_f = AllplanGeo.Point3D(0,0,cover+distance)
            oth_point_t = AllplanGeo.Point3D(0,self.Width,cover+distance)
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,other_shape,oth_point_f,oth_point_t,cover,cover,self.FirstNum))

        return steel_list

    def create_waist_steel(self):
        steel_list = []
        waist_length = (self.Length - self.CutLength - 2*self.WaistHeadCover)/2
        waist_shape = self.shape_waist_steel(self.WaistBarDia,self.WaistHeadCover,self.CutPosition,self.CutBarExtend)
        m_waist_shape = self.shape_waist_steel(self.WaistBarDia,self.CutPosition + self.CutLength,self.Length - self.WaistHeadCover,self.CutBarExtend,True)
        cover = self.ConcreteCover + self.StirDiameter
        # rest_height = self.Height - self.WaistPosition - self.ConcreteCover
        # waist_lines = int(rest_height / self.WaistDistance)
        distance = 0
        for x in range(self.WaistNum):
            point_f = AllplanGeo.Point3D(0,0,self.WaistPosition + distance)
            point_t = AllplanGeo.Point3D(0,self.Width,self.WaistPosition + distance)
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,waist_shape,point_f,point_t,cover,cover,2))

            m_point_f = AllplanGeo.Point3D(0,0,self.WaistPosition + distance)
            m_point_t = AllplanGeo.Point3D(0,self.Width,self.WaistPosition + distance)
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,m_waist_shape,m_point_f,m_point_t,cover,cover,2))
            distance += self.WaistDistance
            # if rest_height - distance > 0 and rest_height - distance < self.WaistDistance:

        return steel_list

    def create_tie_steel(self):
        steel_list = []
        # cover = self.ConcreteCover + self.StirDiameter
        # rest_height = self.Height - self.WaistPosition - self.ConcreteCover
        # waist_lines = int(rest_height / self.WaistDistance)
        tie_shape = self.shape_tie_steel(self.Width,4*self.TieBarDia)
        distance = 0
        for x in range(self.WaistNum):
            point_f_x = AllplanGeo.Point3D(self.SlotLength + self.StirDiameter,0,self.WaistPosition - 2*self.TieBarDia + distance)
            point_t_x = AllplanGeo.Point3D(self.CutPosition + self.StirDiameter,0,self.WaistPosition - 2*self.TieBarDia + distance)
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                            tie_shape,
                                                                                            point_f_x,
                                                                                            point_t_x,
                                                                                            self.HeadCover,
                                                                                            self.EndCover,
                                                                                            self.TieBarRatio*self.StirDistance,
                                                                                            3))
            if self.cut_pos_1 - self.last_pos_1 > self.StirDistance / 2 \
            and self.cut_pos_1 - self.last_pos_1 < self.StirDistance + self.StirDiameter:
                point_cnt_1 = AllplanGeo.Point3D(self.last_pos_1 + self.StirDistance / 2,0,0)
                point_cnt_2 = AllplanGeo.Point3D(self.cut_pos_1,0,0)
                vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.StirDistance / 2,0,0))
                s_shape = AllplanReinf.BendingShape(tie_shape)
                s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.cut_pos_1 + self.StirDiameter ,
                                                                        0,
                                                                        self.WaistPosition - 2*self.TieBarDia + distance)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_cnt_1,point_cnt_2,s_shape))

            distance += self.WaistDistance


        distance = 0
        for y in range(self.WaistNum):
            point_f_y = AllplanGeo.Point3D(self.CutPosition + self.CutLength + self.StirDiameter,0,self.WaistPosition - 2*self.TieBarDia + distance)
            point_t_y = AllplanGeo.Point3D(self.Length - self.SlotLength + self.StirDiameter,0,self.WaistPosition - 2*self.TieBarDia + distance)
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                            tie_shape,
                                                                                            point_t_y,
                                                                                            point_f_y,
                                                                                            self.HeadCover,
                                                                                            self.EndCover,
                                                                                            self.TieBarRatio*self.StirDistance,
                                                                                            3))
            if self.cut_pos_2 - self.last_pos_2 > self.StirDistance / 2 \
            and self.cut_pos_2 - self.last_pos_2 < self.StirDistance + self.StirDiameter:
                point_cnt_3 = AllplanGeo.Point3D(self.CutPosition + self.CutLength,0,0)
                point_cnt_4 = AllplanGeo.Point3D(self.Length - self.SlotLength,0,0)
                vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.StirDistance / 2,0,0))
                s_shape = AllplanReinf.BendingShape(tie_shape)
                s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.CutPosition + self.CutLength + self.EndCover + self.StirDiameter,
                                                                    0,
                                                                    self.WaistPosition - 2*self.TieBarDia + distance)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_cnt_3,point_cnt_4,s_shape))

            distance += self.WaistDistance


        return steel_list