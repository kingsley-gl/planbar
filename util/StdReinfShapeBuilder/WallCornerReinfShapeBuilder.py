"""
Implementation of the functions for the creation of the reinforcement shapes
inside a wall corner

The walls are define by the following lines

                 s        e
                 |        | top_line2
                 |        |
                 |        |
                 |        s        top_line1
    bottom_line2 |        |e-----------------------s
                 |
                 | wall 2               wall 1
                 |
                 |        s------------------------e
                 |        |      bottom_line1
                 |        |
                 |        |
                 |        |
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import GeometryValidate as GeometryValidate


def create_link_shape_in_wall1(bottom_line1, top_line1, bottom_line2, top_line2,
                               shape_props, concrete_cover_props, start_length, end_length):

    """
    Create the link shape in the first wall

                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       ------------------------------------
                    |  ----------------------------
                    |  |
                    |  ----------------------------
                    |-------------------------------------------

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    del top_line2

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (top_line1, concrete_cover_props.left),
                            (bottom_line2, concrete_cover_props.bottom),
                            (bottom_line1, concrete_cover_props.right),
                            (concrete_cover_props.top) ])

    shape_builder.SetSideLengthStart(start_length)
    shape_builder.SetSideLengthEnd(end_length)

    return shape_builder.CreateShape(shape_props)


def create_link_shape_in_wall2(bottom_line1, top_line1, bottom_line2, top_line2,
                               shape_props, concrete_cover_props, start_length, end_length):
    """
    Create the link shape in the second wall

                    |       |
                    |       |
                    |       |
                    |       |
                    | |   | |
                    | |   | |
                    | |   | |
                    | |   | |
                    | |   | |
                    | |   | ------------------------------------
                    | |   |
                    | |   |
                    | |---|
                    |-------------------------------------------

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    del top_line1

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (bottom_line2, concrete_cover_props.left),
                            (bottom_line1, concrete_cover_props.bottom),
                            (top_line2, concrete_cover_props.right),
                            (concrete_cover_props.top) ])

    shape_builder.SetSideLengthStart(start_length)
    shape_builder.SetSideLengthEnd(end_length)

    return shape_builder.CreateShape(shape_props)


def create_outer_angle_shape(bottom_line1, top_line1, bottom_line2, top_line2,
                             shape_props, concrete_cover_props, start_length, end_length):
    """
    Create the outer angle shape

                    |       |
                    |       |
                    |       |
                    |       |
                    | |     |
                    | |     |
                    | |     |
                    | |     |
                    | |     |
                    | |     ------------------------------------
                    | |
                    | |
                    | |------------------------
                    |-------------------------------------------

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    del top_line1
    del top_line2

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (bottom_line2, concrete_cover_props.left),
                            (bottom_line1, concrete_cover_props.bottom),
                            (concrete_cover_props.right) ])

    shape_builder.SetSideLengthStart(start_length)
    shape_builder.SetSideLengthEnd(end_length)

    return shape_builder.CreateShape(shape_props)


def create_inner_angle_shape1(bottom_line1, top_line1, bottom_line2, top_line2,
                              shape_props, concrete_cover_props, start_length, end_length):
    """
    Create the inner angle shape 1

                    |       |
                    |       |
                    |       |
                    |       |
                    | |     |
                    | |     |
                    | |     |
                    | |     |
                    | |     |
                    | |     ------------------------------------
                    | |------------------------
                    |
                    |
                    |-------------------------------------------

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    del top_line2

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (bottom_line2, concrete_cover_props.left),
                            (top_line1.EndPoint, top_line1.StartPoint, -concrete_cover_props.top),
                            (concrete_cover_props.right) ])

    shape_builder.SetSideLengthStart(start_length)
    shape_builder.SetSideLengthEnd(end_length)

    return shape_builder.CreateShape(shape_props)


def create_inner_angle_shape2(bottom_line1, top_line1, bottom_line2, top_line2,
                              shape_props, concrete_cover_props, start_length, end_length):
    """
    Create the inner angle shape 2

                    |       |
                    |       |
                    |       |
                    |       |
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |     | ------------------------------------
                    |     |
                    |     |
                    |     |--------------
                    |-------------------------------------------

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    del top_line1
    del bottom_line2

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (top_line2.EndPoint, top_line2.StartPoint, -concrete_cover_props.right),
                            (bottom_line1, concrete_cover_props.bottom),
                            (concrete_cover_props.right) ])

    shape_builder.SetSideLengthStart(start_length)
    shape_builder.SetSideLengthEnd(end_length)

    return shape_builder.CreateShape(shape_props)


