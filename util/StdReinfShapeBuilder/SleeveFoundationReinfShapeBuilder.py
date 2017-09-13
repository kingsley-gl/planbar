"""
Implementation of the functions for the creation of the reinforcement shapes
inside a sleeve foundation.

                        Sleeve coordinates

    /YRightOut |----------------------------------------------|
                |                                              |
                |                                              |
                |      |--------------------------------|      |
                |      | /YRightIn                      |      |
                |      |                                |      |
                |      |                                |      |
                |      |                                |      |
                |      |                                |      |
                |      | x_left_in/YLeftIn    XRightInt/  |      |
                |      |---------------------------------      |
                |                                              |
                |                                              |
    x_sleeve/0 ------------------------------------------------ x_right_out/
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

def create_vertial_sleeve_foundation_shape(found_length, found_height, x_sleeve,
                                           sleeve_out_length, sleeve_height, sleeve_thickness,
                                           model_angles,
                                           shape_props,
                                           concrete_cover_bottom, concrete_cover_top,
                                           concrete_cover_outside, concrete_cover_inside):
    """
    Create the vertical sleeve foundation shape

    Return: Bar shape in world coordinates

    Parameter:  found_length            Found length
                found_height            Found height
                x_sleeve                X coordinate of the sleeve
                sleeve_out_length       Out length of the sleeve
                sleeve_height           Sleeve height
                sleeve_thickness        Sleeve thickness
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_bottom   Concrete cover at the bottom side
                concrete_cover_top      Concrete cover at the top side
                concrete_cover_outside  Concrete cover at the out side
                concrete_cover_inside   Concrete cover at the in side
    """

    x_left_in   = x_sleeve + sleeve_thickness
    x_right_out = x_left_in + sleeve_out_length - sleeve_thickness
    x_right_in  = x_right_out - sleeve_thickness
    height      = found_height + sleeve_height


    #------------------ Create the vertical reinforcement inside the foundation an sleeve wall

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(), concrete_cover_bottom),
                             (AllplanGeo.Point2D(x_left_in, 0), concrete_cover_bottom),
                             (AllplanGeo.Point2D(x_left_in, height), concrete_cover_inside),
                             (AllplanGeo.Point2D(x_sleeve, height), concrete_cover_top),
                             (AllplanGeo.Point2D(x_sleeve, 0), concrete_cover_outside),
                             (AllplanGeo.Point2D(x_right_out, 0), concrete_cover_bottom),
                             (AllplanGeo.Point2D(x_right_out, height), concrete_cover_outside),
                             (AllplanGeo.Point2D(x_right_in, height), concrete_cover_top),
                             (AllplanGeo.Point2D(x_right_in, 0), concrete_cover_inside),
                             (AllplanGeo.Point2D(found_length, 0), concrete_cover_bottom),
                             (concrete_cover_bottom)])

    shape_builder.SetAnchorageHookStartFromSide()
    shape_builder.SetAnchorageHookEndFromSide()

    shape = shape_builder.CreateShape(shape_props)


    #----------------- AllplanGeo.Move the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_sleeve_wall_shape(wall_length, wall_width,
                             model_angles,
                             shape_props,
                             concrete_cover):
    """
    Create the sleeve foundation wall shape

    Return: Bar shape of the wall in world coordinates

    Parameter:  wall_length         Wall length
                wall_width          Wall width
                model_angles        Angles for the local to global shape transformation
                shape_props         Shape properties
                concrete_cover      Concrete cover at the sides
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(0, 0), concrete_cover),
                             (AllplanGeo.Point2D(wall_length, 0), concrete_cover),
                             (AllplanGeo.Point2D(wall_length, wall_width), concrete_cover),
                             (AllplanGeo.Point2D(0, wall_width), concrete_cover),
                             (AllplanGeo.Point2D(0, 0), concrete_cover),
                             (AllplanGeo.Point2D(wall_length, 0), concrete_cover),
                             (concrete_cover)])

    shape_builder.SetOverlapLengthEnd()

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape in the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape
