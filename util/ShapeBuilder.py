"""
Implementation of the functions for the creation of the general reinforcement shapes
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

def get_hook_type_from_angle(hook_type, hook_angle):
    """
    Create a longitudinal shape with hooks

    Parameter:  hook_angle  Hook angle
                hook_type   Type of the hooks, -1 set type from angle

    Return: Bar shape of the longitudinal shape in world coordinates
    """

    if hook_type != -1:
        return hook_type

    if abs(hook_angle) < 134:
        return AllplanReinf.HookType.eAngle

    return  AllplanReinf.HookType.eStirrup


def create_longitudinal_shape_with_hooks(length, model_angles,
                                         shape_props,
                                         concrete_cover_props,
                                         start_hook=0,
                                         end_hook=0):
    """
    Create a longitudinal shape with hooks

    Return: Bar shape of the longitudinal shape in world coordinates

    Parameter:  length                      Length of the geometry side
                model_angles                Angles for the local to global shape transformation
                shape_props                 Shape properties
                concrete_cover_props        Concrete cover properties: needed left, right, bottom
                start_hook                  Create an anchorage hook at the start point:
                                            -1 = no / 0 = calculate / >0 = value
                end_hook                    Create an anchorage hook at the end point::
                                            -1 = no / 0 = calculate / >0 = value
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (concrete_cover_props.right)])

    if start_hook == 0:
        shape_builder.SetAnchorageHookStart(90)
    elif start_hook > 0:
        shape_builder.SetHookStart(start_hook, 90, AllplanReinf.HookType.eAnchorage)

    if end_hook == 0:
        shape_builder.SetAnchorageHookEnd(90)
    elif end_hook > 0:
        shape_builder.SetHookEnd(end_hook, 90, AllplanReinf.HookType.eAnchorage)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_longitudinal_shape_with_anchorage(from_point, to_point,
                                             shape_props,
                                             concrete_cover_props,
                                             start_anchorage=0,
                                             end_anchorage=0):
    """
    Create a longitudinal shape with hooks

    Return: Bar shape of the longitudinal shape in world coordinates

    Parameter:  from_point                  Shape from point
                to_point                    Shape to point
                shape_props                 Shape properties
                concrete_cover_props        Concrete cover properties: needed left, right, bottom
                start_anchorage             Anchorage length at the start point, 0 = no
                end_anchorage               Anchorage length at the end point, 0= no
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(from_point, concrete_cover_props.left),
                             (to_point, concrete_cover_props.bottom),
                             (concrete_cover_props.right)])

    if start_anchorage != 0:
        shape_builder.SetAnchorageLengthStart(start_anchorage)

    if end_anchorage != 0:
        shape_builder.SetAnchorageLengthEnd(end_anchorage)

    return shape_builder.CreateShape(shape_props)


def create_l_shape_with_hooks(length,
                              width,
                              model_angles,
                              shape_props,
                              concrete_cover_props,
                              start_hook=0,
                              end_hook=0):
    """
    Create a L shape with hooks

    Return: Bar shape of the L shape in world coordinates

    Parameter:  length                      Length of the l shape
                width                       Width of the l shape
                model_angles                Angles for the local to global shape transformation
                shape_props                 Shape properties
                concrete_cover_props        Concrete cover properties: needed left, right, bottom
                start_hook                  Create an anchorage hook at the start point:
                                            -1 = no / 0 = calculate / >0 = value
                end_hook                    Create an anchorage hook at the end point::
                                            -1 = no / 0 = calculate / >0 = value
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (AllplanGeo.Point2D(length, width), concrete_cover_props.right),
                             (concrete_cover_props.top)])

    if start_hook == 0:
        shape_builder.SetAnchorageHookStart(90)
    elif start_hook > 0:
        shape_builder.SetHookStart(start_hook, 90, AllplanReinf.HookType.eAnchorage)

    if end_hook == 0:
        shape_builder.SetAnchorageHookEnd(90)
    elif end_hook > 0:
        shape_builder.SetHookEnd(end_hook, 90, AllplanReinf.HookType.eAnchorage)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stirrup(length, width,
                   model_angles,
                   shape_props,
                   concrete_cover_props,
                   stirrup_type=AllplanReinf.StirrupType.Normal):
    """
    Create a stirrup

    Return: Bar shape of the stirrup in world coordinates

    Parameter:  length                      Length of the geometry side
                width                       Width of the geometry side
                model_angles                Angles for the local to global shape transformation
                shape_props                 Shape properties
                concrete_cover_props        Concrete cover at the sides
                stirrup_type                Type of the stirrup
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(length, width), concrete_cover_props.top),
                             (AllplanGeo.Point2D(0, width), concrete_cover_props.top),
                             (AllplanGeo.Point2D(0, 0), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (AllplanGeo.Point2D(length, width), concrete_cover_props.right),
                             (concrete_cover_props.top)])

    if stirrup_type == AllplanReinf.StirrupType.Torsion:
        shape_builder.AddPoint(AllplanGeo.Point2D(0, width), concrete_cover_props.top, 0)

    shape = shape_builder.CreateStirrup(shape_props,
                                        stirrup_type)


    #----------------- Rotate the shape in the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_open_stirrup(length, width,
                        model_angles,
                        shape_props,
                        concrete_cover_props,
                        start_hook       = 0,
                        end_hook         = 0,
                        start_hook_angle = 90.0,
                        end_hook_angle   = 90.0,
                        hook_type        = -1):
    """
    Create a stirrup

    Return: Bar shape of the stirrup in world coordinates

    Parameter:  length                  Length of the geometry side
                width                   Width of the geometry side
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_hook              Create a hook at the start point:
                                        -1 = no / 0 = calculate / >0 = value
                end_hook                Create a hook at the end point:
                                        -1 = no / 0 = calculate / >0 = value
                start_hook_angle        Create a hook with specified angle [-180, 180]:
                                        default is 90°
                end_hook_angle          Create a hook with specified angle [-180, 180]:
                                        default is 90°
                hook_type               Type of the hooks, -1 set type from angle
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(0, width), concrete_cover_props.top),
                             (AllplanGeo.Point2D(0, 0), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), concrete_cover_props.bottom),
                             (AllplanGeo.Point2D(length, width), concrete_cover_props.right),
                             (concrete_cover_props.top)])

    if start_hook >= 0:
        shape_builder.SetHookStart(start_hook, start_hook_angle,
                                   get_hook_type_from_angle(hook_type, start_hook_angle))

    if end_hook >= 0:
        shape_builder.SetHookEnd(end_hook, end_hook_angle,
                                 get_hook_type_from_angle(hook_type, end_hook_angle))

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape in the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_s_hook(length, model_angles,
                  shape_props,
                  concrete_cover_props, hook_length=0):
    """
    Create a S hook

    Return: Bar shape of the S hook shape in world coordinates

    Parameter:  length                      Length of the geometry side
                model_angles                Angles for the local to global shape transformation
                shape_props                 Shape properties
                concrete_cover_props        Concrete cover properties: needed top and bottom
                hook_length                 0 = calculate / >0 = value
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), 0),
                             (concrete_cover_props.right)])

    shape_builder.SetHookStart(hook_length, 180, AllplanReinf.HookType.eStirrup)
    shape_builder.SetHookEnd(hook_length, -180, AllplanReinf.HookType.eStirrup)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_hook_stirrup(length, model_angles,
                        shape_props,
                        concrete_cover_props, hook_length=0):
    """
    Create a hook stirrup

    Return: Bar shape of the S hook shape in world coordinates

    Parameter:  length                      Length of the geometry side
                model_angles                Angles for the local to global shape transformation
                shape_props                 Shape properties
                concrete_cover_props        Concrete cover properties: needed top and bottom
                hook_length                 0 = calculate / >0 = value
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_props.left),
                             (AllplanGeo.Point2D(length, 0), 0),
                             (concrete_cover_props. right)])

    shape_builder.SetHookStart(hook_length, 180, AllplanReinf.HookType.eStirrup)
    shape_builder.SetHookEnd(hook_length, 180, AllplanReinf.HookType.eStirrup)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_spacer(length, width, height, model_angles, shape_props):
    """
    Create a spacer

    Return: Bar shape of the S hook shape in world coordinates

    Parameter:  length                      Length of the spacer
                width                       Width of the spacer
                height                      Height of the spacer
                model_angles                Angles for the local to global shape transformation
                shape_props                 Shape properties
    """

    len2 = length / 2

    shape_pol = AllplanGeo.Polyline3D()
    shape_pol += AllplanGeo.Point3D(0, 0, 0)
    shape_pol += AllplanGeo.Point3D(len2, 0, 0)
    shape_pol += AllplanGeo.Point3D(len2, 0, height)
    shape_pol += AllplanGeo.Point3D(len2, width, height)
    shape_pol += AllplanGeo.Point3D(len2, width, 0)
    shape_pol += AllplanGeo.Point3D(length, width, 0)

    br_list = AllplanReinf.BendingRollerList()

    bero = shape_props.bending_roller

    br_list[:] = [bero, bero, bero, bero]

    shape = AllplanReinf.BendingShape(shape_pol, br_list, shape_props.diameter, shape_props.steel_grade, -1,
                                      AllplanReinf.BendingShapeType.BarSpacer)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_u_link(width, side_length, model_angles, shape_props, concrete_cover_props, hook_length):
    """
    Create an u-link (opend stirrup)

    Return: Bar shape of the S hook shape in world coordinates

    Parameter:  width                       Width of the links base line
                side_length                 Side length
                model_angles                Angles for the local to global shape transformation
                shape_props                 Shape properties
                concrete_cover_props        Concrete cover properties
                hook                        Create an anchorage hook at the end point:
                                            -1 = no / 0 = calculate / >0 = value
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(0, side_length), 0),
                             (AllplanGeo.Point2D(0, 0), concrete_cover_props.left),
                             (AllplanGeo.Point2D(width, 0), concrete_cover_props.bottom),
                             (AllplanGeo.Point2D(width, side_length), concrete_cover_props.right),
                             (0)])

    shape_builder.SetSideLengthStart(side_length)
    shape_builder.SetSideLengthEnd(side_length)

    if hook_length == 0:
        shape_builder.SetAnchorageHookStart(90)
        shape_builder.SetAnchorageHookEnd(90)

    elif hook_length > 0:
        shape_builder.SetHookStart(hook_length, 90, AllplanReinf.HookType.eAnchorage)
        shape_builder.SetHookEnd(hook_length, 90, AllplanReinf.HookType.eAnchorage)

    u_shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if u_shape.IsValid() is True:
        u_shape.Rotate(model_angles)

    return u_shape


def create_freeform_shape_with_hooks(points, model_angles,
                                     shape_props,
                                     concrete_cover,
                                     start_hook=0,
                                     end_hook=0 ):
    """
    Create a longitudinal shape with hooks

    Return: Bar shape of the longitudinal shape in world coordinates

    Parameter:  points                      Points of the geometry side (min. 2 points)
                model_angles                Angles for the local to global shape transformation
                shape_props                 Shape properties
                concrete_cover_props        Concrete cover properties: needed left, right, bottom
                start_hook                  Create an anchorage hook at the start point:
                                            -1 = no / 0 = calculate / >0 = value
                end_hook                    Create an anchorage hook at the end point::
                                            -1 = no / 0 = calculate / >0 = value
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    for point in points:
        shape_builder.AddPoints([(AllplanGeo.Point2D(point), concrete_cover),(concrete_cover)])

    if start_hook == 0:
        shape_builder.SetAnchorageHookStart(90)
    elif start_hook > 0:
        shape_builder.SetHookStart(start_hook, 90, AllplanReinf.HookType.Anchorage)

    if end_hook == 0:
        shape_builder.SetAnchorageHookEnd(90)
    elif end_hook > 0:
        shape_builder.SetHookEnd(end_hook, 90, AllplanReinf.HookType.Anchorage)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape

