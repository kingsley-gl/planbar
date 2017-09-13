"""
Implementation of the functions for the creation of freeform stirrup shapes
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

from StdReinfShapeBuilder.GeneralReinfShapeBuilder import get_hook_type_from_angle


def get_rotation_matrix_from_xz_to_xy():
    """
    Get the rotation matrix for global/local transformation
    """

    rot_mat = AllplanGeo.Matrix3D()
    rot_angle = AllplanGeo.Angle()
    rot_angle.SetDeg(-90)
    rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(1000, 0, 0)), rot_angle)
    return rot_mat

def create_profile_shape(polyline3d,
                         rotation_matrix,
                         shape_props,
                         concrete_cover,
                         start_hook       = 0,
                         end_hook         = 0,
                         start_hook_angle = 90.0,
                         end_hook_angle   = 90.0,
                         hook_type        = -1):
    """
    Create the bottom flange shape

    Return: Bar shape of the flange shape in world coordinates

    Parameter:  polyline3d              3D polyline of the geometry
                shape_props             Shape properties
                concrete_cover          Concrete cover used for all sides
                start_hook              Create an anchorage hook at the start point:
                                        -1 = no / 0 = calculate / >0 = value
                end_hook                Create an anchorage hook at the end point:
                                        -1 = no / 0 = calculate / >0 = value
                start_hook_angle        Create an anchorage hook with specified angle [-180, 180]:
                                        default is 90°
                end_hook_angle          Create an anchorage hook with specified angle [-180, 180]:
                                        default is 90°
                hook_type               Type of the hooks, -1 set type from angle
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder(rotation_matrix)

    # fill up a list of points / concrete_cover values
    point_concrete_tuple_list = []
    for index in range(polyline3d.Count()):
        point_concrete_tuple_list.append((polyline3d[index], concrete_cover))

    shape_builder.AddPoints(point_concrete_tuple_list)

    shape_builder.SetConcreteCoverStart(concrete_cover)
    shape_builder.SetConcreteCoverEnd(concrete_cover)

    if start_hook >= 0:
        shape_builder.SetHookStart(start_hook, start_hook_angle,
                                   get_hook_type_from_angle(hook_type, start_hook_angle))

    if end_hook >= 0:
        shape_builder.SetHookEnd(end_hook, end_hook_angle,
                                 get_hook_type_from_angle(hook_type, end_hook_angle))

    return shape_builder.CreateShape(shape_props)

def create_profile_stirrup(polyline3d,
                           rotation_matrix,
                           shape_props,
                           concrete_cover,
                           stirrup_type = AllplanReinf.StirrupType.Normal):
    """
    Create a freeform stirrup shape

    Return: Bar shape of the stirrup shape in world coordinates

    Parameter:  polyline3d              3D polyline of the geometry
                shape_props             Shape properties
                concrete_cover          Concrete cover used for all sides
                stirrup_type            Type of the stirrup
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder(rotation_matrix)

    # fill up a list of points / concrete_cover values
    point_concrete_tuple_list = []
    for index in range(polyline3d.Count()):
        point_concrete_tuple_list.append((polyline3d[index], concrete_cover))

    shape_builder.AddPoints(point_concrete_tuple_list)

    return shape_builder.CreateStirrup(shape_props, stirrup_type)

