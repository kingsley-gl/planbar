"""
Implementation of the concrete cover properties class
"""

def get_concrete_cover_from_name(name, reinf, param_dict, default):
    """
    Get the concrete from the name
    """

    if not name in reinf:
        return default
                

    return eval(reinf[name], param_dict)


class ConcreteCoverProperties():
    """
    Implementation of the concrete cover properties class

    The class includes concrete cover properties for the
    left, right, top and bottom border
    """

    def __init__(self, left = 0, right = 0, top = 0, bottom = 0):
        """
        Set the properties of the concrete cover

        Parameter:  left    Concrete cover at the left border
                    right   Concrete cover at the right border
                    top     Concrete cover at the top border
                    bottom  Concrete cover at the bottom border
        """

        self.prop_left   = left
        self.prop_right  = right
        self.prop_top    = top
        self.prop_bottom = bottom

    def __repr__(self):
        description =  '<%s>\n'\
            '   left    = %s\n'\
            '   right   = %s\n'\
            '   top     = %s\n'\
            '   bottom  = %s\n'\
            % (self.__class__.__name__,
               self.prop_left,
               self.prop_right,
               self.prop_top,
               self.prop_bottom)
        return description

    @staticmethod
    def all(concrete_cover):
        """
        Set the properties of the concrete cover for all borders

        Parameter:  concrete_cover  Concrete cover at all borders
        """

        return ConcreteCoverProperties(concrete_cover, concrete_cover, concrete_cover, concrete_cover)


    @staticmethod
    def left_right_bottom(left, right, bottom):
        """
        Set the properties of the concrete cover

        Parameter:  left    Concrete cover at the left border
                    right   Concrete cover at the right border
                    bottom  Concrete cover at the bottom border
        """

        return ConcreteCoverProperties(left, right, 0, bottom)


    @staticmethod
    def left_right(left, right):
        """
        Set the properties of the concrete cover

        Parameter:  left    Concrete cover at the left border
                    right   Concrete cover at the right border
        """

        return ConcreteCoverProperties(left, right, 0, 0)


    @staticmethod
    def top_bottom(top, bottom):
        """
        Set the properties of the concrete cover

        Parameter:  top     Concrete cover at the top border
                    bottom  Concrete cover at the bottom border
        """

        return ConcreteCoverProperties(0, 0, top, bottom)


    @property
    def left(self):
        """
        Get the cover at the left border
        """
        return self.prop_left


    @property
    def right(self):
        """
        Get the cover at the right border
        """
        return self.prop_right


    @property
    def top(self):
        """
        Get the cover at the top border
        """
        return self.prop_top


    @property
    def bottom(self):
        """
        Get the cover at the bottom border
        """
        return self.prop_bottom

    def from_reinforcement_definition(self, reinf_def):
        """
        Get the cover from the reinforcement definition

        Args:
            reinf_def: reinforcement definition
        """

        self.prop_left   = reinf_def.get_value("ShapeCoverLeft", self.left);
        self.prop_right  = reinf_def.get_value("ShapeCoverRight", self.right);
        self.prop_bottom = reinf_def.get_value("ShapeCoverBottom", self.bottom);
        self.prop_top    = reinf_def.get_value("ShapeCoverTop", self.top);
