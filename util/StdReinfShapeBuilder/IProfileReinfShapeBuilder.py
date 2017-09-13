#pylint: disable=W1401
# Anomalous backslash in string

"""
Implementation of the functions for the creation of the reinforcement shapes
inside an I profile.

The points are defined in the following order.
The picture shows a section in the y/z plane,
the x coordinate is the section coordinate.

                  6 ----------5
                  |           |
                  7           4
                   \         /
                    8       3
                    |       |
                    9       2
                   /         \
                  10          1
                  |           |
                  11----------0
"""

#pylint: enable=W1401
# Only disabled for comment part

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf


def get_rotation_matrix_from_yz_to_xy():
    """
    Get the rotation matrix for global/local transformation
    """

    rot_mat = AllplanGeo.Matrix3D()
    rot_angle = AllplanGeo.Angle()

    rot_angle.SetDeg(-90)

    rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(0, 0, 1000)), rot_angle)

    rot_angle.SetDeg(90)

    rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(1000, 0, 0)), rot_angle)

    return rot_mat


def create_bottom_flange_shape(polyline3d, shape_props, concrete_cover_props):
    """
    Create the bottom flange shape

    Return: Bar shape of the flange shape in world coordinates

    Parameter:  polyline3d              3D polyline of the geometry
                shape_props             Shape properties
                concrete_cover_props    Concrete cover properies: needed left, right, bottom
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder(get_rotation_matrix_from_yz_to_xy())

    shape_builder.AddPoints([(polyline3d[9], concrete_cover_props.right),
                             (polyline3d[10], concrete_cover_props.left),
                             (polyline3d[11], concrete_cover_props.left),
                             (polyline3d[0], concrete_cover_props.bottom),
                             (polyline3d[1], concrete_cover_props.right),
                             (polyline3d[2], concrete_cover_props.right)])

    shape_builder.SetConcreteCoverLineStart(polyline3d[3], polyline3d[2], -concrete_cover_props.right)
    shape_builder.SetConcreteCoverLineEnd(polyline3d[9], polyline3d[8], -concrete_cover_props.left)

    return shape_builder.CreateShape(shape_props)


def create_top_flange_shape(polyline3d, shape_props, concrete_cover_props):
    """
    Create the top flange shape

    Return: Bar shape of the flange shape in world coordinates

    Parameter:  polyline3d              3D polyline of the geometry
                shape_props             Shape properties
                concrete_cover_props    Concrete cover properies: needed left, right, top
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder(get_rotation_matrix_from_yz_to_xy())

    shape_builder.AddPoints([(polyline3d[3], concrete_cover_props.left),
                             (polyline3d[4], concrete_cover_props.right),
                             (polyline3d[5], concrete_cover_props.right),
                             (polyline3d[6], concrete_cover_props.top),
                             (polyline3d[7], concrete_cover_props.left),
                             (polyline3d[8], concrete_cover_props.left)])

    shape_builder.SetConcreteCoverLineStart(polyline3d[9], polyline3d[8], -concrete_cover_props.left)
    shape_builder.SetConcreteCoverLineEnd(polyline3d[3], polyline3d[2], -concrete_cover_props.right)

    return shape_builder.CreateShape(shape_props)



def create_web_stirrup(polyline3d, shape_props, concrete_cover_props):
    """
    Create the web stirrup

    Return: Bar shape of the flange shape in world coordinates

    Parameter:  polyline3d              3D polyline of the geometry
                shape_props             Shape properties
                concrete_cover_props    Concrete cover properies: needed left, right, bottom
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder(get_rotation_matrix_from_yz_to_xy())

    shape_builder.AddSides([(polyline3d[5], polyline3d[6], concrete_cover_props.top),
                            (polyline3d[8], polyline3d[9], concrete_cover_props.left),
                            (polyline3d[11], polyline3d[0], concrete_cover_props.bottom),
                            (polyline3d[2], polyline3d[3], concrete_cover_props.right)])

    return shape_builder.CreateStirrup(shape_props, AllplanReinf.StirrupType.Normal)
