"""
Implementation of the functions for the creation of the reinforcement corbel shapes
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf


def column_corbel_shape_type1(column_width, column_thickness, corbel_width, corbel_top,
                              model_angles,
                              shape_props, concrete_cover):
    """
    Create the shape for the corbel type 1

    Return: Bar shape of the corbel in world coordinates

    Parameter:  column_width        Column width
                column_thickness    Column thickness
                corbel_width        Corbel width
                corbel_top          Top position (z) of the corbel
                model_angles        Angles for the local to global shape transformation
                shape_props         Shape properties
                concrete_cover      Concrete cover at the shape sides
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(AllplanGeo.Point2D(0., 0.), concrete_cover),
                             (AllplanGeo.Point2D(0., corbel_top), -concrete_cover),
                             (AllplanGeo.Point2D(column_width + corbel_width, corbel_top), -concrete_cover),
                             (concrete_cover + shape_props.diameter / 2)])

    shape_builder.SetSideLengthStart(1000.)

    shape = shape_builder.CreateShape(shape_props)

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

        shape_pol = shape.GetShapePolyline()
        shape_pol1 = AllplanGeo.Move(shape_pol,
                                     AllplanGeo.Vector3D(0, column_thickness - concrete_cover * 2 - \
                                                         shape_props.diameter, 0))

        for i in range(2, -1, -1):
            shape_pol += shape_pol1[i]

        bending_roller_vec = shape.GetBendingRoller()

        bending_roller_vec.append(shape_props.bending_roller)
        bending_roller_vec.append(shape_props.bending_roller)
        bending_roller_vec.append(shape_props.bending_roller)

        shape.SetShapePolyline(shape_pol)
        shape.SetBendingRoller(bending_roller_vec)

    return shape
