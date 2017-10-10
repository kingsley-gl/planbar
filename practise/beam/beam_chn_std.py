# -*- coding: utf-8 -*-
# @Time    : 2017/08/11
# @Author  : kingsley kuang
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : beam_chn_std.py
# @Software: 横梁源码文件
# @Function: 
"""
Example Script for beam
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

print ('Loading beam_chn_std.py ' )


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
    

    #AllplanUtility.EnablePythonDebug()  #调试开关

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

        polyhedron = self.create_geometry(build_ele.get_parameter_dict())

        reinforcement = self.create_reinforcement(build_ele.get_parameter_dict())
        

        self.texturedef = AllplanBasisElements.TextureDefinition(build_ele.Surface.value)

        views = [View2D3D([AllplanBasisElements.ModelElement3D(self.com_prop,self.texturedef, polyhedron)])]
        
        pythonpart = PythonPart ("Beam_chn_std",                                             #ID
                                 parameter_list = build_ele.get_params_list(),          #.pyp 参数列表
                                 hash_value     = build_ele.get_hash(),                 #.pyp 哈希值
                                 python_file    = build_ele.pyp_file_name,              #.pyp 文件名
                                 views          = views,                                #图形视图
                                 reinforcement  = reinforcement,                        #增强构建
                                 common_props   = self.com_prop)                        #格式参数



        self.create_handle()

        self.model_ele_list = pythonpart.create()

        return (self.model_ele_list, self.handle_list)

    def create_geometry(self, build_ele):
        '''
        Create the element geometries
        构建元素几何图形函数

        Args:
            build_ele: build_ele.get_parameter_dict()
            build_ele: .pyp文件内的 Name标签的参数字典
        '''

        self.length = build_ele['Length'] #长
        self.width = build_ele['Width']   #宽
        self.height = build_ele['Height'] #高

        #point
        from_point = AllplanGeo.Point3D(0,0,0)                  
        to_point = AllplanGeo.Point3D(self.length,self.width,self.height)      

        rectangle = AllplanGeo.Polyhedron3D.CreateCuboid(from_point,to_point) #矩形

        
        return rectangle


    def create_reinforcement(self,build_ele):
        '''
        Create the reinforcement element
        构造并添加增强构建函数

        Args:
            build_ele: build_ele.get_parameter_dict()
            build_ele: .pyp文件内的 Name标签的参数字典
        '''
        reinforcement = []

        #参数
        #-箍筋参数
        high_den_distance = build_ele['HighDensityDistance']                                    #加密区间距
        low_den_distance = build_ele['LowDensityDistance']                                      #非加密区间距
        #-箍筋坐标
        head_high_den_point_f = AllplanGeo.Point3D(0,
                                                   0,
                                                   0)                                           #加密区头部起点
        head_high_den_point_t = AllplanGeo.Point3D(self.height*2,
                                                   0,
                                                   0)                                           #加密区头部终点

        tail_high_den_point_f = AllplanGeo.Point3D(self.length - self.height*2,
                                                   0,
                                                   0)                                           #加密区尾部起点
        tail_high_den_point_t = AllplanGeo.Point3D(self.length,
                                                   0,
                                                   0)                                           #加密区尾部终点

        low_den_point_f = AllplanGeo.Point3D(self.height*2,
                                             0,
                                             0)                                                 #非加密区起点
        low_den_point_t = AllplanGeo.Point3D(self.length - self.height*2,
                                             0,
                                             0)                                                 #非加密区终点

        #-底筋参数
        bottom_bar_extend = build_ele['BottomBarExtendLength']                                  #底筋伸出长度
        bottom_bar_diameter = build_ele['BottomBarDiameter']                                    #底筋直径
        bottom_bar_cnt = build_ele['BottomBarCount']                                            #底筋数量
        bottom_bar_distance = build_ele['BottomBarDistance']                                    #底筋间距
        stir_concrete_cover = build_ele['StirrupConcreteCover']                                 #箍筋保护层厚度
        stir_diameter = build_ele['StirrupDiameter']                                            #箍筋直径
        #-底筋坐标
        bottom_bar_point_f = AllplanGeo.Point3D(0,
                                                stir_concrete_cover + stir_diameter + bottom_bar_diameter/2,
                                                stir_concrete_cover + stir_diameter + bottom_bar_diameter/2)                    #底筋起点
        bottom_bar_point_t = AllplanGeo.Point3D(0,
                                                self.width - stir_concrete_cover - stir_diameter - bottom_bar_diameter/2,
                                                stir_concrete_cover + stir_diameter + bottom_bar_diameter/2)                    #底筋终点

        #-顶筋参数
        top_bar_extend = build_ele['TopBarExtendLength']                                        #顶筋伸出长度
        top_bar_diameter = build_ele['TopBarDiameter']                                          #顶筋直径
        top_bar_cnt = build_ele['TopBarCount']                                                  #顶筋数量
        top_bar_distance = build_ele['TopBarDistance']                                          #顶筋间距
        #-顶筋坐标
        f_top_bar_point_f = AllplanGeo.Point3D(0,
                                               stir_concrete_cover + stir_diameter + bottom_bar_diameter/2,
                                               stir_concrete_cover + stir_diameter + bottom_bar_diameter/2 + 200)
        f_top_bar_point_t = AllplanGeo.Point3D(0,
                                               stir_concrete_cover + stir_diameter + bottom_bar_diameter/2,
                                               self.height)
        b_top_bar_point_f = AllplanGeo.Point3D(0,
                                               self.width - stir_concrete_cover - stir_diameter - bottom_bar_diameter/2,
                                               stir_concrete_cover + stir_diameter + bottom_bar_diameter/2 + 200)
        b_top_bar_point_t = AllplanGeo.Point3D(0,
                                               self.width - stir_concrete_cover - stir_diameter - bottom_bar_diameter/2,
                                               self.height)

        #构模
        shape_stirrup = self.shape_stirrup(build_ele)                                                               #箍筋
        shape_bottom_bar = self.shape_bar(build_ele,bottom_bar_diameter,bottom_bar_extend)                          #底筋
        shape_top_bar = self.shape_bar(build_ele,top_bar_diameter,top_bar_extend)                                   #顶筋

        
        #添加箍筋到加密区头部
        reinforcement.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(0,
                                                                                          shape_stirrup,
                                                                                          head_high_den_point_f,
                                                                                          head_high_den_point_t,
                                                                                          0,
                                                                                          0,
                                                                                          high_den_distance))

        #添加箍筋到加密区尾部
        reinforcement.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(1,
                                                                                          shape_stirrup,
                                                                                          tail_high_den_point_f,
                                                                                          tail_high_den_point_t,
                                                                                          0,
                                                                                          0,
                                                                                          high_den_distance))

        #添加箍筋到非加密区
        reinforcement.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(2,
                                                                                          shape_stirrup,
                                                                                          low_den_point_f,
                                                                                          low_den_point_t,
                                                                                          0,
                                                                                          0,
                                                                                          low_den_distance))

        #添加底筋到梁底部
        reinforcement.append(LinearBarBuilder.create_linear_bar_placement_from_by_dist_count(3,
                                                                                              shape_bottom_bar,
                                                                                              bottom_bar_point_f,
                                                                                              bottom_bar_point_t,
                                                                                              0,
                                                                                              bottom_bar_distance,
                                                                                              bottom_bar_cnt))

        #添加前侧顶筋
        reinforcement.append(LinearBarBuilder.create_linear_bar_placement_from_by_dist_count(4,
                                                                                              shape_top_bar,
                                                                                              f_top_bar_point_f,
                                                                                              f_top_bar_point_t,
                                                                                              0,
                                                                                              top_bar_distance,
                                                                                              top_bar_cnt))

        #添加后侧顶筋
        reinforcement.append(LinearBarBuilder.create_linear_bar_placement_from_by_dist_count(5,
                                                                                              shape_top_bar,
                                                                                              b_top_bar_point_f,
                                                                                              b_top_bar_point_t,
                                                                                              0,
                                                                                              top_bar_distance,
                                                                                              top_bar_cnt))

        return reinforcement

    def shape_stirrup(self,build_ele):
        '''
        箍筋建模函数
        Args:
            build_ele: build_ele.get_parameter_dict()
            build_ele: .pyp文件内的 Name标签的参数字典
        '''
        #参数
        concrete_grade = build_ele['StirrupConcreteGrade']              #混凝土等级
        steel_grade = build_ele['StirrupSteelGrade']                    #钢筋等级
        diameter = build_ele['StirrupDiameter']                         #钢筋直径
        concrete_cover = build_ele['StirrupConcreteCover']              #保护层厚度
        stirrup_type = build_ele['StirrupType']                         #箍筋类型--未使用
        bending_roller = build_ele['StirrupBendingRoller']              #箍筋弯曲长度
        bending_shape_type = AllplanReinf.BendingShapeType.Stirrup

        model_angles = RotationAngles(0,-90,0)

        #保护层混凝土属性
        concrete_props = ConcreteCoverProperties.all(concrete_cover)
        #箍筋属性
        shape_props = ReinforcementShapeProperties.rebar(   diameter,
                                                            bending_roller,
                                                            steel_grade,
                                                            concrete_grade,
                                                            bending_shape_type)

        #建立箍筋模型
        shape = GeneralShapeBuilder.create_stirrup(self.height,
                                                   self.width,
                                                   model_angles,
                                                   shape_props,
                                                   concrete_props)
        return shape

    def shape_bar(self,build_ele,bar_diameter,extend_length=0):
        '''
        纵筋建模函数
        
        Args:
            build_ele: build_ele.get_parameter_dict()
            build_ele: .pyp文件内的 Name标签的参数字典
        '''
        bending_roller = 0
        steel_grade = build_ele['BarSteelGrade']
        concrete_grade = build_ele['BarConcreteGrade']
        bending_shape_type = AllplanReinf.BendingShapeType.Freeform
        concrete_cover = 0

        concrete_props = ConcreteCoverProperties(top=0,right=0,left=0,bottom=concrete_cover)

        shape_props = ReinforcementShapeProperties.rebar(bar_diameter,
                                                         bending_roller,
                                                         steel_grade,
                                                         concrete_grade,
                                                         bending_shape_type)

        shape_builder = AllplanReinf.ReinforcementShapeBuilder()


        shape_builder.AddPoints([(AllplanGeo.Point3D(0 - extend_length,
                                                     0,
                                                     0),0),
                                 (AllplanGeo.Point3D(self.length + extend_length,
                                                     0,
                                                     0),0)])

        shape = shape_builder.CreateShape(shape_props)


        return shape 

    def create_handle(self):
        '''
        Create handle
        创建可拉动游标句柄

        '''
        self.handle_list.append(
            HandleProperties("Height",
                                AllplanGeo.Point3D(0, 0, self.height),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Height", HandleDirection.z_dir)],
                                HandleDirection.z_dir,
                                True))

        self.handle_list.append(
            HandleProperties("Width",
                                AllplanGeo.Point3D(0, self.width, 0),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Width", HandleDirection.y_dir)],
                                HandleDirection.y_dir,
                                True))

        self.handle_list.append(
            HandleProperties("Length",
                                AllplanGeo.Point3D(self.length, 0, 0),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Length", HandleDirection.x_dir)],
                                HandleDirection.x_dir,
                                True))