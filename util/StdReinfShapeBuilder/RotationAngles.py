"""
Implementation of the model angles class
"""
import NemAll_Python_Geometry as AllplanGeo


class RotationAngles():
    """
    Implementation of the rotation angles class

    The rotation angles are used for the transformation of the reinforcement shape
    from/to the local/global coordinate system
    """

    def __init__(self, angle_x, angle_y, angle_z):
        """
        Set the model angles

        Parameter:  angle_x    Rotation (degree) around the local x axis to
                               get the global/local x/y/z coordinates of the shape
                    angle_y    Rotation (degree) around the local y axis to
                               get the global/local x/y/z coordinates of the shape
                    angle_z    Rotation (degree) around the local z axis to
                               get the global/local x/y/z coordinates of the shape
        """

        self.prop_angle_x = angle_x
        self.prop_angle_y = angle_y
        self.prop_angle_z = angle_z

    @property
    def angle_x(self):
        """
        Get the x angle
        """
        return self.prop_angle_x


    @property
    def angle_y(self):
        """
        Get the y angle
        """
        return self.prop_angle_y


    @property
    def angle_z(self):
        """
        Get the y angle
        """
        return self.prop_angle_z


    def get_rotation_matrix(self):
        """
        Get the rotation matrix

        Return: rotation matrix

        """
        rot_mat = AllplanGeo.Matrix3D()
        rot_angle = AllplanGeo.Angle()

        rot_angle.SetDeg(self.angle_x)

        rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(1000, 0, 0)), rot_angle)

        rot_angle.SetDeg(self.angle_y)

        rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(0, 1000, 0)), rot_angle)

        rot_angle.SetDeg(self.angle_z)

        rot_mat.Rotation(AllplanGeo.Line3D(AllplanGeo.Point3D(), AllplanGeo.Point3D(0, 0, 1000)), rot_angle)

        return rot_mat

    def change_rotation(self):
        """
        Get RotationAngles with the changed direction

        Return: rotation matrix

        """

        return RotationAngles(-self.angle_x, -self.angle_y, -self.angle_z)

    def __repr__(self):
        description =  '<%s>\n'\
            '   x-angle = %s\n'\
            '   y-angle = %s\n'\
            '   z-angle = %s\n'\
            % (self.__class__.__name__,
               self.angle_x,
               self.angle_y,
               self.angle_z)
        return description
