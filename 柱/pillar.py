# -*- coding: utf-8 -*-
# @Time    : 2017/08/11
# @Author  : kingsley kwong
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : pillar.py
# @Software: 暗梁源码文件
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

print ('Loading template.py ' )

LANG_CONF = {'bend':['bend','弯'],'straight':['straight','直']}
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

    element = Pillar(doc)
 
    return element.create(build_ele)




class Pillar(object):
    '''
    Definition of class Pillar
    构件类
    '''
    def __init__(self, doc):
        '''
        Initialisation of class Pillar
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


    # def data_update(self):
    #     for key,value in self.__dict__.items():
    #         __class__.build_element.get_parameter_dict()[key] = value

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

        self.data_read(build_ele.get_parameter_dict())

        self.longitudinal_distance = (self.Length - 2*self.A_SideCover - self.Diameter) / (self.Pairs - 1)
        views_list = []

        polyhedron = self.create_geometry()

        reinforcement = self.create_reinforcement()
        
        

        #self.texturedef = AllplanBasisElements.TextureDefinition(self.Surface)

        views_list += polyhedron
        views = [View2D3D(views_list)]

        
        pythonpart = PythonPart ("Pillar",                                             #ID
                                 parameter_list = build_ele.get_params_list(),          #.pyp 参数列表
                                 hash_value     = build_ele.get_hash(),                 #.pyp 哈希值
                                 python_file    = build_ele.pyp_file_name,              #.pyp 文件名
                                 views          = views,                                #图形视图
                                 reinforcement  = reinforcement,                        #增强构建
                                 common_props   = self.com_prop)                        #格式参数



        self.create_handle(build_ele)

        self.model_ele_list = pythonpart.create()

        return (self.model_ele_list, self.handle_list)

    def create_handle(self,build_ele):
        '''
        Create handle
        创建可拉动游标句柄

        '''
        if self.Shape in LANG_CONF['straight']:
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
        elif self.Shape in LANG_CONF['bend']:
            self.handle_list.append(
                HandleProperties("Length",
                                    AllplanGeo.Point3D(self.Length, 0, 0),
                                    AllplanGeo.Point3D(0, 0, 0),
                                    [("Length", HandleDirection.x_dir)],
                                    HandleDirection.x_dir,
                                    True))

            self.handle_list.append(
                HandleProperties("Width",
                                    AllplanGeo.Point3D(0, self.Width, 0),
                                    AllplanGeo.Point3D(0, 0, 0),
                                    [("Width", HandleDirection.y_dir)],
                                    HandleDirection.y_dir,
                                    True))

            self.handle_list.append(
                HandleProperties("B_VertLength",
                                    AllplanGeo.Point3D(self.A_FrontCover, self.B_VertLength + self.A_FrontCover, self.A_Length + self.B_HoriLength),
                                    AllplanGeo.Point3D(0, 0, 0),
                                    [("B_VertLength", HandleDirection.y_dir)],
                                    HandleDirection.y_dir,
                                    True))

            self.handle_list.append(
                HandleProperties("A_FrontCover",
                                    AllplanGeo.Point3D(self.A_FrontCover, self.Width - self.A_FrontCover, self.A_Length ),
                                    AllplanGeo.Point3D(0,self.Width,0),
                                    [("A_FrontCover", HandleDirection.y_dir)],
                                    HandleDirection.y_dir,
                                    True))

            if self.A_Length + self.B_HoriLength + self.C_Length <= self.Height:
                #print('a')
                self.handle_list.append(
                    HandleProperties("Height",
                                        AllplanGeo.Point3D(0, 0, self.Height),
                                        AllplanGeo.Point3D(0, 0, 0),
                                        [("Height", HandleDirection.z_dir)],
                                        HandleDirection.z_dir,
                                        True))

                self.handle_list.append(
                    HandleProperties("A_Length",
                                        AllplanGeo.Point3D(self.A_SideCover, self.A_FrontCover, self.A_Length),
                                        AllplanGeo.Point3D(0, 0, 0),
                                        [("A_Length", HandleDirection.z_dir)],
                                        HandleDirection.z_dir,
                                        True))

                self.handle_list.append(
                    HandleProperties("B_HoriLength",
                                        AllplanGeo.Point3D(self.A_FrontCover, self.Width - self.A_FrontCover - self.B_VertLength, self.A_Length + self.B_HoriLength),
                                        AllplanGeo.Point3D(0,0,self.A_Length),
                                        [("B_HoriLength", HandleDirection.z_dir)],
                                        HandleDirection.z_dir,
                                        True))

                self.handle_list.append(
                    HandleProperties("C_Length",
                                        AllplanGeo.Point3D(self.A_FrontCover, self.B_VertLength + self.A_FrontCover, self.A_Length + self.B_HoriLength + self.C_Length),
                                        AllplanGeo.Point3D(0,0,self.A_Length + self.B_HoriLength),
                                        [("C_Length", HandleDirection.z_dir)],
                                        HandleDirection.z_dir,
                                        True))
            else:
                #print('b')
                build_ele.Height.value = self.A_Length + self.B_HoriLength + self.C_Length
                self.handle_list.append(
                    HandleProperties("Height",
                                        AllplanGeo.Point3D(0, 0, build_ele.Height.value),
                                        AllplanGeo.Point3D(0, 0, 0),
                                        [("Height", HandleDirection.z_dir)],
                                        HandleDirection.z_dir,
                                        True))
                self.handle_list.append(
                    HandleProperties("A_Length",
                                        AllplanGeo.Point3D(self.A_SideCover, self.A_FrontCover, self.A_Length),
                                        AllplanGeo.Point3D(0, 0, 0),
                                        [("A_Length", HandleDirection.z_dir),("Height", HandleDirection.z_dir)],
                                        HandleDirection.z_dir,
                                        True))

                self.handle_list.append(
                    HandleProperties("B_HoriLength",
                                        AllplanGeo.Point3D(self.A_FrontCover, self.Width - self.A_FrontCover - self.B_VertLength, self.A_Length + self.B_HoriLength),
                                        AllplanGeo.Point3D(0,0,self.A_Length),
                                        [("B_HoriLength", HandleDirection.z_dir),("Height", HandleDirection.z_dir)],
                                        HandleDirection.z_dir,
                                        True))

                self.handle_list.append(
                    HandleProperties("C_Length",
                                        AllplanGeo.Point3D(self.A_FrontCover, self.B_VertLength + self.A_FrontCover, self.A_Length + self.B_HoriLength + self.C_Length),
                                        AllplanGeo.Point3D(0,0,self.A_Length + self.B_HoriLength),
                                        [("C_Length", HandleDirection.z_dir),("Height", HandleDirection.z_dir)],
                                        HandleDirection.z_dir,
                                        True))
            



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

        
        return [AllplanBasisElements.ModelElement3D(self.com_prop, rectangle)]


    def create_reinforcement(self):
        '''
        Create the reinforcement element
        构造并添加增强构建函数

        Args:
            build_ele: the building element
            .pyp文件输入参数，buile_ele代表整个.pyp文件信息
        '''
        reinforcement = []
        if self.VisualSteel:
            reinforcement += self.create_longitudinal_steel()

        if self.VisualStir1:
            reinforcement += self.create_stirrup_steel()

        if self.VisualStir2:
            reinforcement += self.create_stirrup2_steel()

        return reinforcement


    def create_longitudinal_steel(self):

        shape = self.shape_longitudinal_steel()
        m_shape = self.shape_longitudinal_steel(True)

        long_steels = []
        arg_list = []

        l_args = {  'position':40,
                    'shape':shape,
                    'from_point':AllplanGeo.Point3D(0,self.A_FrontCover,0),
                    'direction_point':AllplanGeo.Point3D(self.Length,self.A_FrontCover ,0),
                    'concrete_cover':self.A_SideCover,
                    'bar_distance':self.longitudinal_distance,
                    'bar_count':self.Pairs}
        
        m_args = {  'position':40,
                    'shape':m_shape,
                    'from_point':AllplanGeo.Point3D(0,self.Width - self.A_FrontCover,0),
                    'direction_point':AllplanGeo.Point3D(self.Length,self.Width - self.A_FrontCover ,0),
                    'concrete_cover':self.A_SideCover,
                    'bar_distance':self.longitudinal_distance,
                    'bar_count':self.Pairs}

        long_steels.append(LinearBarBuilder.create_linear_bar_placement_from_by_dist_count(**l_args))
        long_steels.append(LinearBarBuilder.create_linear_bar_placement_from_by_dist_count(**m_args))
        return long_steels

    def shape_longitudinal_steel(self,mirror=False):
        point_list = []
        point_list.append((AllplanGeo.Point3D(self.BottomShrink,0,0),0))

        if self.Shape in LANG_CONF['bend']:
            shape_type = AllplanReinf.BendingShapeType.LongitudinalBarDoubleBentOff

            if mirror:
                point_list.append((AllplanGeo.Point3D(self.A_Length,0,0),0))
                point_list.append((AllplanGeo.Point3D(self.A_Length + self.B_HoriLength,-self.B_VertLength,0),0))
                point_list.append((AllplanGeo.Point3D(self.A_Length + self.B_HoriLength+self.C_Length,-self.B_VertLength,0),0))
                point_list.append((AllplanGeo.Point3D(self.A_Length + self.B_HoriLength+self.C_Length+self.UpperStretch,-self.B_VertLength,0),0))
            else:
                point_list.append((AllplanGeo.Point3D(self.A_Length,0,0),0))
                point_list.append((AllplanGeo.Point3D(self.A_Length + self.B_HoriLength,self.B_VertLength,0),0))
                point_list.append((AllplanGeo.Point3D(self.A_Length + self.B_HoriLength+self.C_Length,self.B_VertLength,0),0))    
                point_list.append((AllplanGeo.Point3D(self.A_Length + self.B_HoriLength+self.C_Length+self.UpperStretch,self.B_VertLength,0),0))    

        elif self.Shape in LANG_CONF['straight']:
            shape_type = AllplanReinf.BendingShapeType.LongitudinalBar
            point_list.append((AllplanGeo.Point3D(self.Height + self.UpperStretch,0,0),0))

        shape_builder = AllplanReinf.ReinforcementShapeBuilder()
        shape_builder.AddPoints(point_list)

        rebar_args = {  'diameter':self.Diameter,
                        'bending_roller':0,
                        'steel_grade':self.SteelGrade,
                        'concrete_grade':self.ConcreteGrade,
                        'bending_shape_type':shape_type}

        rein_prop = ReinforcementShapeProperties.rebar(**rebar_args)
        shape = shape_builder.CreateShape(rein_prop)

        angle = RotationAngles(0,-90,0)
        if shape.IsValid():
            shape.Rotate(angle)
            return shape

    def create_stirrup_steel(self):

        stirrup_list = []
        low_arg_dict = {}
        low_bend_dict = {}
        high_arg_dict = {}
        high_bend_dict = {}

        size_dict = {   'length':self.Length - 2*self.ConcreteCover ,
                        'width':self.Width, 
                        'angle':RotationAngles(0,0,0)}

        bend_size_dict = {  'length':self.Length - 2*self.ConcreteCover,
                            'width':self.Width - 2*self.B_VertLength,
                            'angle':RotationAngles(0,0,0)}

        cover_dict = {  'top':self.ConcreteCover,
                        'bottom':self.ConcreteCover,
                        'left':0,
                        'right':0}


        low_stirrup_props_dict = {  'steel_grade':self.StirrupGrade1,
                                    'diameter':self.LowDensDia,
                                    'bending_roller':math.pi * self.LDBendDia / 4,
                                    'stirrup_type':AllplanReinf.StirrupType.Normal}

        high_stirrup_props_dict = { 'steel_grade':self.StirrupGrade1,
                                    'diameter':self.HighDensDia,
                                    'bending_roller':math.pi * self.HDBendDia / 4,
                                    'stirrup_type':AllplanReinf.StirrupType.Normal}

        low_arg_dict.update(size_dict)                                    
        low_arg_dict.update(cover_dict)
        low_arg_dict.update(low_stirrup_props_dict)

        low_bend_dict.update(bend_size_dict)                                    
        low_bend_dict.update(cover_dict)
        low_bend_dict.update(low_stirrup_props_dict)

        high_arg_dict.update(size_dict)
        high_arg_dict.update(cover_dict)
        high_arg_dict.update(high_stirrup_props_dict)

        high_bend_dict.update(bend_size_dict)
        high_bend_dict.update(cover_dict)
        high_bend_dict.update(high_stirrup_props_dict)

        low_stirrup_shape = self.shape_stirrup_steel(open_stirrup=False,**low_arg_dict)
        high_stirrup_shape = self.shape_stirrup_steel(open_stirrup=False,**high_arg_dict)
        low_bend_stirrup_shape = self.shape_stirrup_steel(open_stirrup=False,**low_bend_dict)
        high_bend_stirrup_shape = self.shape_stirrup_steel(open_stirrup=False,**high_bend_dict)


        #-------------------------------------------------------#

        low_general = {   'position':41,
                        'concrete_cover_left':self.LDPrimPitch,
                        'concrete_cover_right':self.LDPrimPitch,
                        'bar_distance':self.LDPitch,
                        'start_end_rule':4}

        high_general = {   'position':42,
                            'concrete_cover_left':self.HDPrimPitch,
                            'concrete_cover_right':self.HDPrimPitch,
                            'bar_distance':self.HDPitch,
                            'start_end_rule':4}

        if self.Shape in LANG_CONF['straight']:
            lows = {    'shape':low_stirrup_shape,
                        'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.DensArea),
                        'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.Height)}

            lows.update(low_general)
            stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**lows))
            if self.DensArea != 0:
                highs = {'shape':high_stirrup_shape,
                        'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,0),
                        'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.DensArea)}
                highs.update(high_general)
                stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**highs))
        else:
            if self.DensArea > self.A_Length + self.B_HoriLength:
                high = {'shape':high_stirrup_shape,
                        'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,0),
                        'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.A_Length+self.B_HoriLength)}
                high_bend = {   'shape':high_bend_stirrup_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.A_Length+self.B_HoriLength),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.DensArea)}
                low_bend = {'shape':low_bend_stirrup_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.DensArea),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.Height)}
                high.update(high_general)
                high_bend.update(high_general)      
                low_bend.update(low_general)
                if self.DensArea != 0:
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_bend))
                stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend))

            else:
                high = {'shape':high_stirrup_shape,
                        'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,0),
                        'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.DensArea)}
                low = {'shape':low_stirrup_shape,
                        'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.DensArea),
                        'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.A_Length+self.B_HoriLength)}
                low_bend = {'shape':low_bend_stirrup_shape,
                        'from_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.A_Length+self.B_HoriLength),
                        'to_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.Height)}

                high.update(high_general)
                low.update(low_general)      
                low_bend.update(low_general)
                if self.DensArea != 0:
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high))
                stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low))
                stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend))

        return stirrup_list

    def create_stirrup2_steel(self):

        stirrup2_general = {'top':0,
                            'bottom':0,
                            'left':self.ConcreteCover,
                            'right':self.ConcreteCover,
                            'diameter':self.StirrupDia2,
                            'bending_roller':0,
                            'steel_grade':self.StirrupGrade2,
                            'start_hook':self.HookLength,
                            'end_hook':self.HookLength,
                            'start_hook_angle':self.HookAngle,
                            'end_hook_angle':self.HookAngle,
                            'hook_type':-1}

        stirrup2 = {'length':self.Width,
                    'width':4*self.StirrupDia2}

        stirrup2_bend = {'length':self.Width - 2*self.B_VertLength,
                        'width':4*self.StirrupDia2}
        stirrup2.update(stirrup2_general)
        stirrup2_bend.update(stirrup2_general)

        stir2_shape = self.shape_stirrup_steel(open_stirrup=True,angle=RotationAngles(0,180,-90),**stirrup2)
        stir2_bend_shape = self.shape_stirrup_steel(open_stirrup=True,angle=RotationAngles(0,180,-90),**stirrup2_bend)
        

        low_general = {   'position':43,
                            'concrete_cover_left':self.LDPrimPitch,
                            'concrete_cover_right':self.LDPrimPitch,
                            'bar_distance':self.LDPitch,
                            'start_end_rule':4}

        high_general = {  'position':43,
                            'concrete_cover_left':self.HDPrimPitch,
                            'concrete_cover_right':self.HDPrimPitch,
                            'bar_distance':self.HDPitch,
                            'start_end_rule':4}
                      
                        
        stirrup_list = []
        if self.Shape in LANG_CONF['straight']:
            if self.Position1:
                low_general.update({  'shape':stir2_shape,
                                        'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.DensArea+self.LowDensDia),
                                        'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.Height+self.LowDensDia)})
                high_general.update({ 'shape':stir2_shape,
                                        'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.HighDensDia),
                                        'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.DensArea+self.HighDensDia)})
                if self.DensArea != 0:
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_general))
                stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_general))

            if self.Position2:
                low_general.update({  'shape':stir2_shape,
                                        'from_point':AllplanGeo.Point3D(self.ConcreteCover + self.longitudinal_distance,0,self.DensArea+self.LowDensDia),
                                        'to_point':AllplanGeo.Point3D(self.ConcreteCover + self.longitudinal_distance,0,self.Height+self.LowDensDia)})
                high_general.update({ 'shape':stir2_shape,
                                        'from_point':AllplanGeo.Point3D(self.ConcreteCover + self.longitudinal_distance,0,self.HighDensDia),
                                        'to_point':AllplanGeo.Point3D(self.ConcreteCover + self.longitudinal_distance,0,self.DensArea+self.HighDensDia)})
                if self.DensArea != 0:
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_general))
                stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_general))

            if self.Position3:
                low_general.update({  'shape':stir2_shape,
                                        'from_point':AllplanGeo.Point3D(self.ConcreteCover + 2*self.longitudinal_distance,0,self.DensArea+self.LowDensDia),
                                        'to_point':AllplanGeo.Point3D(self.ConcreteCover + 2*self.longitudinal_distance,0,self.Height+self.LowDensDia)})
                high_general.update({ 'shape':stir2_shape,
                                        'from_point':AllplanGeo.Point3D(self.ConcreteCover + 2*self.longitudinal_distance,0,self.HighDensDia),
                                        'to_point':AllplanGeo.Point3D(self.ConcreteCover + 2*self.longitudinal_distance,0,self.DensArea+self.HighDensDia)})
                if self.DensArea != 0:
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_general))
                stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_general))

            if self.Position4:
                low_general.update({  'shape':stir2_shape,
                                        'from_point':AllplanGeo.Point3D(self.ConcreteCover + 3*self.longitudinal_distance,0,self.DensArea+self.LowDensDia),
                                        'to_point':AllplanGeo.Point3D(self.ConcreteCover + 3*self.longitudinal_distance,0,self.Height+self.LowDensDia)})
                high_general.update({ 'shape':stir2_shape,
                                        'from_point':AllplanGeo.Point3D(self.ConcreteCover + 3*self.longitudinal_distance,0,self.HighDensDia),
                                        'to_point':AllplanGeo.Point3D(self.ConcreteCover + 3*self.longitudinal_distance,0,self.DensArea+self.HighDensDia)})
                if self.DensArea != 0:
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_general))
                stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_general))

        else:
            if self.Position1:
                if self.DensArea > self.A_Length + self.B_HoriLength:
                    high_p1 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.HighDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.A_Length+self.B_HoriLength+self.HighDensDia)}
                    high_bend_p1 = {   'shape':stir2_bend_shape,
                                    'from_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.A_Length+self.B_HoriLength+self.HighDensDia),
                                    'to_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.DensArea+self.HighDensDia)}
                    low_bend_p1 = {'shape':stir2_bend_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.DensArea+self.LowDensDia),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.Height+self.LowDensDia)}

                    high_p1.update(high_general)
                    high_bend_p1.update(high_general)      
                    low_bend_p1.update(low_general)
                    if self.DensArea != 0:
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_p1))
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_bend_p1))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend_p1))

                else:
                    high_p1 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.HighDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.DensArea+self.HighDensDia)}
                    low_p1 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.DensArea+self.LowDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover,0,self.A_Length+self.B_HoriLength+self.LowDensDia)}
                    low_bend_p1 = {'shape':stir2_bend_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.A_Length+self.B_HoriLength+self.LowDensDia),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover,self.B_VertLength,self.Height+self.LowDensDia)}

                    high_p1.update(high_general)
                    low_p1.update(low_general)      
                    low_bend_p1.update(low_general)
                    if self.DensArea != 0:
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_p1))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_p1))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend_p1))

            if self.Position2:
                if self.DensArea > self.A_Length + self.B_HoriLength:
                    high_p2 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,0,self.HighDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,0,self.A_Length+self.B_HoriLength+self.HighDensDia)}
                    high_bend_p2 = {   'shape':stir2_bend_shape,
                                    'from_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,self.B_VertLength,self.A_Length+self.B_HoriLength+self.HighDensDia),
                                    'to_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,self.B_VertLength,self.DensArea+self.HighDensDia)}
                    low_bend_p2 = {'shape':stir2_bend_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,self.B_VertLength,self.DensArea+self.LowDensDia),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,self.B_VertLength,self.Height+self.LowDensDia)}

                    high_p2.update(high_general)
                    high_bend_p2.update(high_general)      
                    low_bend_p2.update(low_general)
                    if self.DensArea != 0:
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_p2))
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_bend_p2))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend_p2))

                else:
                    high_p2 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,0,self.HighDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,0,self.DensArea+self.HighDensDia)}
                    low_p2 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,0,self.DensArea+self.LowDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,0,self.A_Length+self.B_HoriLength+self.LowDensDia)}
                    low_bend_p2 = {'shape':stir2_bend_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,self.B_VertLength,self.A_Length+self.B_HoriLength+self.LowDensDia),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover+self.longitudinal_distance,self.B_VertLength,self.Height+self.LowDensDia)}

                    high_p2.update(high_general)
                    low_p2.update(low_general)      
                    low_bend_p2.update(low_general)
                    if self.DensArea != 0:
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_p2))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_p2))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend_p2))

            if self.Position3:
                if self.DensArea > self.A_Length + self.B_HoriLength:
                    high_p3 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,0,self.HighDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,0,self.A_Length+self.B_HoriLength+self.HighDensDia)}
                    high_bend_p3 = {   'shape':stir2_bend_shape,
                                    'from_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,self.B_VertLength,self.A_Length+self.B_HoriLength+self.HighDensDia),
                                    'to_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,self.B_VertLength,self.DensArea+self.HighDensDia)}
                    low_bend_p3 = {'shape':stir2_bend_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,self.B_VertLength,self.DensArea+self.LowDensDia),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,self.B_VertLength,self.Height+self.LowDensDia)}

                    high_p3.update(high_general)
                    high_bend_p3.update(high_general)      
                    low_bend_p3.update(low_general)
                    if self.DensArea != 0:
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_p3))
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_bend_p3))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend_p3))

                else:
                    high_p3 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,0,self.HighDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,0,self.DensArea+self.HighDensDia)}
                    low_p3 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,0,self.DensArea+self.LowDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,0,self.A_Length+self.B_HoriLength+self.LowDensDia)}
                    low_bend_p3 = {'shape':stir2_bend_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,self.B_VertLength,self.A_Length+self.B_HoriLength+self.LowDensDia),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover+2*self.longitudinal_distance,self.B_VertLength,self.Height+self.LowDensDia)}

                    high_p3.update(high_general)
                    low_p3.update(low_general)      
                    low_bend_p3.update(low_general)
                    if self.DensArea != 0:
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_p3))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_p3))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend_p3))

            if self.Position4:
                if self.DensArea > self.A_Length + self.B_HoriLength:
                    high_p4 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,0,self.HighDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,0,self.A_Length+self.B_HoriLength+self.HighDensDia)}
                    high_bend_p4 = {   'shape':stir2_bend_shape,
                                    'from_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,self.B_VertLength,self.A_Length+self.B_HoriLength+self.HighDensDia),
                                    'to_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,self.B_VertLength,self.DensArea+self.HighDensDia)}
                    low_bend_p4 = {'shape':stir2_bend_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,self.B_VertLength,self.DensArea+self.LowDensDia),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,self.B_VertLength,self.Height+self.LowDensDia)}

                    high_p4.update(high_general)
                    high_bend_p4.update(high_general)      
                    low_bend_p4.update(low_general)
                    if self.DensArea != 0:
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_p4))
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_bend_p4))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend_p4))

                else:
                    high_p4 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,0,self.HighDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,0,self.DensArea+self.HighDensDia)}
                    low_p4 = {'shape':stir2_shape,
                            'from_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,0,self.DensArea+self.LowDensDia),
                            'to_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,0,self.A_Length+self.B_HoriLength+self.LowDensDia)}
                    low_bend_p4 = {'shape':stir2_bend_shape,
                                'from_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,self.B_VertLength,self.A_Length+self.B_HoriLength+self.LowDensDia),
                                'to_point':AllplanGeo.Point3D(self.ConcreteCover+3*self.longitudinal_distance,self.B_VertLength,self.Height+self.LowDensDia)}

                    high_p4.update(high_general)
                    low_p4.update(low_general)      
                    low_bend_p4.update(low_general)
                    if self.DensArea != 0:
                        stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**high_p4))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_p4))
                    stirrup_list.append(LinearBarBuilder.create_linear_bar_placement_from_to_by_dist(**low_bend_p4))

        return stirrup_list

    def shape_stirrup_steel(self,open_stirrup,length,width,angle,top,bottom,left,right,diameter,bending_roller,steel_grade,**kwargs):

        concrete_args = {'top':top,
                        'bottom':bottom,
                        'left':left,
                        'right':right}

        concrete_props = ConcreteCoverProperties(**concrete_args)
        stirrup_args = {'diameter':diameter,
                        'bending_roller':bending_roller,
                        'steel_grade':steel_grade,
                        'concrete_grade':self.ConcreteGrade}
        if open_stirrup:
            stirrup_args['bending_shape_type']=AllplanReinf.BendingShapeType.OpenStirrup
        else:
            stirrup_args['bending_shape_type']=AllplanReinf.BendingShapeType.Stirrup


        stirrup_props = ReinforcementShapeProperties.rebar(**stirrup_args)

        #-------------------------------------#



        args = {'length':length,
                'width':width,
                'shape_props':stirrup_props,
                'concrete_cover_props':concrete_props}

        if open_stirrup:                
            args.update({   'model_angles':angle,
                            'start_hook':kwargs['start_hook'],
                            'end_hook':kwargs['end_hook'],
                            'start_hook_angle':kwargs['start_hook_angle'],
                            'end_hook_angle':kwargs['end_hook_angle'],
                            'hook_type':kwargs['hook_type']})
            stirrup_shape = GeneralShapeBuilder.create_open_stirrup(**args)
        else:
            args.update({   'model_angles':angle,
                            'stirrup_type':kwargs['stirrup_type']})
            stirrup_shape = GeneralShapeBuilder.create_stirrup(**args)

        if stirrup_shape.IsValid():
            return stirrup_shape


