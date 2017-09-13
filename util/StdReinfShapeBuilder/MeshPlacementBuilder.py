"""
Implementation of the functions for the creation of the mesh placements
"""

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf


def create_mesh_placement_by_points(mesh_data,
                                    from_point,
                                    to_point,
                                    position,
                                    concrete_cover_left,
                                    concrete_cover_right,
                                    model_ele_list):
    """
    Create the mesh placement by placement points

    Parameter:  mesh_dat                List with tuples of mesh data (shape, placement length)
                from_point              Placement from point
                to_point                Placement to point
                position                First position number
                concrete_cover_left     Concrete cover at the left placement side
                concrete_cover_right    Concrete cover at the right placement side
                model_ele_list          List with the created placements
    """

    place_line = AllplanGeo.Line3D(from_point, to_point)

    rest_length = AllplanGeo.CalcLength(place_line) - concrete_cover_left - concrete_cover_right


    #----------------- check the place length

    real_length = []

    rest_index = -1

    for i, data in enumerate(mesh_data):
        region_length = data[1]

        rest_length -= region_length

        if not region_length:
            rest_index = i

        real_length.append(region_length)

    if rest_index != -1:
        real_length[rest_index] = rest_length


    #----------------- cut and create the placements

    x_start = concrete_cover_left

    for i, data in enumerate(mesh_data):
        shape = data[0]

        if shape.IsValid():
            mesh_type        = shape.GetMeshType()
            mesh_bending_dir = shape.GetMeshBendingDirection()

            mesh_length, mesh_width = AllplanReinf.ReinforcementShapeBuilder.GetMeshData(mesh_type).GetDimensions()

            cut_length = mesh_width if mesh_bending_dir == AllplanReinf.MeshBendingDirection.LongitudinalBars \
                else mesh_length

            place_length = real_length[i]

            while place_length > 0:
                if cut_length < place_length:
                    x_end = x_start + cut_length

                    place_length -= cut_length
                else:
                    x_end = x_start + place_length

                    place_length = 0

                start_pnt = AllplanGeo.TransformCoord.PointGlobal(place_line, x_start)
                end_pnt   = AllplanGeo.TransformCoord.PointGlobal(place_line, x_end)

                x_start = x_end

                mesh_shape = AllplanReinf.BendingShape(shape)

                mesh_shape.Move(AllplanGeo.Vector3D(start_pnt))

                dist_vec = AllplanGeo.Vector3D(start_pnt, end_pnt)

                model_ele_list.append(AllplanReinf.MeshPlacement(position, dist_vec, mesh_shape))

                position += 1

