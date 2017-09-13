"""
Implementation of the bar shape placement utilities

The BarShapePlacementUtil can be used to calculate the bar shape placement
according to multiple defined shapes.
"""


import NemAll_Python_Geometry as AllplanGeo
import GeometryValidate as GeometryValidate
import NemAll_Python_Reinforcement as AllplanReinf

from StdReinfShapeBuilder.BarPlacementUtil import get_placement_inside_bending_roller
from StdReinfShapeBuilder.BarPlacementUtil import get_placement_start_from_bending_roller
from StdReinfShapeBuilder.BarPlacementUtil import get_placement_end_from_bending_roller
from StdReinfShapeBuilder.BarPlacementUtil import get_placement_inside_side_intersection


class BarShapePlacementUtil:
    """
    Implementation of the bar shape placement utilities
    """

    def __init__(self):
        self.shapes = {}


    def add_shape(self, shape_id, shape):
        """
        Add a shape to the shape list

        Parameter:  shape_id    ID of the shape
                    shape       Shape
        """

        self.shapes[shape_id] = AllplanReinf.BendingShape(shape)


    def is_shape_created(self, shape_id):
        """
        Check for an existing shape by an shape_id

        Return: Shape exist: True/False

        Parameter:  shape_id    ID of the shape
        """

        return shape_id in self.shapes


    def get_side_length(self, shape_id, side_number):
        """
        Check for an existing shape by an shape_id

        Return: Shape exist: True/False

        Parameter:  shape_id    ID of the shape
                    side_number Number of the side
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        if side_number > shape_pol.Count():
            print("index error in get_side_length")
            return 0.

        return AllplanGeo.CalcLength(shape_pol.GetLine(side_number - 1))


    def get_placent_line_cover_from_side(self, shape_id, side_number, b_above_side):
        """
        Get the placement line cover from a shape side by side number

        Return: 3D placement line and the cover

        Parameter:  shape_id        ID of the shape
                    side_number     Number of the shape side
                    b_above_side    Cover above the side: True/False
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        rad = shape.GetDiameter() / 2.

        if b_above_side is False:
            rad = -rad

        return AllplanGeo.Line3D(shape_pol[side_number - 1], shape_pol[side_number]), rad


    def get_placement_from_bending_roller(self, shape_id, side_number, b_roller_start_point,
                                          placement_base_line, b_placment_start_point, placement_diameter,
                                          local_angles):
        """
        Get the placement cover from the bending roller of a defined side number

        Return: Local placement cover to a placement base line

        Parameter:  shape_id                ID of the shape
                    side_number             Number of the shape side
                    b_roller_start_point    True = roller at the start point / False = roller at the end point
                    placement_base_line     Base line of the placement
                    b_placment_start_point  True = placement start point / False = placement end point
                    placement_diameter      Bar diameter of the placement
                    local_angles            Rotation angles to get the local x/y coordinate system for the calculation
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        roller_base_side3d = AllplanGeo.Line3D(shape_pol[side_number - 1], shape_pol[side_number])

        roller_base_side = AllplanGeo.Line2D(AllplanGeo.Transform(roller_base_side3d,
                                                                  local_angles.get_rotation_matrix()))


        #----------------- get the local roller distance to the shape side

        if b_roller_start_point:
            bending_roller = shape.GetBendingRoller()[side_number - 2]

            cover = get_placement_start_from_bending_roller(shape, side_number, bending_roller,
                                                            roller_base_side, placement_diameter,
                                                            local_angles)

            cover_pnt = AllplanGeo.TransformCoord.PointGlobal(roller_base_side, cover)

        else:
            bending_roller = shape.GetBendingRoller()[side_number - 1]

            cover = get_placement_end_from_bending_roller(shape, side_number, bending_roller,
                                                          roller_base_side, placement_diameter,
                                                          local_angles)

            cover_pnt = AllplanGeo.TransformCoord.PointGlobal(roller_base_side,
                                                              AllplanGeo.CalcLength(roller_base_side) - cover)


        #----------------- get the cover to the placement base side

        if b_placment_start_point:
            return AllplanGeo.TransformCoord.PointLocal(placement_base_line, cover_pnt).X
        else:
            return AllplanGeo.CalcLength(placement_base_line) - \
                AllplanGeo.TransformCoord.PointLocal(placement_base_line, cover_pnt).X


    def get_placement_from_side_intersection(self, shape_id1, side_number1, b_above_side1,
                                             shape_id2, side_number2, b_above_side2,
                                             placement_base_line, b_placment_start_point, placement_diameter,
                                             local_angles):
        """
        Get the placement cover from the side intersection of two defined side numbers.

        Return: Local placement cover to a placement base line

        Parameter:  shape_id1               ID of the first shape
                    side_number1            Number of the first shape side
                    b_above_side1           Cover above the first side: True/False
                    shape_id2               ID of the second shape
                    side_number2            Number of the second shape side
                    b_above_side2           Cover above the second side: True/False
                    placement_base_line     Base line of the placement
                    b_placment_start_point  True = placement start point / False = placement end point
                    placement_diameter      Bar diameter of the placement
                    local_angles            Rotation angles to get the local x/y coordinate system for the calculation
        """

        place_pnt = get_placement_inside_side_intersection(self.shapes[shape_id1], side_number1,
                                                           b_above_side1,
                                                           self.shapes[shape_id2], side_number2,
                                                           b_above_side2,
                                                           placement_diameter,
                                                           local_angles)

        if b_placment_start_point:
            cover = AllplanGeo.TransformCoord.PointLocal(placement_base_line, place_pnt).X - placement_diameter / 2
        else:
            cover = AllplanGeo.CalcLength(placement_base_line) - AllplanGeo.TransformCoord.PointLocal(
                placement_base_line, place_pnt).X - placement_diameter / 2

        return cover


    def get_placement_in_side_intersection(self, shape_id1, side_number1, b_above_side1,
                                           shape_id2, side_number2, b_above_side2,
                                           placement_diameter, local_angles):
        """
        Get the placement point from the side intersection of two defined side numbers.

        Return: Local placement cover to a placement base line

        Parameter:  shape_id1               ID of the first shape
                    side_number1            Number of the first shape side
                    b_above_side1           Cover above the first side: True/False
                    shape_id2               ID of the second shape
                    side_number2            Number of the second shape side
                    b_above_side2           Cover above the second side: True/False
                    placement_diameter      Bar diameter of the placement
                    local_angles            Rotation angles to get the local x/y coordinate system for the calculation
        """

        return get_placement_inside_side_intersection(self.shapes[shape_id1], side_number1,
                                                      b_above_side1,
                                                      self.shapes[shape_id2], side_number2,
                                                      b_above_side2,
                                                      placement_diameter,
                                                      local_angles)

    def get_placement_at_shape_side(self, shape_id, side_number, ref_pnt_fac, b_above_side,
                                    placement_diameter,
                                    local_angles):
        """
        Calculate the local placement line at a shape side inside the local X/Y coordinate system of the shapes

        Return: tuple of (local 2D placement line started by a reference point and left and right limited by
                          the next bending roller or side intersection,
                          cover at the shape side,
                          cover at the start of the line,
                          cover at the end of the line)

        Parameter:  shape_id                ID of the shape
                    side_number             Number of the shape side
                    ref_pnt_fac             Factor for the reference point calculation
                                            (-1 = at the side from left to right)
                    b_above_side            Cover above the side: True/False
                    placement_diameter      Bar diameter of the placement
                    local_angles            Rotation angles to get the local x/y coordinate system for the calculation
        """

        shape_cover_line, concrete_cover = self.get_placent_line_cover_from_side(shape_id, side_number, b_above_side)

        del shape_cover_line

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        placement_base_line3d = AllplanGeo.Line3D(shape_pol[side_number - 1], shape_pol[side_number])

        placement_base_line = AllplanGeo.Line2D(AllplanGeo.Transform(placement_base_line3d,
                                                                     local_angles.get_rotation_matrix()))

        if side_number == 1:
            placement_cover_left = 0
        else:
            placement_cover_left =  \
                self.get_placement_from_bending_roller(shape_id, side_number, True, placement_base_line, True,
                                                       placement_diameter, local_angles)

        if side_number == self.shapes[shape_id].GetShapePolyline().Count() - 1:
            placement_cover_right = 0
        else:
            placement_cover_right = \
                self.get_placement_from_bending_roller(shape_id, side_number, False, placement_base_line, False,
                                                       placement_diameter, local_angles)


        #----------------- Check the intersections

        if ref_pnt_fac != -1:
            dist = placement_diameter / 2. if b_above_side else -placement_diameter / 2.

            err, intersect_line = AllplanGeo.Offset(dist, placement_base_line)

            if not GeometryValidate.offset(err):
                return (AllplanGeo.Line2D(), 0, 0)

            side_length = AllplanGeo.CalcLength(placement_base_line)

            x_ref = side_length * ref_pnt_fac

            for shape_id_iter, shape_iter in self.shapes.items():
                if shape_id_iter != shape_id:
                    polyline = shape_iter.GetShapePolyline()

                    for i_side in range(0, polyline.Count() - 1):
                        if i_side + 1 >= polyline.Count():
                            print("index error in get_placement_at_shape_side")
                            break

                        side_line_3d = polyline.GetLine(i_side)

                        side_line = AllplanGeo.Line2D(AllplanGeo.Transform(side_line_3d,
                                                                           local_angles.get_rotation_matrix()))

                        result, i_pnt = AllplanGeo.IntersectionCalculus(intersect_line, side_line)

                        if result:
                            x_loc = AllplanGeo.TransformCoord.PointLocal(placement_base_line, i_pnt).X


                            #----------------- new left cover

                            if x_loc < x_ref  and  x_loc > placement_cover_left:
                                y_start = AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                               side_line.StartPoint).Y
                                y_end = AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line.EndPoint).Y

                                b_roller_pnt_start = False
                                b_roller_pnt_end = False


                                #----- check for bending roller at the end point of the line before intersection line

                                if i_side > 0  and abs(y_start) < placement_diameter:
                                    side_line3d_before = polyline.GetLine(i_side - 1)

                                    side_line_before = AllplanGeo.Line2D(AllplanGeo.Transform(
                                        side_line3d_before,
                                        local_angles.get_rotation_matrix()))

                                    if AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                            side_line_before.StartPoint).X > \
                                        AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line_before.EndPoint).X:
                                        b_roller_pnt_end = True


                                #----- check for bending roller at the start point of the line after intersection line

                                if i_side < polyline.Count() - 2  and abs(y_end) < placement_diameter:
                                    if i_side + 2 >= polyline.Count():
                                        print("index error in get_placement_at_shape_side")
                                        break

                                    side_line3d_after = polyline.GetLine(i_side + 1)

                                    side_line_after = AllplanGeo.Line2D(AllplanGeo.Transform(
                                        side_line3d_after,
                                        local_angles.get_rotation_matrix()))

                                    if AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                            side_line_after.StartPoint).X < \
                                        AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line_after.EndPoint).X:
                                        b_roller_pnt_start = True


                                #----------------- mew cover from bending roller or intersection

                                if b_roller_pnt_start:
                                    placement_cover_left = self.get_placement_from_bending_roller(
                                        shape_id_iter, i_side + 2, True, placement_base_line, True, placement_diameter,
                                        local_angles)

                                elif b_roller_pnt_end:
                                    placement_cover_left = self.get_placement_from_bending_roller(
                                        shape_id_iter, i_side, False, placement_base_line, True, placement_diameter,
                                        local_angles)

                                else:
                                    place_pnt = get_placement_inside_side_intersection(
                                        shape, side_number, b_above_side,
                                        shape_iter, i_side + 1, y_start > 0., placement_diameter,
                                        local_angles)

                                    placement_cover_left = AllplanGeo.TransformCoord.PointLocal(
                                        placement_base_line, place_pnt).X - placement_diameter / 2


                            #----------------- new right cover

                            elif x_loc > x_ref  and x_loc < side_length - placement_cover_right:
                                y_start = AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                               side_line.StartPoint).Y
                                y_end = AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line.EndPoint).Y

                                b_roller_pnt_start = False
                                b_roller_pnt_end = False


                                #-------- check for bending roller at the end point of the line before intersection line

                                if i_side > 0  and abs(y_start) < placement_diameter:
                                    side_line3d_before = polyline.GetLine(i_side - 1)

                                    side_line_before = AllplanGeo.Line2D(AllplanGeo.Transform(
                                        side_line3d_before,
                                        local_angles.get_rotation_matrix()))

                                    if AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                            side_line_before.StartPoint).X < \
                                        AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line_before.EndPoint).X:
                                        b_roller_pnt_end = True


                                #----- check for bending roller at the start point of the line after intersection line

                                if i_side < polyline.Count() - 2  and abs(y_end) < placement_diameter:
                                    side_line3d_after = polyline.GetLine(i_side)

                                    side_line_after = AllplanGeo.Line2D(AllplanGeo.Transform(
                                        side_line3d_after,
                                        local_angles.get_rotation_matrix()))

                                    if AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                            side_line_after.StartPoint).X > \
                                        AllplanGeo.TransformCoord.PointLocal(placement_base_line,
                                                                             side_line_after.EndPoint).X:
                                        b_roller_pnt_start = True


                                #----------------- mew cover from bending roller or intersection

                                if b_roller_pnt_start:
                                    placement_cover_right = self.get_placement_from_bending_roller(
                                        shape_id_iter, i_side + 2, True, placement_base_line, False, placement_diameter,
                                        local_angles)

                                elif b_roller_pnt_end:
                                    placement_cover_right = self.get_placement_from_bending_roller(
                                        shape_id_iter, i_side, False, placement_base_line, False, placement_diameter,
                                        local_angles)
                                else:
                                    place_pnt = get_placement_inside_side_intersection(
                                        shape, side_number, b_above_side,
                                        shape_iter, i_side + 1, y_start < 0., placement_diameter,
                                        local_angles)

                                    placement_cover_right = side_length - AllplanGeo.TransformCoord.PointLocal(
                                        placement_base_line, place_pnt).X - placement_diameter / 2


        #----------------- calculate the placement line

        if concrete_cover > 0.:
            concrete_cover += placement_diameter / 2

        elif concrete_cover < 0.:
            concrete_cover -= placement_diameter / 2

        err, placement_line_local = AllplanGeo.Offset(concrete_cover, placement_base_line)

        if not GeometryValidate.offset(err):
            return (AllplanGeo.Line2D(), 0, 0)

        return (placement_line_local, placement_cover_left, placement_cover_right)


    def get_placement_in_corner(self, shape_id, corner_number,
                                placement_diameter,
                                local_angles):
        """
        Calculate the local placement point inside the local X/Y coordinate system of the shape corner

        Return: local position of placement start

        Parameter:  shape_id                ID of the shape
                    corner_number           Number of the shape corner
                    placement_diameter      Bar diameter of the placement
                    local_angles            Rotation angles to get the local x/y coordinate system for the calculation
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        if corner_number > shape_pol.Count():
            return AllplanGeo.Point3D()

        placement_base_line3d = AllplanGeo.Line3D(shape_pol[corner_number - 1], shape_pol[corner_number])

        AllplanGeo.Line2D(AllplanGeo.Transform(placement_base_line3d, local_angles.get_rotation_matrix()))

        bending_roller = shape.GetBendingRoller()

        if corner_number > len(bending_roller):
            return AllplanGeo.Point3D()

        bending_roller = bending_roller[corner_number - 1]

        return get_placement_inside_bending_roller(shape, corner_number, bending_roller, placement_diameter,
                                                   local_angles)


    def get_placement_in_side_corners(self, shape_id, side_number,
                                      placement_diameter,
                                      local_angles):
        """
        Calculate the local placement line from the left to the right side corner inside
        the local X/Y coordinate system of the shapes

        Return: tuple of (local 2D placement line from the left bending roller bar position
                          to the right bending roller bar position,
                          cover at the start of the line,
                          cover at the end of the line)

        Parameter:  shape_id                ID of the shape
                    side_number             Number of the shape side
                    placement_diameter      Bar diameter of the placement
                    local_angles            Rotation angles to get the local x/y coordinate system for the calculation
        """

        shape = self.shapes[shape_id]

        shape_pol = shape.GetShapePolyline()

        bending_roller_list = shape.GetBendingRoller()

        if side_number - 1 >= len(bending_roller_list):
            return (AllplanGeo.Line2D(), 0, 0)

        bending_roller = bending_roller_list[side_number - 2]

        corner_pnt1 = get_placement_inside_bending_roller(shape, side_number - 1, bending_roller, placement_diameter,
                                                          local_angles)

        bending_roller = bending_roller_list[side_number - 1]

        corner_pnt2 = get_placement_inside_bending_roller(shape, side_number, bending_roller, placement_diameter,
                                                          local_angles)

        place_line_axis = AllplanGeo.Line2D(AllplanGeo.Point2D(corner_pnt1), AllplanGeo.Point2D(corner_pnt2))

        place_line_axis.TrimStart(-placement_diameter / 2.)
        place_line_axis.TrimEnd(-placement_diameter / 2.)

        return (place_line_axis, 0, 0)


    def get_placement(self, reinf_def, param_dict, diameter,
                      local_angles):
        """
        Calculate the local placement line inside the local X/Y coordinate system of the shapes

        Return: tuple of (local 2D placement line,
                          cover at the start of the line,
                          cover at the end of the line)

        Parameter:  reinf_def           Reinforcement definition
                    param_dict          Parameter dictionary
                    local_angles        Rotation angles to get the local x/y coordinate system for the calculation
        """

        diameter_str =  reinf_def.get_attribute("Diameter")

        angle_str = ",local_angles"

        param_dict["local_angles"] = local_angles


        #----------------- placement in the shape corner, at the shape

        placement =  reinf_def.get_attribute("Placement")

        if placement:
            if placement.find("in_corner") != -1:
                placement = "ShapePlaceUtil.get_placement_" + placement

                placement = placement.replace(")", "," + diameter_str + angle_str + ")")

                corner_pnt = AllplanGeo.Point2D(eval(placement, param_dict))

                return (AllplanGeo.Line2D(corner_pnt, corner_pnt), 0, 0)

            elif placement.find("in_side_intersection") != -1:
                placement = "ShapePlaceUtil.get_placement_" + placement

                placement = placement.replace(")", "," + diameter_str + angle_str + ")")

                corner_pnt = AllplanGeo.Point2D(eval(placement, param_dict))

                return (AllplanGeo.Line2D(corner_pnt, corner_pnt), 0, 0)


            #----------------- placement at the shape side

            else:
                placement = "ShapePlaceUtil.get_placement_" + placement

                placement = placement.replace(")", "," + diameter_str + angle_str + ")")

                return eval(placement, param_dict)


        #--------------- get the single placement cover values

        else:
            shape_cover_line3d, concrete_cover = eval(
                "ShapePlaceUtil.get_placent_line_cover_" + reinf_def.get_attribute("ConcreteCoverShape"), param_dict)

            shape_cover_line = AllplanGeo.Line2D(AllplanGeo.Transform(shape_cover_line3d,
                                                                      local_angles.get_rotation_matrix()))

            placement_cover_left_str  = reinf_def.get_attribute("PlacementCoverLeft")
            placement_cover_right_str = reinf_def.get_attribute("PlacementCoverRight")

            param_dict["ShapeCoverLine"] = shape_cover_line

            if placement_cover_left_str.find("from") != -1:
                placement_cover_left_str = placement_cover_left_str.replace(
                    ")", ",ShapeCoverLine,True," + diameter_str + angle_str + ")")

                placement_cover_left_str = "ShapePlaceUtil.get_placement_" + placement_cover_left_str

                placement_cover_left = eval(placement_cover_left_str, param_dict)
            else:
                placement_cover_left = eval(placement_cover_left_str, param_dict)

            if placement_cover_right_str.find("from") != -1:
                placement_cover_right_str = placement_cover_right_str.replace(
                    ")", ",ShapeCoverLine,False," + diameter_str + angle_str + ")")

                placement_cover_right_str = "ShapePlaceUtil.get_placement_" + placement_cover_right_str

                placement_cover_right = eval(placement_cover_right_str, param_dict)
            else:
                placement_cover_right = eval(placement_cover_right_str, param_dict)


        #----------------- calculate the placement line

        if concrete_cover > 0.:
            concrete_cover += diameter / 2

        elif concrete_cover < 0.:
            concrete_cover -= diameter / 2

        err, placement_line_local = AllplanGeo.Offset(concrete_cover,
                                                      AllplanGeo.Line2D(shape_cover_line.StartPoint,
                                                                        shape_cover_line.EndPoint))

        if not GeometryValidate.offset(err):
            return (AllplanGeo.Line2D(), 0, 0)

        return (placement_line_local, placement_cover_left, placement_cover_right)
