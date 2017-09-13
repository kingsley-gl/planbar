"""
Implementation of the linear placement bar placement builder
"""
from enum import IntEnum

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf

class StartEndPlacementRule(IntEnum):
    """
    Class with the definition of the handle input directions

    The handle direction can be used to set the coordinate input direction for the handle modification

    Horst Hohmann
    25.06.2015
    """

    AdditionalCover      = 1
    AdditionalCoverLeft  = 2
    AdditionalCoverRight = 3
    AdaptDistance        = 4


def create_linear_bar_placement_from_to_by_dist(position,
                                                shape,
                                                from_point,
                                                to_point,
                                                concrete_cover_left,
                                                concrete_cover_right,
                                                bar_distance,
                                                start_end_rule=StartEndPlacementRule.AdditionalCover,
                                                global_move=True):
    """
    Create a linear placement defined by two points and a bar distance

    Return: Bar placement

    Parameter:  position                Position number
                shape                   Shape for the placement
                from_point              Placement from point
                to_point                Placement to point
                concrete_cover_left     Concrete cover at the left placement side
                concrete_cover_right    Concrete cover at the right placement side
                bar_distance            Bar distance
                start_end_rule          Rule for the adaption of the distance / start-end cover
                global_move             True: move the shape to the from_point of the placement
                                              (e.g. if the shape is created in a local 0/0/0 coordinate system)
                                        False: the shape is already placed at the from_point
    """
    dist_vec = AllplanGeo.Vector3D(from_point, to_point)

    place_length = dist_vec.GetLength() - shape.GetDiameter() - concrete_cover_left - concrete_cover_right

    if place_length <= 0:
        return AllplanReinf.BarPlacement(position, 0, dist_vec, AllplanGeo.Point3D(), AllplanGeo.Point3D(), shape)

    count = int(place_length / bar_distance)

    add_cover = 0.


    #------------------ small difference will be adapted

    if (place_length - count * bar_distance) > bar_distance - 1:
        count += 1


    #------------------ adapt the concrete cover or the distance

    else:
        if start_end_rule == StartEndPlacementRule.AdditionalCover:
            add_cover = (place_length - count * bar_distance) / 2.

        elif start_end_rule == StartEndPlacementRule.AdditionalCoverLeft:
            add_cover = place_length - count * bar_distance

        elif start_end_rule == StartEndPlacementRule.AdditionalCoverRight:
            add_cover = 0.

        else:
            count = count + 1
            bar_distance = place_length / count

    start_point = AllplanGeo.TransformCoord.PointGlobal(AllplanGeo.Line3D(from_point, to_point),
                                                        concrete_cover_left + shape.GetDiameter() / 2. + add_cover)

    if global_move is False:
        start_point -= from_point

    start_shape = AllplanReinf.BendingShape(shape)

    start_shape.Move(AllplanGeo.Vector3D(start_point))

    dist_vec.Normalize(bar_distance)

    return AllplanReinf.BarPlacement(position, count + 1, dist_vec, start_point,
                                     start_point + dist_vec * count, start_shape)


def create_linear_bar_placement_from_to_by_count(position,
                                                 shape,
                                                 from_point,
                                                 to_point,
                                                 concrete_cover_left,
                                                 concrete_cover_right,
                                                 bar_count,
                                                 global_move=True,
                                                 remove_count_left=0,
                                                 remove_count_right=0):
    """
    Create a linear placement defined by two points and a bar count

    Return: Bar placement

    Parameter:  position                Position number
                shape                   Shape for the placement
                from_point              Placement from point
                to_point                Placement to point
                concrete_cover_left     Concrete cover at the left placement side
                concrete_cover_right    Concrete cover at the right placement side
                bar_count               Bar count
                global_move             True: move the shape to the from_point of the placement
                                              (e.g. if the shape is created in a local 0/0/0 coordinate system)
                                        False: the shape is already placed at the from_point
                remove_count_left       Remove ... bars at the left side of the placement
                remove_count_right      Remove ... bars at the right side of the placement
    """


    dist_vec = AllplanGeo.Vector3D(from_point, to_point)

    place_length = dist_vec.GetLength() - shape.GetDiameter() - concrete_cover_left - concrete_cover_right

    bar_distance = place_length if bar_count == 1 else place_length / (bar_count - 1)

    start_point = AllplanGeo.TransformCoord.PointGlobal(AllplanGeo.Line3D(from_point, to_point),
                                                        concrete_cover_left + shape.GetDiameter() / 2.)

    if global_move is False:
        start_point -= from_point

    start_shape = AllplanReinf.BendingShape(shape)

    start_shape.Move(AllplanGeo.Vector3D(start_point))

    dist_vec = AllplanGeo.Vector3D(from_point, to_point)

    if dist_vec.IsZero():
        return AllplanReinf.BarPlacement()

    dist_vec.Normalize(bar_distance)

    if remove_count_left:
        move_vec = dist_vec * float(remove_count_left)

        start_shape.Move(move_vec)

    if bar_count == 1:
        return AllplanReinf.BarPlacement(position,
                                         bar_count - remove_count_left - remove_count_right,
                                         dist_vec,
                                         start_point + dist_vec / 2,start_point + dist_vec / 2,
                                         start_shape)

    return AllplanReinf.BarPlacement(position,
                                     bar_count - remove_count_left - remove_count_right,
                                     dist_vec,
                                     start_point,start_point + dist_vec * (bar_count - 1),
                                     start_shape)