def create_longitudinal_shape1_wall1(bottom_line1, top_line1, bottom_line2, top_line2,
                                     shape_props, concrete_cover_props, start_length, end_length):
    """
    Create the longitudinal shape in wall 1

                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
     ----------------       ------------------------------------


            ----------------------------
     ----------------       ------------------------------------
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    intersect, pnt1 = AllplanGeo.IntersectionCalculusEx(bottom_line1, bottom_line2)
    
    if not GeometryValidate.intersection(intersect):
        return AllplanReinf.BendingShape()

    intersect, pnt2 = AllplanGeo.IntersectionCalculusEx(bottom_line1, top_line2)
    
    if not GeometryValidate.intersection(intersect):
        return AllplanReinf.BendingShape()

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(pnt1, 0),
                             (pnt2, concrete_cover_props.bottom),
                             (0) ])

    shape_builder.SetAnchorageLengthStart(start_length)
    shape_builder.SetAnchorageLengthEnd(end_length)

    return shape_builder.CreateShape(shape_props)


def create_longitudinal_shape2_wall1(bottom_line1, top_line1, bottom_line2, top_line2,
                                     shape_props, concrete_cover_props, start_length, end_length):
    """
    Create the longitudinal shape in wall 1

                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
     ----------------       ------------------------------------
            ----------------------------


     ----------------       ------------------------------------
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |
                    |       |

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    shape = create_longitudinal_shape1_wall1(bottom_line1, top_line1, bottom_line2, top_line2,
                                             shape_props, concrete_cover_props, start_length, end_length)

    err, shape_line = AllplanGeo.Offset(concrete_cover_props.top + concrete_cover_props.bottom +
                                        shape_props.diameter, top_line1)

    if not GeometryValidate.offset(err):
        return AllplanReinf.BendingShape()

    intersect, pnt1 = AllplanGeo.IntersectionCalculusEx(shape_line, top_line2)
    
    if not GeometryValidate.intersection(intersect):
        return AllplanReinf.BendingShape()

    intersect, pnt2 = AllplanGeo.IntersectionCalculusEx(bottom_line1, top_line2)
    
    if not GeometryValidate.intersection(intersect):
        return AllplanReinf.BendingShape()

    move_vec = AllplanGeo.Vector2D(pnt2, pnt1)

    shape.Move(AllplanGeo.Vector3D(move_vec))

    return shape


def create_longitudinal_shape1_wall2(bottom_line1, top_line1, bottom_line2, top_line2,
                                     shape_props, concrete_cover_props, start_length, end_length):
    """
    Create the longitudinal shape in wall 2

                    |       |
                    |       |
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |     | ------------------------------------
                    |     | 
                    |     | 
                    |     | 
                    |     | ------------------------------------
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |     | |
                    |       |

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    intersect, pnt1 = AllplanGeo.IntersectionCalculusEx(bottom_line1, top_line2)
    
    if not GeometryValidate.intersection(intersect):
        return AllplanReinf.BendingShape()

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddPoints([(pnt1, 0),
                             (top_line1.EndPoint, concrete_cover_props.bottom),
                             (0) ])

    shape_builder.SetAnchorageLengthStart(start_length)
    shape_builder.SetAnchorageLengthEnd(end_length)

    return shape_builder.CreateShape(shape_props)


def create_longitudinal_shape2_wall2(bottom_line1, top_line1, bottom_line2, top_line2,
                                     shape_props, concrete_cover_props, start_length, end_length):
    """
    Create the longitudinal shape in wall 2

                    |       |
                    |       |
                    |       |
                    |       |
                    | |     |
                    | |     |
                    | |     |
                    | |     |
                    | |     |
                    | |     ------------------------------------
                    | |
                    | |
                    | |
                    | |     ------------------------------------
                    | |     |
                    | |     |
                    | |     |
                    | |     |
                    | |     |
                    |       |
                    |       |

    Return: Bar shape in world coordinates

    Parameter:  bottom_line1          Bottom line of the first wall
                top_line1             Top line of the first wall
                bottom_line2          Bottom line of the second wall
                top_line2             Top line of the second wall
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                start_length          Length of the start side
                end_length            Length of the end side
    """

    shape = create_longitudinal_shape1_wall2(bottom_line1, top_line1, bottom_line2, top_line2,
                                             shape_props, concrete_cover_props, start_length, end_length)

    err, shape_line = AllplanGeo.Offset(concrete_cover_props.top + concrete_cover_props.bottom +
                                        shape_props.diameter, bottom_line2)

    if not GeometryValidate.offset(err):
        return AllplanReinf.BendingShape()

    intersect, pnt1 = AllplanGeo.IntersectionCalculusEx(shape_line, top_line1)
    
    if not GeometryValidate.intersection(intersect):
        return AllplanReinf.BendingShape()

    intersect, pnt2 = AllplanGeo.IntersectionCalculusEx(top_line2, top_line1)
    
    if not GeometryValidate.intersection(intersect):
        return AllplanReinf.BendingShape()

    move_vec = AllplanGeo.Vector2D(pnt2, pnt1)

    shape.Move(AllplanGeo.Vector3D(move_vec))

    return shape


def create_longitudional_bar(z_min, z_max, place_pnt, shape_props, concrete_cover_props,
                             bottom_anchorage = 0, top_anchorage = 0):
    """
    Create the longitudinal bar

    Return: Bar shape in world coordinates

    Parameter:  z_min                 Minimal z coordinate of the geometry
                z_max                 Maximal z coordinate of the geometry
                shape_props           Shape properties
                concrete_cover_props  Concrete cover at the sides
                bottom_anchorage      Anchorage length at the bottom point, 0 = no
                top_anchorage         Anchorage length at the top point, 0= no
    """

    shape_pol = AllplanGeo.Polyline3D()

    if bottom_anchorage:
        shape_pol += AllplanGeo.Point3D(place_pnt.X, place_pnt.Y, z_min - bottom_anchorage)
    else:
        shape_pol += AllplanGeo.Point3D(place_pnt.X, place_pnt.Y, z_min + concrete_cover_props.bottom)

    if top_anchorage:
        shape_pol += AllplanGeo.Point3D(place_pnt.X, place_pnt.Y, z_max + top_anchorage)
    else:
        shape_pol += AllplanGeo.Point3D(place_pnt.X, place_pnt.Y, z_max - concrete_cover_props.top)

    return AllplanReinf.BendingShape(shape_pol, AllplanReinf.BendingRollerList(),
                                     shape_props.diameter, shape_props.steel_grade,
                                     shape_props.concrete_grade,
                                     AllplanReinf.BendingShapeType.LongitudinalBar)

