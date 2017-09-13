"""
Implementation of the functions for the creation of the reinforcement shapes
inside a stairs.

The stairs is defined by the following points

                  11
                    |------------------- 10
                 12 |                   |
                    /               8---9
                   /                 |
                  /     /-------------
                 /     / 6           7
                /     /
               /     /
  1         0 /     /
  -----------/     /
  |               /
 2---3           /
     |          /
     ----------/
     4         5
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import GeometryValidate as GeometryValidate


def create_stairs_shape_type_4_5_6_11_10(points, model_angles,
                                         shape_props, concrete_cover_props,
                                         start_length, end_length):
    """
                            /-------- 10
                           /
                          /
                         /
                        /
                       /
                      /
                     /
                    /
       4 ----------/ 5

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[4], points[5], concrete_cover_props.bottom),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (points[11], points[10], -concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_1_0_5_6(points, model_angles,
                                     shape_props, concrete_cover_props,
                                     start_length, end_length):
    """
                      / 6
                     /
                    /
        1----------/

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[1], points[0], -concrete_cover_props.top),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_4_5_0_12(points, model_angles,
                                      shape_props, concrete_cover_props,
                                      start_length, end_length):
    """
                      / 12
                     /
                    /
        4----------/

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[4], points[5], concrete_cover_props.bottom),
                            (points[0], points[12], -concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_0_12_6_7(points, model_angles,
                                      shape_props, concrete_cover_props,
                                      start_length, end_length):
    """
                       /-------------
                      /            7
                     /
                    /
                   /  0

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[0], points[12], -concrete_cover_props.top),
                            (points[6], points[7], concrete_cover_props.bottom),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_10_11_12_0(points, model_angles,
                                        shape_props, concrete_cover_props,
                                        start_length, end_length):
    """
                       /-------------
                      /            10
                     /
                    /
                   /  0

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (points[12], points[0], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)
    else:
        shape_builder.SetConcreteCoverLineEnd(points[4], points[5], concrete_cover_props.bottom)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_10_11_12_0_5_4(points, model_angles,
                                            shape_props, concrete_cover_props,
                                            start_length, end_length):
    """
                       /-------------
                      /            10
                     /
                    / 0
                   /
           4 ------

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (points[12], points[0], concrete_cover_props.top),
                            (points[5], points[4], -concrete_cover_props.bottom),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)
    else:
        shape_builder.SetConcreteCoverLineEnd(points[5], points[4], concrete_cover_props.bottom)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_0_1_2_3_5_6(points, model_angles,
                                         shape_props, concrete_cover_props,
                                         start_length, end_length):
    """
                    / 6
                   /
                  /
              0  /
      --------- /
      |   3    /
      --------/

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[0], points[1], concrete_cover_props.top),
                            (points[1], points[2], concrete_cover_props.top),
                            (points[2], points[3], concrete_cover_props.top),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)
    else:
        shape_builder.SetConcreteCoverLineStart(points[5], points[6], concrete_cover_props.bottom)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)
    else:
        set_end_length_intersection_side_5_6(points, shape_builder, concrete_cover_props.bottom)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_6_5_0_1_2_3(points, model_angles,
                                         shape_props, concrete_cover_props,
                                         start_length, end_length):
    """
                    / 6
                   /
                  /
              0  /
      --------- /
      |   3
      --------

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[6], points[5], -concrete_cover_props.bottom),
                            (points[0], points[1], concrete_cover_props.top),
                            (points[1], points[2], concrete_cover_props.top),
                            (points[2], points[3], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)
    else:
        result, i_pnt1 = AllplanGeo.IntersectionCalculusEx(AllplanGeo.Line2D(points[5], points[6]),
                                                           AllplanGeo.Line2D(points[7], points[8]))

        if not GeometryValidate.intersection(result):
            return AllplanReinf.BendingShape()

        result, i_pnt2 = AllplanGeo.IntersectionCalculusEx(AllplanGeo.Line2D(points[5], points[6]),
                                                           AllplanGeo.Line2D(points[10], points[11]))

        if not GeometryValidate.intersection(result):
            return AllplanReinf.BendingShape()

        if i_pnt1.Y < i_pnt2.Y:
            shape_builder.SetConcreteCoverLineStart(points[7], points[8], concrete_cover_props.top)
        else:
            shape_builder.SetConcreteCoverLineStart(points[11], points[10], -concrete_cover_props.top)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_6_5_0_1_3_4_5_6(points, model_angles,
                                             shape_props, concrete_cover_props,
                                             start_length, end_length):
    """
                   // 6
                  //
      -----------//
      |          /
      |         /
      |        /
   4  --------/ 5

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[6], points[5], -concrete_cover_props.bottom),
                            (points[0], points[1], concrete_cover_props.top),
                            (points[3], points[4], concrete_cover_props.top),
                            (points[4], points[5], concrete_cover_props.bottom),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)
    else:
        set_start_length_intersection_side_6_5(points, shape_builder, concrete_cover_props.bottom)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)
    else:
        set_end_length_intersection_side_5_6(points, shape_builder, concrete_cover_props.bottom)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_0_1_3_4_5_6(points, model_angles,
                                         shape_props, concrete_cover_props,
                                         start_length, end_length):
    """
                    / 6
                   /
      ----------- /
      |          /
      |         /
      |        /
   4  --------/ 5

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[0], points[1], concrete_cover_props.top),
                            (points[3], points[4], concrete_cover_props.top),
                            (points[4], points[5], concrete_cover_props.bottom),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)
    else:
        shape_builder.SetConcreteCoverLineStart(points[5], points[6], concrete_cover_props.bottom)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)
    else:
        set_end_length_intersection_side_5_6(points, shape_builder, concrete_cover_props.bottom)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_0_1_3_4_5_6_11_10(points, model_angles,
                                               shape_props, concrete_cover_props,
                                               start_length, end_length):
    """
                      /----------- 10
                     /
                    / 6
                   /
      ------      /
      |          /
      |         /
      |        /
   4  --------/ 5

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[0], points[1], concrete_cover_props.top),
                            (points[3], points[4], concrete_cover_props.top),
                            (points[4], points[5], concrete_cover_props.bottom),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (points[11], points[10], -concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)
    else:
        shape_builder.SetConcreteCoverLineStart(points[5], points[6], concrete_cover_props.bottom)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_10_11_12_0_3_4(points, model_angles,
                                            shape_props, concrete_cover_props,
                                            start_length, end_length):
    """
                    -- 10
                   /
                  /
                 /
                /
                | 4

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (points[12], points[0], concrete_cover_props.top),
                            (points[3], points[4], concrete_cover_props.top),
                            (concrete_cover_props.bottom)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_12_0(points, model_angles,
                                  shape_props, concrete_cover_props,
                                  start_length, end_length):
    """
                    12
                   /
                  /
                 /
                /
               0

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    del start_length
    del end_length

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[12], points[0], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    shape_builder.SetConcreteCoverLineStart(points[7], points[8], concrete_cover_props.top)
    shape_builder.SetConcreteCoverLineEnd(points[3], points[4], concrete_cover_props.top)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_5_6_7_8_10_11_12(points, model_angles,
                                              shape_props, concrete_cover_props,
                                              start_length, end_length):
    """
                  -----
                  |   |
                  |   /
                  |  /
              12  | /
                   /
                  /
                 /
                / 5

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (points[7], points[8], concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (points[11], points[12], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_12_11_8_9_10_11_12(points, model_angles,
                                                shape_props, concrete_cover_props,
                                                start_length, end_length):
    """
                        |--------- 10
                     12 |        |
                        ||-------- 9
                        ||
                         |

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[12], points[11], -concrete_cover_props.top),
                            (points[8], points[9], concrete_cover_props.top),
                            (points[9], points[10], concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (points[11], points[12], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_0_12_6_7_8_10_11(points, model_angles,
                                              shape_props, concrete_cover_props,
                                              start_length, end_length):
    """
              11 -----
                      |
                  /--- 7
                 /
                /
               /
              /
             /
            / 0

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[0], points[12], -concrete_cover_props.top),
                            (points[6], points[7], concrete_cover_props.bottom),
                            (points[7], points[8], concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_12_0_5_6(points, model_angles,
                                      shape_props, concrete_cover_props,
                                      start_length, end_length):
    """
                         /
                        /  /
                       /  /
                      /  /
                     /  /
                     './

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    line = AllplanGeo.Line2D(points[5], points[6])

    ortho_pnt = AllplanGeo.Point2D(AllplanGeo.TransformCoord.PointGlobal(line, AllplanGeo.Point2D(0, 1000)))

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[12], points[0], concrete_cover_props.top),
                            (ortho_pnt, points[5], concrete_cover_props.top),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_5_6_12_0(points, model_angles,
                                      shape_props, concrete_cover_props,
                                      start_length, end_length):
    """
                         /'.
                        /  /
                       /  /
                      /  /
                     /  /
                       /

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    line1 = AllplanGeo.Line2D(points[5], points[6])
    line2 = AllplanGeo.Line2D(points[7], points[8])

    err, off_line1 = AllplanGeo.Offset(concrete_cover_props.bottom, line1)

    if not GeometryValidate.offset(err):
        return

    result, i_pnt = AllplanGeo.IntersectionCalculusEx(off_line1, line2)

    if not GeometryValidate.intersection(result):
        return

    x_end = AllplanGeo.TransformCoord.PointLocal(line1, i_pnt).X

    ortho_pnt = AllplanGeo.Point2D(AllplanGeo.TransformCoord.PointGlobal(line1, AllplanGeo.Point2D(x_end, 1000)))

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[5], points[6], concrete_cover_props.bottom),
                            (i_pnt, ortho_pnt, concrete_cover_props.top),
                            (points[12], points[0], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_10_11_6_5(points, model_angles,
                                       shape_props, concrete_cover_props,
                                       start_length, end_length):
    """
                            /-------- 10
                           /
                          /
                         /
                        /
                       /
                      /
                     /
                    /
                  5/

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (points[6], points[5], -concrete_cover_props.bottom),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_8_9_10_11_12_0(points, model_angles,
                                            shape_props, concrete_cover_props,
                                            start_length, end_length):
    """
                       /------------- 10
                      /             |
                     /            --- 9
                    /
                   /  0

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[8], points[9], concrete_cover_props.top),
                            (points[9], points[10], concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (points[12], points[0], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_0_1_2_3(points, model_angles,
                                     shape_props, concrete_cover_props,
                                     start_length, end_length):
    """
              0
      ---------
      |   3
      --------

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[0], points[1], concrete_cover_props.top),
                            (points[1], points[2], concrete_cover_props.top),
                            (points[2], points[3], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)
    else:
        shape_builder.SetConcreteCoverLineStart(points[5], points[6], concrete_cover_props.bottom)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)
    else:
        shape_builder.SetConcreteCoverLineEnd(points[5], points[6], concrete_cover_props.bottom)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_stairs_shape_type_8_9_10_11_12(points, model_angles,
                                          shape_props, concrete_cover_props,
                                          start_length, end_length):
    """
                         -------- 10
                                 |
                         -------- 9

    Return: Bar shape in world coordinates

    Parameter:  points                  Geometry points of the stairs
                model_angles            Angles for the local to global shape transformation
                shape_props             Shape properties
                concrete_cover_props    Concrete cover at the sides
                start_length            Length of the start side
                end_length              Length of the end side
    """

    shape_builder = AllplanReinf.ReinforcementShapeBuilder()

    shape_builder.AddSides([(concrete_cover_props.top),
                            (points[8], points[9], concrete_cover_props.top),
                            (points[9], points[10], concrete_cover_props.top),
                            (points[10], points[11], concrete_cover_props.top),
                            (concrete_cover_props.top)])

    if start_length:
        shape_builder.SetSideLengthStart(start_length)

    if end_length:
        shape_builder.SetSideLengthEnd(end_length)

    shape = shape_builder.CreateShape(shape_props)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def create_cross_bar(stairs_width, model_angles, shape_props, concrete_cover):
    """
    Create the cross bar

    Return: Bar shape in world coordinates

    Parameter:  stairs_width        Stairs width
                model_angles        Angles for the local to global shape transformation
                shape_props         Shape properties
                concrete_cover      Concrete cover at the start and end of the cross bar
    """

    shape_pol = AllplanGeo.Polyline3D()

    shape_pol += AllplanGeo.Point3D(0, concrete_cover, 0)
    shape_pol += AllplanGeo.Point3D(0, stairs_width - concrete_cover, 0)

    shape = AllplanReinf.BendingShape(shape_pol, AllplanReinf.BendingRollerList(),
                                      shape_props.diameter, shape_props.steel_grade,
                                      shape_props.concrete_grade,
                                      AllplanReinf.BendingShapeType.LongitudinalBar)


    #----------------- Rotate the shape to the model

    if shape.IsValid() is True:
        shape.Rotate(model_angles)

    return shape


