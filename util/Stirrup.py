# -*- coding: utf-8 -*-
# @Time    : 2017/08/11
# @Author  : kingsley kuang
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : stirrup.py 箍筋自建文件
# @Software: 
# @Function: 


import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_Reinforcement as AllplanReinf
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Utility as AllplanUtility          
import NemAll_Python_Palette as AllplanPalette


import StdReinfShapeBuilder.GeneralReinfShapeBuilder as GeneralShapeBuilder
import StdReinfShapeBuilder.LinearBarPlacementBuilder as LinearBarBuilder


from StdReinfShapeBuilder.ConcreteCoverProperties import ConcreteCoverProperties
from StdReinfShapeBuilder.ReinforcementShapeProperties import ReinforcementShapeProperties
from StdReinfShapeBuilder.RotationAngles import RotationAngles

print("Loading Stirrup.py")
class Stirrup(ConcreteCoverProperties,ReinforcementShapeProperties,object):

	def __init__(self,cover_dict=0,rebar_dict=0):
		ConcreteCoverProperties.__init__(self)
		self._con = ConcreteCoverProperties(1,2,3,4)
		#ReinforcementShapeProperties.rebar(**rebar_dict)
		self._mirror = False
		self._shape = None
		
	def shape(self):
		return self._shape

	def linear(self):
		print(self._con)

	def place(self):
		return

	@property
	def mirror(self):
		return self._mirror

	def cover(self,**kwargs):
		return

test = Stirrup()
print(test)
print(test.linear())