def create_linear_bar_placement_from_by_dist_count(position, shape, from_point, direction_point,
                                                   concrete_cover, bar_distance, bar_count,
                                                   global_move=True):
    """
    Create a linear placement defined by a from point, a direction point, a bar count and a distance

    Return: Bar placement

    Parameter:  position                Position number
                shape                   Shape for the placement
                from_point              Placement from point
                direction_point         Direction point
                concrete_cover          Concrete cover
                bar_distance            Bar distance
                bar_count               Bar count
    """

    start_point = AllplanGeo.TransformCoord.PointGlobal(AllplanGeo.Line3D(from_point, direction_point),
                                                        concrete_cover + shape.GetDiameter() / 2.)

    if global_move is False:
        start_point -= from_point

    start_shape = AllplanReinf.BendingShape(shape)

    start_shape.Move(AllplanGeo.Vector3D(start_point))

    dist_vec = AllplanGeo.Vector3D(from_point, direction_point)

    dist_vec.Normalize(bar_distance)

    end_point = start_point + dist_vec * (bar_count - 1)

    return AllplanReinf.BarPlacement(position, bar_count, dist_vec, start_point, end_point, start_shape)


def calculate_length_of_regions(value_list,
                                from_point,
                                to_point,
                                concrete_cover_left,
                                concrete_cover_right):
    """
    Create the real region length of a placement

    Return: Bar placement ploints as list of tuples (start point, end point)

    Parameter:  value_list              list with the tuple (length, distance, diameter)
                from_point              Placement from point
                to_point                Placement to point
                concrete_cover_left     Concrete cover at the left placement side
                concrete_cover_right    Concrete cover at the right placement side
    """

    value_count = len(value_list)

    dist_vec = AllplanGeo.Vector3D(from_point, to_point)

    place_length = dist_vec.GetLength() - value_list[0][2] - value_list[value_count - 1][2] -   \
                   concrete_cover_left - concrete_cover_right


    #------------------ adapt the length to the distance

    real_length = []
    dist_next = []

    rest_index = -1

    length_sum = 0

    for i in range(value_count):
        value = value_list[i]

        if value[0]:
            length = check_placement_length_by_distance(value[0], value[1])

            length_sum += length

            real_length.append(length)
        else:
            real_length.append(0)

            rest_index = i


    #------------------ get the distance to the next region

    use_value_next = True

    for i in range(value_count - 1):
        value = value_list[i]
        value_next = value_list[i + 1]

        if not value[0]  or  not use_value_next:
            use_value_next = False
            dist_next.append(value[1])
        else:
            dist_next.append(value_next[1])

        length_sum += dist_next[i]


    #------------------ Calculate and set the rest

    real_length[rest_index] = place_length - length_sum


    #------------------ Create the real length at the left side

    x_start = concrete_cover_left

    place_line = AllplanGeo.Line3D(from_point, to_point)

    place_points = []

    for i in range(value_count):
        if i:
            x_start += dist_next[i - 1] - value[2] / 2

        value = value_list[i]

        x_end = x_start + real_length[i] + value[2]

        place_points.append((AllplanGeo.TransformCoord.PointGlobal(place_line, x_start),
                             AllplanGeo.TransformCoord.PointGlobal(place_line, x_end)))

        x_start = x_end - value[2] / 2.

    return place_points


def check_placement_length_by_distance(length, distance):
    """
    Helper function for the length checking of a placement

    Return: adpapted length of the placement

    Parameter:  length      length of the placement
                distance    distance of the placement
    """

    count = int(length / distance)

    if length - float(count * distance) > 0.:
        count += 1

    return float(count * distance)





