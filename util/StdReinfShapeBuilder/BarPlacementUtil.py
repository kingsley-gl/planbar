"""
Implementation of the bar placement utilities
"""


import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import GeometryValidate as GeometryValidate


def get_placement_start_from_bending_roller(shape, side_number, bending_roller,
                                            base_line, placement_diameter,
                                            local_angles):
    """
    Calculate the placement start point from the bending roller point at the start of a shape side.
    The point is local to the start of the base line

       |
       |
        \
         --------

    S----x----------------  base line
     --->

    Return: local position of placement start

    Parameter:  shape               Reinforcement shape
                side_number         Number of the shape side with the placement (starting from 1)
                bending_roller      Bending roller
                base_line           Geometry base line of the placement
                placement_diameter  Bar diameter of the placement
                local_angles        Rotation angles to get the local x/y coordinate system for the calculation
    """

    local_shape = AllplanReinf.BendingShape(shape)

    local_shape.Rotate(local_angles)

    bar_poly = local_shape.GetShapePolyline()

    line1 = AllplanGeo.Line2D(bar_poly.GetLine(side_number - 2))
    line2 = AllplanGeo.Line2D(bar_poly.GetLine(side_number - 1))

    dist = (bending_roller / 2. + 0.5) * shape.GetDiameter()

    if AllplanGeo.TransformCoord.PointLocal(line2, line1.StartPoint).Y < 0.:
        dist *= -1

    err, par_line_1 = AllplanGeo.Offset(dist, line1)

    if not GeometryValidate.offset(err):
        return 0

    err, par_line_2 = AllplanGeo.Offset(dist, line2)

    if not GeometryValidate.offset(err):
        return 0

    result, roller_pnt = AllplanGeo.IntersectionCalculusEx(par_line_1, par_line_2)

    if not GeometryValidate.intersection(result):
        return 0

    return AllplanGeo.TransformCoord.PointLocal(base_line, roller_pnt).X - placement_diameter / 2.


def get_placement_end_from_bending_roller(shape, side_number, bending_roller,
                                          base_line, placement_diameter,
                                          local_angles):
    """
    Calculate the placement start point from the bending roller point at the end of a shape side.
    The point is local to the end of the base line

                      |
                      |
                     /
             --------

    ----------------x----E  base line
                     <---

    Return: local position of placement end from E to x

    Parameter:  shape               Reinforcement shape
                side_number         Number of the shape side with the placement (starting from 1)
                bending_roller      Bending roller
                base_line           Geometry base line of the placement
                placement_diameter  Bar diameter of the placement
                local_angles        Rotation angles to get the local x/y coordinate system for the calculation
    """

    local_shape = AllplanReinf.BendingShape(shape)

    local_shape.Rotate(local_angles)

    bar_poly = local_shape.GetShapePolyline()

    if side_number + 1 >= bar_poly.Count():
        print("index error in get_placement_end_from_bending_roller")
        return AllplanGeo.Point3D()

    line1 = AllplanGeo.Line2D(bar_poly.GetLine(side_number - 1))
    line2 = AllplanGeo.Line2D(bar_poly.GetLine(side_number))

    dist = (bending_roller / 2. + 0.5) * shape.GetDiameter()

    if AllplanGeo.TransformCoord.PointLocal(line1, line2.EndPoint).Y < 0.:
        dist *= -1

    err, par_line_1 = AllplanGeo.Offset(dist, line1)

    if not GeometryValidate.offset(err):
        return 0

    err, par_line_2 = AllplanGeo.Offset(dist, line2)

    if not GeometryValidate.offset(err):
        return 0

    result, roller_pnt = AllplanGeo.IntersectionCalculusEx(par_line_1, par_line_2)

    if not GeometryValidate.intersection(result):
        return 0

    return AllplanGeo.CalcLength(base_line) - \
           AllplanGeo.TransformCoord.PointLocal(base_line, roller_pnt).X - placement_diameter / 2.


