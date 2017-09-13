"""
Implementation of the reinforcement shape properties class
"""

import NemAll_Python_Reinforcement as AllplanReinf

class ReinforcementShapeProperties():
    """
    Implementation of the reinforcement shape properties class
    """

    def __init__(self, diameter, bending_roller, steel_grade, concrete_grade,
                 bending_shape_type, mesh_type, mesh_bending_direction):
        """
        Set the properties of a reinforcement bar

        Parameter:  diameter                Bar diameter
                    bending_roller          Default bending roller (-1 = default for diameter)
                    steel_grade             Steel grade
                    concrete_grade          Concrete grade ((index of the global list starting from 0,
                                            -1 = use global value from the settings)
                    bending_shape_type      Bending shape type
                    mesh_type               Mesh type
                    mesh_bending_direction  Mesh bending direction
        """

        if mesh_type != "":
            mesh_data = AllplanReinf.ReinforcementShapeBuilder.GetMeshData(mesh_type)

            diameter = mesh_data.DiameterLongitudinal \
                      if mesh_bending_direction == AllplanReinf.MeshBendingDirection.LongitudinalBars \
                      else mesh_data.DiameterCross

        if bending_roller == -1:
            bending_roller = AllplanReinf.BendingRollerService.GetBendingRollerFactor(diameter, steel_grade,
                                                                                      concrete_grade, False)

        self.prop_diameter               = diameter
        self.prop_bending_roller         = bending_roller
        self.prop_steel_grade            = steel_grade
        self.prop_concrete_grade         = concrete_grade
        self.prop_bending_shape_type     = bending_shape_type
        self.prop_mesh_type              = mesh_type
        self.prop_mesh_bending_direction = mesh_bending_direction

    def __repr__(self):
        description =  '<%s>\n'\
            '   prop_diameter               = %s\n'\
            '   prop_bending_roller         = %s\n'\
            '   prop_steel_grade            = %s\n'\
            '   prop_concrete_grade         = %s\n'\
            '   prop_bending_shape_type     = %s\n'\
            '   prop_mesh_type              = %s\n'\
            '   prop_mesh_bending_direction = %s\n'\
            % (self.__class__.__name__,
               self.prop_diameter,
               self.prop_bending_roller,
               self.prop_steel_grade,
               self.prop_concrete_grade,
               self.prop_bending_shape_type,
               self.prop_mesh_type,
               self.prop_mesh_bending_direction)
        return description

    @staticmethod
    def rebar(diameter, bending_roller, steel_grade, concrete_grade, bending_shape_type):
        """
        Set the properties of a reinforcement bar

        Parameter:  diameter            Bar diameter
                    bending_roller      Default bending roller
                    steel_grade         Steel grade
                    concrete_grade      Concrete grade (index of the global list starting from 0,
                                        -1 = use global value from the settings)
                    bending_shape_type  Bending shape type
        """

        return ReinforcementShapeProperties(diameter, bending_roller, steel_grade, concrete_grade,
                                            bending_shape_type, "",
                                            AllplanReinf.MeshBendingDirection.LongitudinalBars)


    @staticmethod
    def mesh(mesh_type,  mesh_bending_direction, bending_roller, concrete_grade, bending_shape_type):

        """
        Set the properties of a reinforcement mesh

        Parameter:  mesh_type               Mesh type
                    mesh_bending_direction  Mesh bending direction
                    concrete_grade          Concrete grade (index of the global list starting from 0,
                                            -1 = use global value from the settings)
                    bending_roller          Default bending roller
                    bending_shape_type      Bending shape type
        """

        return ReinforcementShapeProperties(0, bending_roller, 4, concrete_grade,
                                            bending_shape_type, mesh_type, mesh_bending_direction)


    @property
    def diameter(self):
        """
        Get the mesh diameter
        """
        return self.prop_diameter


    @property
    def bending_roller(self):
        """
        Get the bending roller
        """
        return self.prop_bending_roller


    @property
    def steel_grade(self):
        """
        Get the steel grade
        """
        return self.prop_steel_grade


    @property
    def concrete_grade(self):
        """
        Get the concrete grade
        """
        return self.prop_concrete_grade


    @property
    def bending_shape_type(self):
        """
        Get the bending shape type
        """
        return self.prop_bending_shape_type


    @property
    def mesh_type(self):
        """
        Get the mesh type
        """
        return self.prop_mesh_type


    @property
    def mesh_bending_direction(self):
        """
        Get the mesh bending direction
        """
        return self.prop_mesh_bending_direction

