# -*- coding: utf-8 -*-
# @Time    : 2017/09/20
# @Author  : kingsley kuang
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : wall.py 樑源码文件
# @Software: 
# @Function: 
"""
Example Script for an liang
"""


import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Utility as AllplanUtility          # allplan util library


import StdReinfShapeBuilder.GeneralReinfShapeBuilder as GeneralShapeBuilder
import StdReinfShapeBuilder.LinearBarPlacementBuilder as LinearBarBuilder


from StdReinfShapeBuilder.ConcreteCoverProperties import ConcreteCoverProperties
from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties
from StdReinfShapeBuilder.RotationAngles import RotationAngles

from HandleDirection import HandleDirection
from HandleProperties import HandleProperties
from PythonPart import View2D3D, PythonPart   
import math        

from JunheModels.util.LongitudinalBarShape import LongitudinalSteel
from JunheModels.util.Stirrup import Stirrup
from JunheModels.util.calculate import steel_modify

print ('Loading wall.py ' )


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

    element = Wall(doc)
 
    return element.create(build_ele)




class Wall(object):
    '''
    Definition of class Beam
    构件类
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

    def data_update(self,build_dict):
        for key,value in self.__dict__.items():
            build_dict.get_parameter_dict()[key] = value

    def create(self, build_ele):
        '''
        Create the elements
        构造物件函数
        Args:
            build_ele: the building element
            .pyp文件输入参数，build_ele代表整个.pyp文件信息

        Returns:
            tuple with created elements and handles.
            被创造元素以及其句柄，由元祖打包返回
        '''
        views_list = []
        #读取数据
        self.data_read(build_ele.get_parameter_dict())
        #建立游标
        self.create_handle()
        
        self.texturedef = AllplanBasisElements.TextureDefinition(build_ele.Surface.value)

        polyhedron = self.create_geometry()


        reinforcement = self.create_reinforcement()
        
        



        
        views_list += polyhedron
        views = [View2D3D(views_list)]
        
        pythonpart = PythonPart ("Wall",                                             #ID
                                 parameter_list = build_ele.get_params_list(),          #.pyp 参数列表
                                 hash_value     = build_ele.get_hash(),                 #.pyp 哈希值
                                 python_file    = build_ele.pyp_file_name,              #.pyp 文件名
                                 views          = views,                                #图形视图
                                 reinforcement  = reinforcement,                        #增强构建
                                 common_props   = self.com_prop)                        #格式参数





        self.model_ele_list = pythonpart.create()

        return (self.model_ele_list, self.handle_list)

    def create_geometry(self):
        '''
        Create the element geometries
        构建元素几何图形函数

        Args:
            build_ele: the building element
            .pyp文件输入参数，build_ele代表整个.pyp文件信息
        '''


        #point
        from_point = AllplanGeo.Point3D(0,0,0)                  
        to_point = AllplanGeo.Point3D(self.Length,self.Width,self.Height)      

        rectangle = AllplanGeo.Polyhedron3D.CreateCuboid(from_point,to_point) #矩形

        
        return [AllplanBasisElements.ModelElement3D(self.com_prop,self.texturedef, rectangle)]


    def create_reinforcement(self):
        '''
        Create the reinforcement element
        构造并添加增强构建函数

        Args:
            build_ele: the building element
            .pyp文件输入参数，buile_ele代表整个.pyp文件信息
        '''
        reinforcement = []
        horizon,vertical,tie = self.create_horizontal_steel(),self.create_vertical_steel(),self.create_tie_steel()
        for ele_1 in horizon:
            ele_1.SetAttributes(AllplanBaseElements.Attributes([AllplanBaseElements.AttributeSet([AllplanBaseElements.AttributeInteger(1013,self.MarkIndex_Hori)])]))
        for ele_2 in vertical:
            ele_2.SetAttributes(AllplanBaseElements.Attributes([AllplanBaseElements.AttributeSet([AllplanBaseElements.AttributeInteger(1013,self.MarkIndex_Vert)])]))
        for ele_3 in tie:
            ele_3.SetAttributes(AllplanBaseElements.Attributes([AllplanBaseElements.AttributeSet([AllplanBaseElements.AttributeInteger(1013,self.MarkIndex_Tie)])]))


        if self.HoriSteelVisual:
            reinforcement += horizon
        if self.VertSteelVisual:
            reinforcement += vertical
        if self.TieSteelVisual:
            reinforcement += tie


        return reinforcement

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

    def shape_tie_steel(self,length,width):

        bending_shape_type = AllplanReinf.BendingShapeType.OpenStirrup
        rebar_prop = {  'diameter':self.TieSteelDia,
                        'bending_roller':0,
                        'steel_grade':self.TieSteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':bending_shape_type}      

        angle = RotationAngles(0,0,90)

        #保护层混凝土属性
        concrete_props = ConcreteCoverProperties.all(self.HoriFrontCover - self.HoriSteelDia)

        #箍筋属性
        shape_props = ReinforcementShapeProperties.rebar(**rebar_prop)

        #
        args = {'length':length,
                'width':width,
                'shape_props':shape_props,
                'concrete_cover_props':concrete_props,
                'model_angles':angle,
                'start_hook':self.TieSteelHook,
                'end_hook':self.TieSteelHook,
                'start_hook_angle':-45,
                'end_hook_angle':-45}

        shape = GeneralShapeBuilder.create_open_stirrup(**args)
        if shape.IsValid():
            return shape

    def create_horizontal_steel(self):
        steel_list = []

        cover = ConcreteCoverProperties.left_right(self.HoriSideCover,self.HoriSideCover)
        rebar_prop = {  'diameter':self.HoriSteelDia,
                        'bending_roller':0,
                        'steel_grade':self.HoriSteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':AllplanReinf.BendingShapeType.LongitudinalBar}    

        longit = LongitudinalSteel(cover,rebar_prop)

        steel_hs1 = longit.shape_steel(self.Length)

        if not self.Degrees_HS2:
            steel_hs2_1 = steel_hs2_2 = longit.shape_extend_steel(self.Length,self.HoriExtend)
        else:
            steel_hs2_1 = longit.shape_hook_steel(self.Length,self.DegreesHook_HS2,hook_side=3,left=self.LeftAnchor_HS2,right=self.RightAnchor_HS2,mirror=False)
            steel_hs2_2 = longit.shape_hook_steel(self.Length,self.DegreesHook_HS2,hook_side=3,left=self.LeftAnchor_HS2,right=self.RightAnchor_HS2,mirror=True)

        point_f_1 = AllplanGeo.Point3D(0,0,0)
        point_t_1 = AllplanGeo.Point3D(0,0,self.Height)

        lines = int((self.Height - self.HoriTopCover - self.HoriBottomCover - self.HoriSteelDia) / self.HoriDistance)
        point_f = AllplanGeo.Point3D(0,0,0)
        point_t = AllplanGeo.Point3D(self.Length,self.Width,self.Height)
        vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.HoriDistance,0,0))
        distance = self.HoriBottomCover
        for x in range(lines + 1):
            
            if x % 3 != 0:
                s_shape_hs1_1 = AllplanReinf.BendingShape(steel_hs1)
                s_shape_hs1_1.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(0,self.HoriFrontCover,distance)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f,point_t,s_shape_hs1_1))
                s_shape_hs1_2 = AllplanReinf.BendingShape(steel_hs1)
                s_shape_hs1_2.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(0,self.Width-self.HoriFrontCover,distance)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f,point_t,s_shape_hs1_2))
            else:
                s_shape_hs2_1 = AllplanReinf.BendingShape(steel_hs2_1)
                s_shape_hs2_1.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(0,self.HoriFrontCover,distance)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f,point_t,s_shape_hs2_1))
                s_shape_hs2_2 = AllplanReinf.BendingShape(steel_hs2_2)
                s_shape_hs2_2.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(0,self.Width-self.HoriFrontCover,distance)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f,point_t,s_shape_hs2_2))
            distance += self.HoriDistance

        if steel_modify(self.Height,self.HoriSteelDia,self.HoriDistance,self.HoriBottomCover,self.HoriTopCover):
            if (lines + 1) % 3 != 0:
                s_shape_hs1_1 = AllplanReinf.BendingShape(steel_hs1)
                s_shape_hs1_1.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(0,self.HoriFrontCover,self.Height-self.HoriTopCover)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f,point_t,s_shape_hs1_1))
                s_shape_hs1_2 = AllplanReinf.BendingShape(steel_hs1)
                s_shape_hs1_2.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(0,self.Width-self.HoriFrontCover,self.Height-self.HoriTopCover)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f,point_t,s_shape_hs1_2))
            else:
                s_shape_hs2_1 = AllplanReinf.BendingShape(steel_hs2_1)
                s_shape_hs2_1.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(0,self.HoriFrontCover,self.Height-self.HoriTopCover)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f,point_t,s_shape_hs2_1))
                s_shape_hs2_2 = AllplanReinf.BendingShape(steel_hs2_2)
                s_shape_hs2_2.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(0,self.Width-self.HoriFrontCover,self.Height-self.HoriTopCover)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f,point_t,s_shape_hs2_2))                           

        return steel_list


    def create_vertical_steel(self):
        steel_list = []

        cover = [self.Length_BA,self.Length_BA,self.Length_BA,self.Length_BA]
        rebar_prop = {  'diameter':self.HoriSteelDia,
                        'bending_roller':0,
                        'steel_grade':self.HoriSteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':AllplanReinf.BendingShapeType.LongitudinalBar}    

        longit = LongitudinalSteel(cover,rebar_prop)
        if self.BendingAnchor:
            steel_vert_1 = longit.shape_anchor_steel(self.Height,self.Length_TA,self.BendPosition,self.BendLength,self.BendWidth,2,False,True)
            steel_vert_2 = longit.shape_anchor_steel(self.Height,self.Length_TA,self.BendPosition,self.BendLength,self.BendWidth,2,True,True)

        else:
            steel_vert_1 = steel_vert_2 = longit.shape_extend_steel(length=self.Height,extend=self.Length_TA,extend_side=2,vertical=True)

        point_f_1 = AllplanGeo.Point3D(0,self.HoriFrontCover + self.HoriSteelDia,0)
        point_t_1 = AllplanGeo.Point3D(self.Length,self.HoriFrontCover + self.HoriSteelDia,0)

        steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                        steel_vert_1,
                                                                                        point_f_1,
                                                                                        point_t_1,
                                                                                        self.VertSideCover,
                                                                                        self.VertSideCover,
                                                                                        self.VertDistance,
                                                                                        3))

        point_f_2 = AllplanGeo.Point3D(0,self.Width - self.HoriFrontCover - self.HoriSteelDia,0)
        point_t_2 = AllplanGeo.Point3D(self.Length,self.Width - self.HoriFrontCover - self.HoriSteelDia,0)

        steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                        steel_vert_2,
                                                                                        point_f_2,
                                                                                        point_t_2,
                                                                                        self.VertSideCover,
                                                                                        self.VertSideCover,
                                                                                        self.VertDistance,
                                                                                        3))

        if steel_modify(self.Length,self.VertSteelDia,self.VertDistance,self.VertSideCover,self.VertSideCover):
            point_f_3 = AllplanGeo.Point3D(0,0,0)
            point_t_3 = AllplanGeo.Point3D(self.Length ,0,0)
            vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.VertDistance / 2,0,0))
            s_shape_1 = AllplanReinf.BendingShape(steel_vert_1)
            s_shape_1.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.Length - self.VertSideCover,self.HoriFrontCover + self.HoriSteelDia,0)))
            s_shape_2 = AllplanReinf.BendingShape(steel_vert_2)
            s_shape_2.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.Length - self.VertSideCover,self.Width-self.HoriFrontCover - self.HoriSteelDia,0)))
            steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f_3,point_t_3,s_shape_1))
            steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f_3,point_t_3,s_shape_2))

        return steel_list

    def create_tie_steel(self):
        steel_list = []
        tie_shape = self.shape_tie_steel(self.Width,4*self.TieSteelDia)

        distance = self.HoriBottomCover + self.HoriSteelDia


        lines = int((self.Height - self.HoriTopCover - self.HoriBottomCover - self.HoriSteelDia) / self.HoriDistance)
        rows = int((self.Length - 2 * self.VertSideCover - self.VertSteelDia) / self.VertDistance)
        if self.TieMode == 1:
            for x in range(lines+1):

                point_f = AllplanGeo.Point3D(2 * self.VertSteelDia,0,distance)
                point_t = AllplanGeo.Point3D(self.Length + 2 * self.VertSteelDia,0,distance)
                if x % 3 == 0:
                    steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                                tie_shape,
                                                                                                point_f,
                                                                                                point_t,
                                                                                                self.VertSideCover,
                                                                                                self.VertSideCover,
                                                                                                3*self.VertDistance,
                                                                                                3))   

                distance += self.HoriDistance
            #last row
            if steel_modify(self.Height,self.HoriSteelDia,self.HoriDistance,self.HoriBottomCover,self.HoriTopCover) and (lines + 1) % 3 == 0:
                point_f = AllplanGeo.Point3D(2 * self.VertSteelDia,0,self.Height - self.HoriTopCover + self.HoriSteelDia)
                point_t = AllplanGeo.Point3D(self.Length + 2 * self.VertSteelDia,0,self.Height - self.HoriTopCover + self.HoriSteelDia)     
                steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                            tie_shape,
                                                                                            point_f,
                                                                                            point_t,
                                                                                            self.VertSideCover,
                                                                                            self.VertSideCover,
                                                                                            3*self.VertDistance,
                                                                                            3))       



            #last line
            if steel_modify(self.Length,self.VertSteelDia,self.VertDistance,self.VertSideCover,self.VertSideCover) and (rows + 1) % 3 == 0:
                l_distance = self.HoriBottomCover + self.HoriSteelDia
                for y in range(lines + 1):
                    if y % 3 == 0:
                        point_f_e = AllplanGeo.Point3D(0,0,0)
                        point_t_e = AllplanGeo.Point3D(self.Length ,0,0)
                        vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.VertDistance / 2,0,0))
                        s_shape = AllplanReinf.BendingShape(tie_shape)
                        s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.Length - self.VertSideCover - self.VertSteelDia + 2 * self.VertSteelDia,0,l_distance)))
                        steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f_e,point_t_e,s_shape))
                    l_distance += self.HoriDistance
                #last line & row
                if steel_modify(self.Height,self.HoriSteelDia,self.HoriDistance,self.HoriBottomCover,self.HoriTopCover) and (lines + 1) % 3 == 0:
                    point_f_e = AllplanGeo.Point3D(0,0,0)
                    point_t_e = AllplanGeo.Point3D(self.Length ,0,0)
                    vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.VertDistance / 2,0,0))
                    s_shape = AllplanReinf.BendingShape(tie_shape)
                    s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.Length - self.VertSideCover - self.VertSteelDia + 2 * self.VertSteelDia,0,self.Height - self.HoriTopCover + self.HoriSteelDia)))
                    steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f_e,point_t_e,s_shape))   

        elif self.TieMode == 2:
            distance = self.VertSideCover + 2 * self.VertSteelDia 
            for x in range(rows + 1):             

                if x % 4 == 0:
                    point_f = AllplanGeo.Point3D(distance,0,self.HoriSteelDia)
                    point_t = AllplanGeo.Point3D(distance,0,self.Height + self.HoriSteelDia)
                    steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                                tie_shape,
                                                                                                point_f,
                                                                                                point_t,
                                                                                                self.HoriBottomCover,
                                                                                                self.HoriTopCover,
                                                                                                4*self.HoriDistance,
                                                                                                3))  
                if (x + 2) % 4 == 0 and x != 0:
                    point_f = AllplanGeo.Point3D(distance,0,self.HoriSteelDia + 2*self.HoriDistance)
                    point_t = AllplanGeo.Point3D(distance,0,self.Height + self.HoriSteelDia)
                    steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                                tie_shape,
                                                                                                point_f,
                                                                                                point_t,
                                                                                                self.HoriBottomCover,
                                                                                                self.HoriTopCover,
                                                                                                4*self.HoriDistance,
                                                                                                3))

                distance += self.VertDistance

            if steel_modify(self.Length,self.VertSteelDia,self.VertDistance,self.VertSideCover,self.VertSideCover):
                if (rows + 1) % 4 == 0:
                    point_f = AllplanGeo.Point3D(self.Length - self.VertSideCover,0,self.HoriSteelDia)
                    point_t = AllplanGeo.Point3D(self.Length - self.VertSideCover,0,self.Height + self.HoriSteelDia)
                    steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                                tie_shape,
                                                                                                point_f,
                                                                                                point_t,
                                                                                                self.HoriBottomCover,
                                                                                                self.HoriTopCover,
                                                                                                4*self.HoriDistance,
                                                                                                3))
                if (rows + 3) % 4 == 0:
                    point_f = AllplanGeo.Point3D(self.Length - self.VertSideCover,0,self.HoriSteelDia + 2*self.HoriDistance)
                    point_t = AllplanGeo.Point3D(self.Length - self.VertSideCover,0,self.Height + self.HoriSteelDia)
                    steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                                tie_shape,
                                                                                                point_f,
                                                                                                point_t,
                                                                                                self.HoriBottomCover,
                                                                                                self.HoriTopCover,
                                                                                                4*self.HoriDistance,
                                                                                                3))
            #last row
            if steel_modify(self.Height,self.HoriSteelDia,self.HoriDistance,self.HoriBottomCover,self.HoriTopCover):
                if(lines + 1) % 4 == 0:
                    r_distance = self.VertSideCover + 2 * self.VertSteelDia

                    for z1 in range(rows + 1):
                        if z1 % 4 == 0:
                            point_f_e = AllplanGeo.Point3D(0,0,0)
                            point_t_e = AllplanGeo.Point3D(self.Length ,0,0)
                            vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.HoriDistance / 2,0,0))
                            s_shape = AllplanReinf.BendingShape(tie_shape)
                            s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(r_distance,0,self.Height - self.HoriTopCover + self.HoriSteelDia)))
                            steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f_e,point_t_e,s_shape))   
                        r_distance += self.VertDistance             
                        #last row & line
                        if steel_modify(self.Length,self.VertSteelDia,self.VertDistance,self.VertSideCover,self.VertSideCover) and (rows + 1) % 4 == 0:                    
                            point_f_e = AllplanGeo.Point3D(0,0,0)
                            point_t_e = AllplanGeo.Point3D(self.Length ,0,0)
                            vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.HoriDistance / 2,0,0))
                            s_shape = AllplanReinf.BendingShape(tie_shape)
                            s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.Length - self.VertSideCover - self.VertSteelDia + 2 * self.VertSteelDia,0,self.Height - self.HoriTopCover + self.HoriSteelDia)))
                            steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f_e,point_t_e,s_shape))

                #last row
                if (lines + 3) % 4 == 0:
                    r_distance = self.VertSideCover + 2 * self.VertSteelDia
                    
                    for z2 in range(rows + 1):
                        if (z2 + 2) % 4 == 0:
                            point_f_e = AllplanGeo.Point3D(0,0,0)
                            point_t_e = AllplanGeo.Point3D(self.Length ,0,0)
                            vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.HoriDistance / 2,0,0))
                            s_shape = AllplanReinf.BendingShape(tie_shape)
                            s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(r_distance,0,self.Height - self.HoriTopCover + self.HoriSteelDia)))
                            steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f_e,point_t_e,s_shape))  
                        r_distance += self.VertDistance 
                        #last row & line
                        if steel_modify(self.Length,self.VertSteelDia,self.VertDistance,self.VertSideCover,self.VertSideCover) and (rows + 3) % 4 == 0:
                            point_f_e = AllplanGeo.Point3D(0,0,0)
                            point_t_e = AllplanGeo.Point3D(self.Length ,0,0)
                            vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.HoriDistance / 2,0,0))
                            s_shape = AllplanReinf.BendingShape(tie_shape)
                            s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.Length - self.VertSideCover - self.VertSteelDia + 2 * self.VertSteelDia,0,self.Height - self.HoriTopCover + self.HoriSteelDia)))
                            steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_f_e,point_t_e,s_shape))



                    




        return steel_list     