def get_placement_inside_bending_roller(shape, corner_number, bending_roller, placement_diameter,
                                        local_angles, global_point=False):
    """
    Calculate the position of a placement inside the bending roller

       |
       |    X
        \
         --------

    Return: local position of placement start as Point3D

    Parameter:  shape               Reinforcement shape
                corner_number       Number of the shape corner with the placement (starting from 1)
                bending_roller      Bending roller
                placement_diameter  Bar diameter of the placement
                local_angles        Rotation angles to get the local x/y coordinate system for the calculation
    """

    local_shape = AllplanReinf.BendingShape(shape)

    local_shape.Rotate(local_angles)

    bar_poly = local_shape.GetShapePolyline()

    if corner_number + 1 >= bar_poly.Count():
        print("index error in get_placement_inside_bending_roller")
        return AllplanGeo.Point3D()

    line1 = AllplanGeo.Line2D(bar_poly.GetLine(corner_number - 1))
    line2 = AllplanGeo.Line2D(bar_poly.GetLine(corner_number))

    rad = (bending_roller / 2. + 0.5) * shape.GetDiameter()

    fillet = AllplanGeo.FilletCalculus2D(line1, line2, rad)

    arc = fillet.GetNearest(line1.EndPoint)

    arc_len = AllplanGeo.CalcLength(arc)

    center = AllplanGeo.TransformCoord.PointGlobal(arc, arc_len / 2)

    line = AllplanGeo.Line2D(AllplanGeo.Point2D(center), arc.Center)

    corner_pnt = AllplanGeo.TransformCoord.PointGlobal(line, shape.GetDiameter() / 2 + placement_diameter / 2)

    if global_point:
        global_angles = local_angles.change_rotation()

        corner_pnt = AllplanGeo.Transform(corner_pnt, global_angles.get_rotation_matrix())

    return corner_pnt


def get_placement_inside_side_intersection(shape1, side_number1, above_side1,
                                           shape2, side_number2, above_side2,
                                           placement_diameter,
                                           local_angles, global_point=False):
    """
    Calculate the position of a placement inside the intersection of two shape sides

    Return: local placement point as Point2D

    Parameter:  shape1              First reinforcement shape
                side_number1        Number of the first shape side with the placement (starting from 1)
                above_side1,        First placement direction above the side: True/False
                shape2              Second reinforcement shape
                side_number2        Number of the second shape side with the placement (starting from 1)
                above_side2,        Second placement direction above the side: True/False
                placement_diameter  Bar diameter of the placement
                local_angles        Rotation angles to get the local x/y coordinate system for the calculation
    """

    local_shape1 = AllplanReinf.BendingShape(shape1)
    local_shape2 = AllplanReinf.BendingShape(shape2)

    local_shape1.Rotate(local_angles)
    local_shape2.Rotate(local_angles)

    bar_poly1 = local_shape1.GetShapePolyline()
    bar_poly2 = local_shape2.GetShapePolyline()

    rad = placement_diameter / 2.

    direction1 = 1 if above_side1 else -1
    direction2 = 1 if above_side2 else -1

    if side_number1 >= bar_poly1.Count():
        print("index error in get_placement_inside_side_intersection 1:")
        return AllplanGeo.Point3D()

    err, par_line_1 = AllplanGeo.Offset((shape1.GetDiameter() / 2. + rad) * direction1,
                                        AllplanGeo.Line2D(bar_poly1.GetLine(side_number1 - 1)))

    if not GeometryValidate.offset(err):
        return AllplanGeo.Point2D()

    if side_number2 >= bar_poly2.Count():
        print("index error in get_placement_inside_side_intersection 1:")
        return AllplanGeo.Point3D()

    err, par_line_2 = AllplanGeo.Offset((shape2.GetDiameter() / 2. + rad) * direction2,
                                        AllplanGeo.Line2D(bar_poly2.GetLine(side_number2 - 1)))

    if not GeometryValidate.offset(err):
        return AllplanGeo.Point2D()

    result, place_pnt = AllplanGeo.IntersectionCalculusEx(par_line_1, par_line_2)

    if not GeometryValidate.intersection(result):
        return AllplanGeo.Point2D()

    if global_point:
        global_angles = local_angles.change_rotation()

        place_pnt = AllplanGeo.Transform(AllplanGeo.Point3D(place_pnt), global_angles.get_rotation_matrix())

    return place_pnt
