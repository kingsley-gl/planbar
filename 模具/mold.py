# -*- coding: utf-8 -*-
# @Time    : 2017/08/11
# @Author  : kingsley kuang
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : mold.py
# @Software: 模具源码文件
# @Function: 

"""
Example Script for an liang
"""


import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Utility as AllplanUtility          # allplan util library
import NemAll_Python_AllplanSettings as AllplanSetting

import StdReinfShapeBuilder.GeneralReinfShapeBuilder as GeneralShapeBuilder
import StdReinfShapeBuilder.LinearBarPlacementBuilder as LinearBarBuilder


from StdReinfShapeBuilder.ConcreteCoverProperties import ConcreteCoverProperties
from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties
from StdReinfShapeBuilder.RotationAngles import RotationAngles

from HandleDirection import HandleDirection
from HandleProperties import HandleProperties
from PythonPart import View2D3D, PythonPart   
import math        

print ('Loading test.py ' )


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
    

    element = Mold(doc)
 
    return element.create(build_ele)




class Mold(object):
    '''
    Definition of class Mold
    梁模具
    '''
    def __init__(self, doc):
        '''
        Initialisation of class Beam
        初始化函数
        Args:
            doc: Input document
            文档输入
        '''
        self.model_ele_list = []
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
            .pyp文件输入参数，build_ele代表整个.pyp文件信息

        Returns:
            tuple with created elements and handles.
            被创造元素以及其句柄，由元祖打包返回
        '''



        self.surf = AllplanBasisElements.TextureDefinition(build_ele.Surface.value)
        self.long_surf = AllplanBasisElements.TextureDefinition(build_ele.LongSurface.value)
        self.short_surf = AllplanBasisElements.TextureDefinition(build_ele.ShortSurface.value)

        polyhedron = self.create_geometry(build_ele.get_parameter_dict())

        f_side_stiff =  self.create_side_stiff(build_ele.get_parameter_dict(),-build_ele.StiffenerThick.value-build_ele.BottomStiffenerWidth.value)
        s_side_stiff =  self.create_side_stiff(build_ele.get_parameter_dict(),build_ele.StiffenerThick.value+build_ele.Width.value)

        f_top_stiff = self.create_top_stiff(build_ele.get_parameter_dict(),
                                            -build_ele.StiffenerThick.value-build_ele.BottomStiffenerWidth.value,
                                            build_ele.Thick.value-build_ele.StiffenerThick.value)

        f_bottom_stiff = self.create_top_stiff(build_ele.get_parameter_dict(),
                                                -build_ele.StiffenerThick.value-build_ele.BottomStiffenerWidth.value)

        s_top_stiff = self.create_top_stiff(build_ele.get_parameter_dict(),
                                            build_ele.StiffenerThick.value+build_ele.Width.value,
                                            build_ele.Thick.value-build_ele.StiffenerThick.value)

        s_bottom_stiff = self.create_top_stiff(build_ele.get_parameter_dict(),
                                                build_ele.StiffenerThick.value+build_ele.Width.value)

        fst_long_stiff = self.create_long_stiff(build_ele.get_parameter_dict(),
                                                -2*build_ele.StiffenerThick.value-build_ele.BottomStiffenerWidth.value)

        snd_long_stiff = self.create_long_stiff(build_ele.get_parameter_dict(),
                                                -build_ele.StiffenerThick.value)

        trd_long_stiff = self.create_long_stiff(build_ele.get_parameter_dict(),
                                                build_ele.Width.value)

        fth_long_stiff = self.create_long_stiff(build_ele.get_parameter_dict(),
                                                build_ele.StiffenerThick.value+build_ele.Width.value+build_ele.BottomStiffenerWidth.value)

        vertical_short_stiff_1 = self.create_vertical_short_stiff(build_ele.get_parameter_dict(),
                                                                  -build_ele.LongEdgeMainExtendLength.value/2)

        vertical_short_stiff_2 = self.create_vertical_short_stiff(build_ele.get_parameter_dict(),
                                                                  -build_ele.LongEdgeMainExtendLength.value/2,
                                                                  build_ele.Width.value-build_ele.StiffenerThick.value)

        vertical_short_stiff_3 = self.create_vertical_short_stiff(build_ele.get_parameter_dict(),
                                                                  build_ele.Length.value+build_ele.StiffenerThick.value)

        vertical_short_stiff_4 = self.create_vertical_short_stiff(build_ele.get_parameter_dict(),
                                                                  build_ele.Length.value+build_ele.StiffenerThick.value,
                                                                  build_ele.Width.value-build_ele.StiffenerThick.value)

        horizon_short_stiff_1 = self.create_horizon_short_stiff(build_ele.get_parameter_dict(),
                                                                -build_ele.LongEdgeMainExtendLength.value/2,
                                                                build_ele.StiffenerThick.value)

        horizon_short_stiff_2 = self.create_horizon_short_stiff(build_ele.get_parameter_dict(),
                                                                build_ele.Length.value+build_ele.StiffenerThick.value,
                                                                build_ele.StiffenerThick.value)

        horizon_short_stiff_3 = self.create_horizon_short_stiff(build_ele.get_parameter_dict(),
                                                                -build_ele.LongEdgeMainExtendLength.value/2,
                                                                build_ele.StiffenerThick.value,
                                                                build_ele.Thick.value-build_ele.StiffenerThick.value)

        horizon_short_stiff_4 = self.create_horizon_short_stiff(build_ele.get_parameter_dict(),
                                                                build_ele.Length.value+build_ele.StiffenerThick.value,
                                                                build_ele.StiffenerThick.value,
                                                                build_ele.Thick.value-build_ele.StiffenerThick.value)

        short_stiff_1 = self.create_short_stiff(build_ele.get_parameter_dict(),
                                                -build_ele.StiffenerThick.value)

        short_stiff_2 = self.create_short_stiff(build_ele.get_parameter_dict(),
                                                build_ele.Length.value)


        reinforcement = self.create_reinforcement(build_ele.get_parameter_dict())
              
        views_list = []

        views_list += polyhedron
        views_list += f_side_stiff
        views_list += s_side_stiff
        views_list += f_top_stiff
        views_list += s_top_stiff
        views_list += f_bottom_stiff
        views_list += s_bottom_stiff
        views_list += fst_long_stiff
        views_list += snd_long_stiff
        views_list += trd_long_stiff
        views_list += fth_long_stiff
        views_list += vertical_short_stiff_1
        views_list += vertical_short_stiff_2
        views_list += vertical_short_stiff_3
        views_list += vertical_short_stiff_4
        views_list += horizon_short_stiff_1
        views_list += horizon_short_stiff_2
        views_list += horizon_short_stiff_3
        views_list += horizon_short_stiff_4
        views_list += short_stiff_1
        views_list += short_stiff_2

        views = [View2D3D(views_list)]
        
        pythonpart = PythonPart ("Mold",                                                #ID
                                 parameter_list = build_ele.get_params_list(),          #.pyp 参数列表
                                 hash_value     = build_ele.get_hash(),                 #.pyp 哈希值
                                 python_file    = build_ele.pyp_file_name,              #.pyp 文件名
                                 views          = views,                                #图形视图
                                 reinforcement  = reinforcement,                        #增强构建
                                 common_props   = self.com_prop)                        #格式参数


        self.create_handle(build_ele.get_parameter_dict())

        self.model_ele_list = pythonpart.create()

        return (self.model_ele_list, self.handle_list)

    def create_geometry(self, build_ele):
        '''
        Create the element geometries
        构建元素几何图形函数

        Args:
            build_ele: the building element
            .pyp文件输入参数，build_ele代表整个.pyp文件信息
        '''

        length = build_ele['Length']    #长
        width = build_ele['Width']      #宽
        thick = build_ele['Thick']      #厚

        #point
        from_point = AllplanGeo.Point3D(0,0,0)                  
        to_point = AllplanGeo.Point3D(length,width,thick)      

        rectangle = AllplanGeo.Polyhedron3D.CreateCuboid(from_point,to_point) #矩形
        
        return [AllplanBasisElements.ModelElement3D(self.com_prop,self.surf, rectangle)]


    def create_reinforcement(self,build_ele):
        '''
        Create the reinforcement element
        构造并添加增强构建函数

        Args:
            build_ele: the building element
            .pyp文件输入参数，buile_ele代表整个.pyp文件信息
        '''
        reinforcement = []
        return reinforcement

    def create_handle(self,build_ele):
        '''
        Create handle
        创建可拉动游标句柄

        Args:
            build_ele: the building element dict
            .pyp文件的变量参数字典
        Return:
            
        '''
        length = build_ele['Length']    #长
        width = build_ele['Width']      #宽
        thick = build_ele['Thick']      #厚

        self.handle_list.append(
            HandleProperties("Thick",
                                AllplanGeo.Point3D(0, 0, thick),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Thick", HandleDirection.z_dir)],
                                HandleDirection.z_dir,
                                True))

        self.handle_list.append(
            HandleProperties("Width",
                                AllplanGeo.Point3D(0, width, 0),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Width", HandleDirection.y_dir)],
                                HandleDirection.y_dir,
                                True))

        self.handle_list.append(
            HandleProperties("Length",
                                AllplanGeo.Point3D(length, 0, 0),
                                AllplanGeo.Point3D(0, 0, 0),
                                [("Length", HandleDirection.x_dir)],
                                HandleDirection.x_dir,
                                True))



    def create_side_stiff(self,build_ele,y_position=0):
        '''
        create_side_stiff
        侧筋版建模

        Args:
            build_ele: the building element dict
                        .pyp文件的变量参数字典
            y_position:position of y axis 
                        侧筋板在y轴的位置
        Return:
            A list of 3D side stiff
            三维侧筋板列表
            
        '''
        long_extend_length = build_ele['LongEdgeMainExtendLength']                              #长筋板长边伸出长度
        long_side_length = build_ele['Length'] + long_extend_length                             #长筋板长边长度
        side_stiff_width = build_ele['BottomStiffenerWidth']                                    #侧筋板宽度
        side_stiff_height = build_ele['Thick'] - 2 * build_ele['StiffenerThick']                #侧筋板高度
        side_stiff_mid_thick = build_ele['SideStiffenerMidThick']                               #中间侧筋板厚度
        both_end_stiff_thick = build_ele['StiffenerThick']                                      #两头侧筋板厚度
        side_stiff_distance = build_ele['SideStiffenerDistance']                                #侧筋板间距
        
        #calculate
        raw_num = int(long_side_length / side_stiff_distance)
        distance_num = raw_num - 1
        side_stiff_num = raw_num + 2
        
        remain_length = (long_side_length - distance_num * side_stiff_distance)/2               


        stiff_list = []
        distance = 0



        for x in range(side_stiff_num):
            if x == 0 or x == side_stiff_num - 1:
                both_stiff_shape = self.shape_stiff(stiff_length=both_end_stiff_thick,
                                                    stiff_width=side_stiff_width,
                                                    stiff_height=side_stiff_height,
                                                    rX=-long_extend_length/2,
                                                    rY=y_position,
                                                    rZ=both_end_stiff_thick,
                                                    sX=distance)
                stiff_list.append(AllplanBasisElements.ModelElement3D(self.com_prop, self.long_surf, both_stiff_shape))

            else:
                mid_stiff_shape = self.shape_stiff(stiff_length=side_stiff_mid_thick,
                                                   stiff_width=side_stiff_width,
                                                   stiff_height=side_stiff_height,
                                                   rX=-long_extend_length/2,
                                                   rY=y_position,
                                                   rZ=both_end_stiff_thick,
                                                   sX=distance)
                stiff_list.append(AllplanBasisElements.ModelElement3D(self.com_prop, self.short_surf, mid_stiff_shape))
            
            if x == 0:
                distance += remain_length
            elif x == side_stiff_num - 2:
                distance += remain_length - both_end_stiff_thick
            else:
                distance += side_stiff_distance

        return stiff_list

    def create_top_stiff(self,build_ele,y_position=0,z_position=0):
        '''
        create_top_stiff
        上/下筋版建模

        Args:
            build_ele: the building element dict
            .pyp文件的变量参数字典
            y_position:
            z_position:
        Return:
            A list of 3D stiff model
            上/下筋板三维模型列表
        '''

        long_extend_length = build_ele['LongEdgeMainExtendLength']
        width = build_ele['BottomStiffenerWidth']
        length = build_ele['Length'] + long_extend_length
        height = build_ele['StiffenerThick']

        top_stiff = self.shape_stiff(stiff_length=length,
                         stiff_width=width,
                         stiff_height=height,
                         rX=-long_extend_length/2,
                         rY=y_position,
                         rZ=z_position)

        return [AllplanBasisElements.ModelElement3D(self.com_prop, self.long_surf, top_stiff)]

    def create_long_stiff(self,build_ele,y_position=0,z_position=0):
        '''
        create_long_stiff
        长面筋板建模

        Args:
            build_ele: the building element dict
            .pyp文件的变量参数字典
            y_position:
            z_position:
        Return:
            A list of 3D long stiff model
            长筋板三维模型列表           
            
        '''
        long_extend_length = build_ele['LongEdgeMainExtendLength']
        length = build_ele['Length'] + long_extend_length
        height = build_ele['Thick']
        width = build_ele['StiffenerThick']

        long_stiff = self.shape_stiff(stiff_length=length,
                                      stiff_width=width,
                                      stiff_height=height,
                                      rX=-long_extend_length/2,
                                      rY=y_position,
                                      rZ=z_position)

        return [AllplanBasisElements.ModelElement3D(self.com_prop, self.long_surf, long_stiff)]

    def create_vertical_short_stiff(self,build_ele,x_position=0,y_position=0,z_position=0):
        '''
        create_vertical_short_stiff
        垂直方向短筋板建模

        Args:
            build_ele: the building element dict
                       .pyp文件的变量参数字典
            x_position:
            y_position:
            z_position:
        Return:
            A list of 3D vertical short stiff model
            垂直方向短筋板三维模型列表
        '''
        width = build_ele['StiffenerThick']
        length = build_ele['LongEdgeMainExtendLength']/2 - width
        height = build_ele['Thick']

        vertical_short_stiff = self.shape_stiff(stiff_length=length,
                                                stiff_width=width,
                                                stiff_height=height,
                                                rX=x_position,
                                                rY=y_position,
                                                rZ=z_position)

        return [AllplanBasisElements.ModelElement3D(self.com_prop, self.short_surf, vertical_short_stiff)]

    def create_horizon_short_stiff(self,build_ele,x_position=0,y_position=0,z_position=0):
        '''
        create_horizon_short_stiff
        水平方向短筋板建模
        Args:
            build_ele: the building element dict
                        .pyp文件的变量参数字典
            x_position:
            y_position:
            z_position:
        Return:
            A list of 3D horizon short stiff model
            水平方向短筋板三维模型列表
        '''
        length = build_ele['LongEdgeMainExtendLength']/2 - build_ele['StiffenerThick']
        width = build_ele['Width'] - 2 * build_ele['StiffenerThick']
        height = build_ele['StiffenerThick']

        horizon_short_stiff = self.shape_stiff(stiff_length=length,
                                               stiff_width=width,
                                               stiff_height=height,
                                               rX=x_position,
                                               rY=y_position,
                                               rZ=z_position)

        return [AllplanBasisElements.ModelElement3D(self.com_prop, self.short_surf, horizon_short_stiff)]

    def create_short_stiff(self,build_ele,x_position):
        '''
        短筋板主面板建模
        Args:
            build_ele: the building element dict
                        .pyp文件的变量参数字典
            x_position:
        Return:
            A list of 3D stiff model
            短筋板三维模型列表
        '''
        length = build_ele['StiffenerThick']
        width = build_ele['Width']
        height = build_ele['Thick']

        short_stiff = self.shape_stiff(stiff_length=length,
                                       stiff_width=width,
                                       stiff_height=height,
                                       rX=x_position)

        return [AllplanBasisElements.ModelElement3D(self.com_prop, self.short_surf, short_stiff)]

    def shape_stiff(self,stiff_length,stiff_width,stiff_height,rX=0,rY=0,rZ=0,sX=0,sY=0,sZ=0):
        '''
        shape_stiff
        筋板构形

        Args:
            stiff_length:
            stiff_width:
            stiff_height:
            rX:
            rY:
            rZ:
            sX:
            sY:
            sZ:

        Return:
            A stiff object
            筋板对象
        '''

        args = {'refPoint':AllplanGeo.Point3D(rX,rY,rZ),
                'startPoint':AllplanGeo.Point3D(sX,sY,sZ),
                'vec1':AllplanGeo.Vector3D(stiff_length,0,0),
                'vec2':AllplanGeo.Vector3D(0,stiff_width,0),
                'vec3':AllplanGeo.Vector3D(0,0,stiff_height )}

        gen_stiff = AllplanGeo.Cuboid3D(**args)



        return gen_stiff

        
    #def shape_polyhed(self,build_dict):
    #    length = build_dict['Length']
    #    width = build_dict['Width']
    #    height = build_dict['Thick']

    #    base_pol = AllplanGeo.Polygon3D()
    #    base_pol += AllplanGeo.Point3D(length,0,0)
    #    base_pol += AllplanGeo.Point3D(length,width,0)
    #    base_pol += AllplanGeo.Point3D(0,width,0)
    #    base_pol += AllplanGeo.Point3D(0,width,height)
    #    base_pol += AllplanGeo.Point3D(length,width,height)
    #    base_pol += AllplanGeo.Point3D(length,0,height)
    #    base_pol += AllplanGeo.Point3D(length,0,0)

    #    err,poly = AllplanGeo.CreatePolyhedron(base_pol)

    #    print(base_pol,poly)

    #    return [AllplanBasisElements.ModelElement3D(self.com_prop, self.short_surf, base_pol)]