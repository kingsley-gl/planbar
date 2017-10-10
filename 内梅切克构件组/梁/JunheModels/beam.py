#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

print ('Loading beam_one.py ' )


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
        
        pythonpart = PythonPart ("Beam",                                             #ID
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

        stir,longit,waist,tie = self.create_stirrup(),self.create_longitudinal_steel(),self.create_waist_steel(),self.create_tie_steel()

        for ele_1 in stir:
            ele_1.SetAttributes(AllplanBaseElements.Attributes([AllplanBaseElements.AttributeSet([AllplanBaseElements.AttributeInteger(1013,10)])]))
        for ele_2 in longit:
            ele_2.SetAttributes(AllplanBaseElements.Attributes([AllplanBaseElements.AttributeSet([AllplanBaseElements.AttributeInteger(1013,11)])]))
        for ele_3 in waist:
            ele_3.SetAttributes(AllplanBaseElements.Attributes([AllplanBaseElements.AttributeSet([AllplanBaseElements.AttributeInteger(1013,12)])]))
        for ele_4 in tie:
            ele_4.SetAttributes(AllplanBaseElements.Attributes([AllplanBaseElements.AttributeSet([AllplanBaseElements.AttributeInteger(1013,13)])]))

        if self.StirrupVisual:
            reinforcement += stir
        if self.LongBarVisual:
            reinforcement += longit
        if self.WaistBarVisual:
            reinforcement += waist
        if self.TieBarVisual:
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
    def shape_stirrup(self,stir_type):
        '''
        箍筋建模函数
        Args:
            build_ele: build_ele.get_parameter_dict()
            build_ele: .pyp文件内的 Name标签的参数字典
        '''
        #参数
        bending_shape_type = AllplanReinf.BendingShapeType.Stirrup
        rebar_prop = {  'diameter':self.StirDiameter,
                        'bending_roller':math.pi * 3*self.StirDiameter / 40,
                        'steel_grade':self.StirSteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':bending_shape_type}      

        #保护层混凝土属性
        concrete_props = ConcreteCoverProperties(self.StirSideCover,self.StirSideCover,self.StirUpsCover,self.StirUpsCover)

        #箍筋属性
        shape_props = ReinforcementShapeProperties.rebar(**rebar_prop)


        stirrup = Stirrup(concrete_props,shape_props)

        if stir_type == 1:
            # model_angles = RotationAngles(90,0,90)
            shape = stirrup.shape_open_stirrup(self.Height,self.Width,self.StirOneExtendLength,self.StirrupOneHookLength,1,135,True)

        elif stir_type == 2:

            #建立箍筋模型
            model_angles = RotationAngles(0,-90,0)
            shape = stirrup.shape_stirrup(self.Height,self.Width,self.StirTwoExtendLength,1,True)

        return shape

    def create_stirrup(self):

        stirrup_list = []


        #构模
        shape_stirrup = self.shape_stirrup(self.StirrupType)   
        
        point_f_1 = AllplanGeo.Point3D(0,0,0)
        point_t_1 = AllplanGeo.Point3D(self.StirDenseRegionLength,0,0)
        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                          shape_stirrup,
                                                                          point_f_1,
                                                                          point_t_1,
                                                                          self.StirBothEndLength,
                                                                          0,
                                                                          self.StirDenseRegionDistance,
                                                                          3) )

        point_f_2 = AllplanGeo.Point3D(self.Length-self.StirDenseRegionLength,0,0)
        point_t_2 = AllplanGeo.Point3D(self.Length,0,0)       
        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                          shape_stirrup,
                                                                          point_f_2,
                                                                          point_t_2,
                                                                          0,
                                                                          self.StirBothEndLength,
                                                                          self.StirDenseRegionDistance,
                                                                          2) )

        point_f = AllplanGeo.Point3D(self.StirDenseRegionLength,0,0)
        point_t = AllplanGeo.Point3D(self.Length-self.StirDenseRegionLength,0,0)       
        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                          shape_stirrup,
                                                                          point_f,
                                                                          point_t,
                                                                          self.StirDenseRegionDistance/2,
                                                                          self.StirDenseRegionDistance/2,
                                                                          self.StirrupSparseRegionDistance,
                                                                          3) )

        if steel_modify(self.Length-2*self.StirDenseRegionLength,
                        self.StirDiameter,self.StirrupSparseRegionDistance,
                        self.StirDenseRegionDistance/2,self.StirDenseRegionDistance/2):
            point_cnt_1 = AllplanGeo.Point3D(self.StirDenseRegionLength,0,0)
            point_cnt_2 = AllplanGeo.Point3D(self.Length,0,0)
            vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.StirrupSparseRegionDistance / 2,0,0))
            s_shape = AllplanReinf.BendingShape(shape_stirrup)
            s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.Length-self.StirDenseRegionLength,
                                                                    0,
                                                                    0)))
            stirrup_list.append(AllplanReinf.BarPlacement(0,1,vec,point_cnt_1,point_cnt_2,s_shape))

        return stirrup_list


    def create_longitudinal_steel(self):
        steel_list = []

        cover = ConcreteCoverProperties(self.StirSideCover+self.StirDiameter,
                                        self.StirSideCover+self.StirDiameter,
                                        self.StirUpsCover+self.StirDiameter,
                                        self.StirUpsCover+self.StirDiameter)

        rebar_prop = {  'bending_roller':0,
                        'steel_grade':self.SteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':AllplanReinf.BendingShapeType.LongitudinalBar}  

        rebar_prop.update({'diameter':self.BarDiameter_B1})
        longit_B1 = LongitudinalSteel(cover,rebar_prop)
        rebar_prop.update({'diameter':self.BarDiameter_BO})
        longit_BO = LongitudinalSteel(cover,rebar_prop)
        rebar_prop.update({'diameter':self.BarDiameter_T1})
        longit_T1 = LongitudinalSteel(cover,rebar_prop)
        rebar_prop.update({'diameter':self.BarDiameter_TO})
        longit_TO = LongitudinalSteel(cover,rebar_prop)


        if self.AnchorHead90_T1 and not self.AnchorTail90_T1:
            T1_steel_shape = longit_T1.shape_hook_steel(self.Length,15*self.BarDiameter_T1,
                                                        left=self.AnchorHead_T1,right=self.AnchorTail_T1,hook_side=4,rotate=90,mirror=True)
        elif not self.AnchorHead90_T1 and self.AnchorTail90_T1:
            T1_steel_shape = longit_T1.shape_hook_steel(self.Length,15*self.BarDiameter_T1,
                                                        left=self.AnchorHead_T1,right=self.AnchorTail_T1,hook_side=5,rotate=90,mirror=True)
        elif self.AnchorHead90_T1 and self.AnchorTail90_T1:
            T1_steel_shape = longit_T1.shape_hook_steel(self.Length,15*self.BarDiameter_T1,
                                                        left=self.AnchorHead_T1,right=self.AnchorTail_T1,hook_side=3,rotate=90,mirror=True)
        else:
            T1_steel_shape = longit_B1.shape_extend_steel(self.Length,left=self.AnchorHead_T1,
                                                            right=self.AnchorTail_T1,extend_side=3)

        T1_point_f = AllplanGeo.Point3D(0,self.StirDiameter+self.StirSideCover
                                        ,self.Height-(self.StirUpsCover+self.StirDiameter))
        T1_point_t = AllplanGeo.Point3D(0,self.Width-self.StirSideCover-self.StirDiameter
                                        ,self.Height-(self.StirUpsCover+self.StirDiameter))        

        steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,T1_steel_shape,T1_point_f,T1_point_t,0,0,self.BarNumber_T1))

        if self.TopSecondRowLongBar:

            if self.AnchorHead90_TO and not self.AnchorTail90_TO:
                TO_steel_shape = longit_TO.shape_hook_steel(self.Length,15*self.BarDiameter_TO,
                                                        left=self.AnchorHead_TO,right=self.AnchorTail_TO,hook_side=4,rotate=90,mirror=True)
            elif self.AnchorTail90_TO and not self.AnchorHead90_TO:
                TO_steel_shape = longit_TO.shape_hook_steel(self.Length,15*self.BarDiameter_TO,
                                                        left=self.AnchorHead_TO,right=self.AnchorTail_TO,hook_side=5,rotate=90,mirror=True)
            elif self.AnchorHead90_TO and self.AnchorTail90_TO:
                TO_steel_shape = longit_TO.shape_hook_steel(self.Length,15*self.BarDiameter_TO,
                                                        left=self.AnchorHead_TO,right=self.AnchorTail_TO,hook_side=3,rotate=90,mirror=True)
            else:
                TO_steel_shape = longit_TO.shape_extend_steel(self.Length,left=self.AnchorHead_TO,
                                                            right=self.AnchorTail_TO,extend_side=3)

            TO_point_f = AllplanGeo.Point3D(0,self.StirDiameter+self.StirSideCover
                                            ,self.Height-(self.StirUpsCover+self.StirDiameter+self.TopBarDistance))
            TO_point_t = AllplanGeo.Point3D(0,self.Width-self.StirSideCover-self.StirDiameter
                                            ,self.Height-(self.StirUpsCover+self.StirDiameter+self.TopBarDistance))
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,TO_steel_shape,TO_point_f,TO_point_t,0,0,self.BarNumber_TO))



        if self.AnchorHead90_B1 and not self.AnchorTail90_B1:
            B1_steel_shape = longit_B1.shape_hook_steel(self.Length,15*self.BarDiameter_B1,
                                                        left=self.AnchorHead_B1,right=self.AnchorTail_B1,hook_side=4,rotate=90)
            
        elif self.AnchorTail90_B1 and not self.AnchorHead90_B1:
            B1_steel_shape = longit_B1.shape_hook_steel(self.Length,15*self.BarDiameter_B1,
                                                        left=self.AnchorHead_B1,right=self.AnchorTail_B1,hook_side=5,rotate=90)
            
        elif self.AnchorHead90_B1 and self.AnchorTail90_B1:
            B1_steel_shape = longit_B1.shape_hook_steel(self.Length,15*self.BarDiameter_B1,
                                                        left=self.AnchorHead_B1,right=self.AnchorTail_B1,hook_side=3,rotate=90)
            
        else:
            B1_steel_shape = longit_B1.shape_extend_steel(self.Length,left=self.AnchorHead_B1,
                                                            right=self.AnchorTail_B1,extend_side=3)
                        

        B1_point_f = AllplanGeo.Point3D(0,self.StirDiameter+self.StirSideCover
                                        ,self.StirUpsCover+self.StirDiameter)
        B1_point_t = AllplanGeo.Point3D(0,self.Width-self.StirSideCover-self.StirDiameter
                                        ,self.StirUpsCover+self.StirDiameter)

        steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,B1_steel_shape,B1_point_f,B1_point_t,0,0,self.BarNumber_B1))

        if self.BottomSecondRowLongBar:

            if self.AnchorHead90_BO and not self.AnchorTail90_BO:
                BO_steel_shape = longit_BO.shape_hook_steel(self.Length,15*self.BarDiameter_BO,
                                                        left=self.AnchorHead_BO,right=self.AnchorTail_BO,hook_side=4,rotate=90)
            elif self.AnchorTail90_BO and not self.AnchorHead90_BO:
                BO_steel_shape = longit_BO.shape_hook_steel(self.Length,15*self.BarDiameter_BO,
                                                        left=self.AnchorHead_BO,right=self.AnchorTail_BO,hook_side=5,rotate=90)
            elif self.AnchorHead90_BO and self.AnchorTail90_BO:
                BO_steel_shape = longit_BO.shape_hook_steel(self.Length,15*self.BarDiameter_BO,
                                                        left=self.AnchorHead_BO,right=self.AnchorTail_BO,hook_side=3,rotate=90)
            else:
                BO_steel_shape = longit_BO.shape_extend_steel(self.Length,left=self.AnchorHead_BO,
                                                            right=self.AnchorTail_BO,extend_side=3)

            BO_point_f = AllplanGeo.Point3D(0,self.StirDiameter+self.StirSideCover
                                            ,self.StirUpsCover+self.StirDiameter+self.BottomBarDistance)
            BO_point_t = AllplanGeo.Point3D(0,self.Width-self.StirSideCover-self.StirDiameter
                                            ,self.StirUpsCover+self.StirDiameter+self.BottomBarDistance)
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,BO_steel_shape,BO_point_f,BO_point_t,0,0,self.BarNumber_BO))



        return steel_list


    def create_waist_steel(self):
        steel_list = []

        cover = ConcreteCoverProperties(self.StirSideCover+self.StirDiameter,
                                        self.StirSideCover+self.StirDiameter,
                                        0,
                                        0)

        rebar_prop = {  'diameter':self.WaistBarDiameter,
                        'bending_roller':0,
                        'steel_grade':self.WaistBarSteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':AllplanReinf.BendingShapeType.LongitudinalBar} 

        waist = LongitudinalSteel(cover,rebar_prop)

        if self.AnchorHead90_W and not self.AnchorTail90_W:
            waist_shape = waist.shape_hook_steel(length=self.Length,hook=15*self.WaistBarDiameter,
                                                left=self.AnchorHead_W,right=self.AnchorTail_W,rotate=90,hook_side=4)
        elif not self.AnchorHead90_W and self.AnchorTail90_W:
            waist_shape = waist.shape_hook_steel(length=self.Length,hook=15*self.WaistBarDiameter,
                                                left=self.AnchorHead_W,right=self.AnchorTail_W,rotate=90,hook_side=5)
        elif self.AnchorHead90_W and self.AnchorTail90_W:
            waist_shape = waist.shape_hook_steel(length=self.Length,hook=15*self.WaistBarDiameter,
                                                left=self.AnchorHead_W,right=self.AnchorTail_W,rotate=90,hook_side=3)
        else:
            waist_shape = waist.shape_extend_steel(length=self.Length,left=self.AnchorHead_W,right=self.AnchorTail_W,extend_side=3)

        distance = 0
        for x in range(self.WaistRows):
            W_point_f = AllplanGeo.Point3D(0,self.StirDiameter+self.StirSideCover
                                            ,self.WaistPosition+distance)
            W_point_t = AllplanGeo.Point3D(0,self.Width-self.StirSideCover-self.StirDiameter
                                            ,self.WaistPosition+distance)

            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_count(0,waist_shape,W_point_f,W_point_t,0,0,2))
            distance += self.WaistDistance

        return steel_list


    def create_tie_steel(self):
        steel_list = []

        cover = ConcreteCoverProperties(self.StirSideCover+self.StirDiameter,
                                        self.StirSideCover+self.StirDiameter,
                                        0,
                                        0)

        rebar_prop = {  'diameter':self.TieBarDia,
                        'bending_roller':0,
                        'steel_grade':self.TieBarGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':AllplanReinf.BendingShapeType.LongitudinalBar} 

        tie = Stirrup(cover,rebar_prop)

        tie_shape = tie.shape_tie_steel(self.Width+3*self.StirDiameter+2*self.TieBarDia,4*self.TieBarDia,RotationAngles(225,0,90),hook=self.TieBendingLength,degrees=self.TieBarAngle)

        distance = 0
        for x in range(self.WaistRows):
            point_f_1 = AllplanGeo.Point3D(-self.StirDiameter,
                                            -1.5*self.StirDiameter-self.TieBarDia,
                                            self.WaistPosition+self.WaistBarDiameter+distance)
            point_t_1 = AllplanGeo.Point3D(self.StirDenseRegionLength-self.StirDiameter,
                                            -1.5*self.StirDiameter-self.TieBarDia,
                                            self.WaistPosition+self.WaistBarDiameter+distance)

            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                              tie_shape,
                                                                              point_f_1,
                                                                              point_t_1,
                                                                              self.StirBothEndLength,
                                                                              0,
                                                                              self.StirDenseRegionDistance,
                                                                              3) )


            point_f_2 = AllplanGeo.Point3D(self.Length-self.StirDenseRegionLength-self.StirDiameter,
                                            -1.5*self.StirDiameter-self.TieBarDia,
                                            self.WaistPosition+self.WaistBarDiameter+distance)
            point_t_2 = AllplanGeo.Point3D(self.Length-self.StirDiameter,
                                            -1.5*self.StirDiameter-self.TieBarDia,
                                            self.WaistPosition+self.WaistBarDiameter+distance)       
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                              tie_shape,
                                                                              point_f_2,
                                                                              point_t_2,
                                                                              0,
                                                                              self.StirBothEndLength,
                                                                              self.StirDenseRegionDistance,
                                                                              2) )

            point_f = AllplanGeo.Point3D(self.StirDenseRegionLength-self.StirDiameter,
                                        -1.5*self.StirDiameter-self.TieBarDia,
                                        self.WaistPosition+self.WaistBarDiameter+distance)
            point_t = AllplanGeo.Point3D(self.Length-self.StirDenseRegionLength-self.StirDiameter,
                                        -1.5*self.StirDiameter-self.TieBarDia,
                                        self.WaistPosition+self.WaistBarDiameter+distance)       
            steel_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                              tie_shape,
                                                                              point_f,
                                                                              point_t,
                                                                              self.StirDenseRegionDistance/2,
                                                                              self.StirDenseRegionDistance/2,
                                                                              self.StirrupSparseRegionDistance,
                                                                              3) )

            if steel_modify(self.Length-2*self.StirDenseRegionLength,
                self.StirDiameter,self.StirrupSparseRegionDistance,
                self.StirDenseRegionDistance/2,self.StirDenseRegionDistance/2):
                point_cnt_1 = AllplanGeo.Point3D(self.StirDenseRegionLength,0,0)
                point_cnt_2 = AllplanGeo.Point3D(self.Length,0,0)
                vec = AllplanGeo.Vector3D(AllplanGeo.Point3D(0,0,0),AllplanGeo.Point3D(self.StirrupSparseRegionDistance / 2,0,0))
                s_shape = AllplanReinf.BendingShape(tie_shape)
                s_shape.Move(AllplanGeo.Vector3D(AllplanGeo.Point3D(self.Length-self.StirDenseRegionLength-self.StirDiameter,
                                                                        -1.5*self.StirDiameter-self.TieBarDia,
                                                                        self.WaistPosition+self.WaistBarDiameter+distance)))
                steel_list.append(AllplanReinf.BarPlacement(0,1,vec,point_cnt_1,point_cnt_2,s_shape))

            distance += self.WaistDistance

        return steel_list