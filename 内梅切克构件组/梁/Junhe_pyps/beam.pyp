<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>JunheModels\beam.py</Name> <!--file.pyc-->  
        <Title>title</Title>
        <TextId>1000</TextId>
        <ReadLastInput>false</ReadLastInput>
        <Version>1.0</Version>
       <Interactor>False</Interactor>
    </Script>
    <Parameter>
        <Name>Picture</Name>
        <Value>beam.png</Value>
        <Orientation>Middle</Orientation>
        <ValueType>Picture</ValueType>
    </Parameter>
    <Page>
        <Name>Page1</Name>
        <Text>ConcreteMember</Text>
        <TextId>1001</TextId>   

        <Parameter>
            <Name>ConcreteMemberParameters</Name>
            <Text>Concrete Member Parameters</Text>
            <TextId>1101</TextId>
            <ValueType>Expander</ValueType>
            <Parameter>
                <Name>ConcreteGrade</Name>
                <Text>Concrete Grade</Text>
                <TextId>1102</TextId>
                <Value>1</Value>
                <ValueType>ReinfConcreteGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>Length</Name>
                <Text>Length</Text>
                <TextId>e_LENGTH</TextId>
                <Value>7500</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>Height</Name>
                <Text>Height</Text>
                <TextId>e_HEIGHT</TextId>
                <Value>750</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>Width</Name>
                <Text>Width</Text>
                <TextId>e_WIDTH</TextId>
                <Value>400</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
        </Parameter>
    </Page>

    <Page>
        <Name>Page3</Name>
        <Text>Stirrup</Text>
        <TextId>3001</TextId>      

        <Parameter>
            <Name>Separator1</Name>
            <ValueType>Separator</ValueType>
        </Parameter>

            <Parameter>
                <Name>StirrupVisual</Name>
                <Text>Stirrup</Text>
                <TextId>3101</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>

        <Parameter>
            <Name>StirrupExpander</Name>
            <Text>Stirrup Parameter</Text>
            <TextId>3102</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>StirSteelGrade</Name>
                <Text>Stirrup Steel Grade</Text>
                <TextId>3103</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirDiameter</Name>
                <Text>Stirrup Diameter</Text>
                <TextId>3104</TextId>
                <Value>12</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirSideCover</Name>
                <Text>Stirrup Side Cover</Text>
                <TextId>3105</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirUpsCover</Name>
                <Text>Stirrup Ups Cover</Text>
                <TextId>3106</TextId>
                <Value>80</Value>
                <ValueType>length</ValueType>
            </Parameter>

                <Parameter>
                    <Name>StirrupType</Name>
                    <Text>Stirrup Type</Text>
                    <TextId>3107</TextId>
                    <Value>1</Value>
                    <ValueList>1|2</ValueList>
                    <ValueType>IntegerComboBox</ValueType>
                </Parameter>
                <Parameter>
                    <Name>type</Name>
                    <ValueType>separator</ValueType>
                    <Visible>StirrupType == 1</Visible>
                </Parameter> 
                <Parameter>
                    <Name>StirrupOneHookLength</Name>
                    <Text>Stirrup One Hook Length</Text>
                    <TextId>3108</TextId>
                    <Value>200</Value>
                    <ValueType>length</ValueType>
                    <Visible>StirrupType == 1</Visible>
                </Parameter>
                <Parameter>
                    <Name>StirOneExtendLength</Name>
                    <Text>Stirrup One Extend Length</Text>
                    <TextId>3109</TextId>
                    <Value>200</Value>
                    <ValueType>length</ValueType>
                    <Visible>StirrupType == 1</Visible>
                </Parameter>      



                <Parameter>
                    <Name>type</Name>
                    <ValueType>separator</ValueType>
                    <Visible>StirrupType == 2</Visible>
                </Parameter>     
                <Parameter>
                    <Name>StirTwoExtendLength</Name>
                    <Text>Stirrup Two Extend Length</Text>
                    <TextId>3110</TextId>
                    <Value>200</Value>
                    <ValueType>length</ValueType>
                    <Visible>StirrupType == 2</Visible>
                </Parameter>      
        </Parameter>

        <Parameter>
            <Name>DenseRegion</Name>
            <Text>Dense Region</Text>
            <TextId>4001</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>StirBothEndLength</Name>
                <Text>Stirrup Both End Length</Text>
                <TextId>4101</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
            </Parameter>

            <Parameter>
                <Name>StirDenseRegionDistance</Name>
                <Text>Stirrup Dense Region Distance</Text>
                <TextId>4102</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupSparseRegionDistance</Name>
                <Text>Stirrup Sparse Region Distance</Text>
                <TextId>4103</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
            </Parameter>

            <Parameter>
                <Name>StirDenseRegionLength</Name>
                <Text>Stirrup Dense Region Length</Text>
                <TextId>4104</TextId>
                <Value>1400</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
    </Page>

    <Page>
        <Name>Page4</Name>
        <Text>Longitudinal Bar</Text>
        <TextId>5001</TextId>      

        <Parameter>
            <Name>Separator1</Name>
            <ValueType>Separator</ValueType>
        </Parameter>

            <Parameter>
                <Name>LongBarVisual</Name>
                <Text>Long Bar</Text>
                <TextId>5101</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
        <Parameter>
            <Name>SteelGrade</Name>
            <Text>Steel Grade</Text>
            <TextId>5102</TextId>
            <Value>3</Value>
            <ValueType>ReinfSteelGrade</ValueType>
        </Parameter>

        <Parameter>
            <Name>TopFirstRowLongBar</Name>
            <Text>Top First Row Bar Parameter</Text>
            <TextId>6001</TextId>
            <ValueType>Expander</ValueType>



            <Parameter>
                <Name>BarDiameter_T1</Name>
                <Text>First Row Bar Diameter</Text>
                <TextId>6101</TextId>
                <Value>12</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>

            <Parameter>
                <Name>BarNumber_T1</Name>                
                <Text>First Row Bar Number</Text>
                <TextId>6102</TextId>
                <Value>3</Value>
                <ValueType>Integer</ValueType>
            </Parameter>
            <Parameter>
                <Name>AnchorHead_T1</Name>
                <Text>Top First Head Straight Anchor Length</Text>
                <TextId>6103</TextId>
                <Value>600</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>AnchorTail_T1</Name>
                <Text>Top First Tail Straight Anchor Length</Text>
                <TextId>6104</TextId>
                <Value>600</Value>
                <ValueType>length</ValueType>
            </Parameter>

            <Parameter>
                <Name>AnchorHead90_T1</Name>
                <Text>Top First Anchor Head Bend</Text>
                <TextId>6105</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>  

            <Parameter>
                <Name>AnchorTail90_T1</Name>
                <Text>Top First Anchor Tail Bend</Text>
                <TextId>6106</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            

            <Parameter>
                <Name>TopSecondRowLongBar</Name>
                <Text>Top Second Row Long Bar</Text>
                <TextId>7001</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
        </Parameter>

        <Parameter>
            <Name>TopOtherRowLongBar</Name>
            <Text>Top Other Row Bar Parameter</Text>
            <TextId>7001</TextId>
            <ValueType>Expander</ValueType>
            <Visible>TopSecondRowLongBar == True</Visible>

            <Parameter>
                <Name>BarDiameter_TO</Name>
                <Text>Second Row Bar Diameter</Text>
                <TextId>7101</TextId>
                <Value>12</Value>
                <ValueType>ReinfBarDiameter</ValueType>
                <Visible>TopSecondRowLongBar == True</Visible>
            </Parameter>
            <Parameter>
                <Name>TopBarDistance</Name>
                <Text>Between First And Second Row Spacing</Text>
                <TextId>7102</TextId>
                <Value>80</Value>
                <ValueType>Length</ValueType>
                <Visible>TopSecondRowLongBar == True</Visible>
            </Parameter>


            <Parameter>
                <Name>BarNumber_TO</Name>                
                <Text>Second Row Bar Number</Text>
                <TextId>7103</TextId>
                <Value>3</Value>
                <ValueType>Integer</ValueType>
                <Visible>TopSecondRowLongBar == True</Visible>
            </Parameter>
            <Parameter>
                <Name>AnchorHead_TO</Name>
                <Text>Top Second Head Straight Anchor Length</Text>
                <TextId>7104</TextId>
                <Value>300</Value>
                <ValueType>length</ValueType>
                <Visible>TopSecondRowLongBar == True</Visible>
            </Parameter>
            <Parameter>
                <Name>AnchorTail_TO</Name>
                <Text>Top traight Tail Anchor Length</Text>
                <TextId>7105</TextId>
                <Value>300</Value>
                <ValueType>length</ValueType>
                <Visible>TopSecondRowLongBar == True</Visible>
            </Parameter>

            <Parameter>
                <Name>AnchorHead90_TO</Name>
                <Text>Top Second Anchor Head Bend</Text>
                <TextId>7106</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
                <Visible>TopSecondRowLongBar == True</Visible>
            </Parameter>  

            <Parameter>
                <Name>AnchorTail90_TO</Name>
                <Text>Top Second Anchor Tail Bend</Text>
                <TextId>7107</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
                <Visible>TopSecondRowLongBar == True</Visible>
            </Parameter>
        </Parameter>


        <Parameter>
            <Name>BottomFirstRowLongBar</Name>
            <Text>Bottom First Row Bar Parameter</Text>
            <TextId>8001</TextId>
            <ValueType>Expander</ValueType>



            <Parameter>
                <Name>BarDiameter_B1</Name>
                <Text>First Row Bar Diameter</Text>
                <TextId>8101</TextId>
                <Value>12</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>


            <Parameter>
                <Name>BarNumber_B1</Name>                
                <Text>First Row Bar Number</Text>
                <TextId>8102</TextId>
                <Value>3</Value>
                <ValueType>Integer</ValueType>
            </Parameter>

            <Parameter>
                <Name>AnchorHead_B1</Name>
                <Text>First Row Head Straight Anchor Length</Text>
                <TextId>8103</TextId>
                <Value>400</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>AnchorTail_B1</Name>
                <Text>First Row Tail Straight Anchor Length</Text>
                <TextId>8104</TextId>
                <Value>400</Value>
                <ValueType>length</ValueType>
            </Parameter>

            <Parameter>
                <Name>AnchorHead90_B1</Name>
                <Text>First Row Ninety Degree Anchor Head Bend</Text>
                <TextId>8105</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>AnchorTail90_B1</Name>
                <Text>First Row Ninety Degree Anchor Tail Bend</Text>
                <TextId>8106</TextId>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>

        </Parameter>
        <Parameter>
            <Name>BottomSecondRowLongBar</Name>
            <Text>Bottom Second Row Long Bar</Text>
            <TextId>9001</TextId>
            <Value>False</Value>
            <ValueType>checkbox</ValueType>
        </Parameter>

        <Parameter>
            <Name>BottomOtherRowLongBar</Name>
            <Text>Bottom Other Row Bar Parameter</Text>
            <TextId>9101</TextId>
            <ValueType>Expander</ValueType>
            <Visible>BottomSecondRowLongBar == True</Visible>


            <Parameter>
                <Name>BarDiameter_BO</Name>
                <Text>Bottom Other Row Bar Diameter</Text>
                <TextId>9102</TextId>
                <Value>12</Value>
                <ValueType>ReinfBarDiameter</ValueType>
                <Visible>BottomSecondRowLongBar == True</Visible>
            </Parameter>
            <Parameter>
                <Name>BottomBarDistance</Name>
                <Text>Between First And Second Row Distance</Text>
                <TextId>9103</TextId>
                <Value>80</Value>
                <ValueType>Length</ValueType>
                <Visible>BottomSecondRowLongBar == True</Visible>
            </Parameter>

            <Parameter>
                <Name>BarNumber_BO</Name>                
                <Text>Bottom Other Row Bar Number</Text>
                <TextId>9104</TextId>
                <Value>3</Value>
                <ValueType>Integer</ValueType>
                <Visible>BottomSecondRowLongBar == True</Visible>
            </Parameter>
            <Parameter>
                <Name>AnchorHead_BO</Name>
                <Text>Bottom Second Head Straight Anchor Length</Text>
                <TextId>9105</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
                <Visible>BottomSecondRowLongBar == True</Visible>
            </Parameter>
            <Parameter>
                <Name>AnchorTail_BO</Name>
                <Text>Bottom Second Tail Straight Anchor Length</Text>
                <TextId>9106</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
                <Visible>BottomSecondRowLongBar == True</Visible>
            </Parameter>

            <Parameter>
                <Name>AnchorHead90_BO</Name>
                <Text>90 degree Anchor Head bend</Text>
                <TextId>9107</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
                <Visible>BottomSecondRowLongBar == True</Visible>
            </Parameter>

            <Parameter>
                <Name>AnchorTail90_BO</Name>
                <Text>90 degree Anchor Tail Bend</Text>
                <TextId>9108</TextId>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
                <Visible>BottomSecondRowLongBar == True</Visible>
            </Parameter>   

        </Parameter>

    </Page>

    <Page>
        <Name>Page5</Name>
        <Text>Waist Bar</Text>
        <TextId>9002</TextId>      
        <Parameter>
            <Name>WaistBar</Name>
            <Text>Waist Bar Parameter</Text>
            <TextId>9200</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>WaistBarVisual</Name>
                <Text>Waist Bar</Text>
                <TextId>9201</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>

        <Parameter>
            <Name>Separator1</Name>
            <ValueType>Separator</ValueType>
        </Parameter>

            <Parameter>
                <Name>WaistBarSteelGrade</Name>
                <Text>Waist Bar Steel Grade</Text>
                <TextId>9202</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistBarDiameter</Name>
                <Text>Waist Bar Diameter</Text>
                <TextId>9203</TextId>
                <Value>12</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>

            <Parameter>
                <Name>WaistRows</Name>                
                <Text>Waist Bar Row Number</Text>
                <TextId>9204</TextId>
                <Value>2</Value>
                <ValueType>Integer</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistDistance</Name>                
                <Text>Waist Bar Row Distance</Text>
                <TextId>9205</TextId>
                <Value>250</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistPosition</Name>                
                <Text>Waist Bar Row Position</Text>
                <TextId>9206</TextId>
                <Value>200</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>AnchorHead_W</Name>
                <Text>Waist Bar Head Straight Anchor Length</Text>
                <TextId>9207</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>AnchorTail_W</Name>
                <Text>Waist Bar Tail Straight  Anchor Length</Text>
                <TextId>9208</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
            </Parameter>

            <Parameter>
                <Name>AnchorHead90_W</Name>
                <Text>Anchor Head Bend</Text>
                <TextId>9209</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>

            <Parameter>
                <Name>AnchorTail90_W</Name>
                <Text>Anchor Tail Bend</Text>
                <TextId>9210</TextId>
                <Value>False</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
        </Parameter>
    </Page>

    <Page>
        <Name>Page6</Name>
        <Text>TieBar</Text>
        <TextId>9003</TextId>      
        <Parameter>
            <Name>TieBarExpander</Name>
            <Text>Tie Bar Parameter</Text>
            <TextId>9301</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>TieBarVisual</Name>
                <Text>Tie Bar</Text>
                <TextId>9302</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>

        <Parameter>
            <Name>Separator1</Name>
            <ValueType>Separator</ValueType>
        </Parameter>

            <Parameter>
                <Name>TieBarGrade</Name>
                <Text>Tie Bar Grade</Text>
                <TextId>9303</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieBarDia</Name>
                <Text>Tie Bar Diameter</Text>
                <TextId>9304</TextId>
                <Value>12</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>

            <Parameter>
                <Name>TieBendingLength</Name>
                <Text>Tie Bar Bending Length</Text>
                <TextId>9305</TextId>
                <Value>140</Value>
                <ValueType>length</ValueType>
            </Parameter>

            <Parameter>
                <Name>TieBarAngle</Name>
                <Text>Tie Bar One End Bending Angle</Text>
                <TextId>9306</TextId>
                <Value>90</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>   
    </Page>
    <Page>
        <Name>Page2</Name>
        <Text>form</Text>
        <TextId>2001</TextId>      
        <Parameter>
            <Name>FormExpander</Name>
            <Text>Form Attribute</Text>
            <TextId>2101</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>Surface</Name>
                <Text>Surface Material</Text>
                <TextId>e_SURFACE</TextId>
                <Value>SMT\\concrete_exposed_concrete_holes</Value>
                <DisableButtonIsShown>False</DisableButtonIsShown>
                <ValueType>MaterialButton</ValueType>
            </Parameter>
           <!--  <Parameter>
                <Name>Layer</Name>
                <Text>Layer</Text>
                <TextId>e_LAYER</TextId>
                <Value>0</Value>
                <ValueType>Layer</ValueType>
            </Parameter>
            <Parameter>
                <Name>Pen</Name>
                <Text>Pen</Text>
                <TextId>2102</TextId>
                <Value>1</Value>
                <ValueType>Pen</ValueType>
            </Parameter>
            <Parameter>
                <Name>Stroke</Name>
                <Text>Stroke</Text>
                <TextId>2103</TextId>
                <Value>1</Value>
                <ValueType>Stroke</ValueType>
            </Parameter>
            <Parameter>
                <Name>Color</Name>
                <Text>Color</Text>
                <TextId>e_COLOR</TextId>
                <Value>1</Value>
                <ValueType>Color</ValueType>
            </Parameter>
            <Parameter>
                <Name>UseConstructionLineMode</Name>
                <Text>Construction Line</Text>  
                <TextId>2104</TextId>
                <Value>1</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter> -->
        </Parameter>     
    </Page>        
</Element>