def set_end_length_intersection_side_5_6(points, shape_builder, concrete_cover):
    """
    Set the end length as side(5, 6) to the intersection point

    Parameter:  points          Geometry points
                shape_builder   Shape builder
                concrete_cover_props  Concrete cover
    """

    result, i_pnt1 = AllplanGeo.IntersectionCalculusEx(AllplanGeo.Line2D(points[5], points[6]),
                                                       AllplanGeo.Line2D(points[7], points[8]))

    if not GeometryValidate.intersection(result):
        return

    result, i_pnt2 = AllplanGeo.IntersectionCalculusEx(AllplanGeo.Line2D(points[5], points[6]),
                                                       AllplanGeo.Line2D(points[10], points[11]))

    if not GeometryValidate.intersection(result):
        return

    if i_pnt1.Y < i_pnt2.Y:
        shape_builder.SetConcreteCoverLineEnd(points[7], points[8], concrete_cover)
    else:
        shape_builder.SetConcreteCoverLineEnd(points[11], points[10], -concrete_cover)


def set_start_length_intersection_side_6_5(points, shape_builder, concrete_cover):
    """
    Set the end length as side(6, 5) to the intersection point

    Parameter:  points          Geometry points
                shape_builder   Shape builder
                concrete_cover_props  Concrete cover
    """

    result, i_pnt1 = AllplanGeo.IntersectionCalculusEx(AllplanGeo.Line2D(points[5], points[6]),
                                                       AllplanGeo.Line2D(points[7], points[8]))

    if not GeometryValidate.intersection(result):
        return

    result, i_pnt2 = AllplanGeo.IntersectionCalculusEx(AllplanGeo.Line2D(points[5], points[6]),
                                                       AllplanGeo.Line2D(points[10], points[11]))

    if not GeometryValidate.intersection(result):
        return

    if i_pnt1.Y < i_pnt2.Y:
        shape_builder.SetConcreteCoverLineStart(points[7], points[8], concrete_cover)
    else:
        shape_builder.SetConcreteCoverLineStart(points[11], points[10], -concrete_cover)
