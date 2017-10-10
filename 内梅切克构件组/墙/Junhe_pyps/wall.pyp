<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>JunheModels\wall.py</Name> <!--file.pyc-->  
        <Title>wall</Title>
        <!-- <TextId>0001</TextId> -->
        <ReadLastInput>false</ReadLastInput>
        <Version>1.0</Version>
       <Interactor>False</Interactor>
    </Script>
    <Parameter>
        <Name>Picture</Name>
        <Value>wall.png</Value>
        <Orientation>Middle</Orientation>
        <ValueType>Picture</ValueType>
    </Parameter>
    <Page>
        <Name>Wall</Name>
        <Text>Wall</Text>
        <TextId>1001</TextId>   

        <Parameter>
            <Name>WallComponent</Name>
            <Text>Wall Component</Text>
            <TextId>1101</TextId>
            <ValueType>Expander</ValueType>

            <!--Parameter--> 
                      
            <Parameter>
                <Name>Length</Name>
                <Text>Length</Text>
                <TextId>1102</TextId>
                <Value>7000.</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>Height</Name>
                <Text>Height</Text>
                <TextId>1103</TextId>
                <Value>3500.</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>Width</Name>
                <Text>Width</Text>
                <TextId>1104</TextId>
                <Value>800.</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>ConcreteGrade</Name>
                <Text>Concrete Grade</Text>
                <TextId>1105</TextId>
                <Value>1</Value>
                <ValueType>ReinfConcreteGrade</ValueType>
            </Parameter>            
        </Parameter>
    </Page>
    <Page>
        <Name>HorizontalSteel</Name>
        <Text>Horizontal Steel</Text>
        <TextId>1200</TextId>
        <Parameter>
            <Name>HorizontalSteel</Name>
            <Text>Horizontal Steel</Text>
            <TextId>1201</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>HoriSteelVisual</Name>
                <Text>Horizontal Steel Visual</Text>
                <TextId>1202</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>MarkIndex_Hori</Name>
                <Text>Hori Steel Mark Index</Text>
                <TextId>1203</TextId>
                <Value>10</Value>
                <ValueType>Integer</ValueType>
            </Parameter>
            <Parameter>
                <Name>HoriSteelGrade</Name>
                <Text>Horizontal Steel Grade</Text>
                <TextId>1204</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>HoriSteelDia</Name>
                <Text>Horizontal Steel Diameter</Text>
                <TextId>1205</TextId>
                <Value>10</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>HoriDistance</Name>
                <Text>Horizontal Steel Distance</Text>
                <TextId>1206</TextId>
                <Value>500</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>HoriFrontCover</Name>
                <Text>Horizontal Front Cover</Text>
                <TextId>1207</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>HoriTopCover</Name>
                <Text>Horizontal Top Cover</Text>
                <TextId>1208</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>HoriBottomCover</Name>
                <Text>Horizontal Bottom Cover</Text>
                <TextId>1209</TextId>
                <Value>150</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>HoriExtend</Name>
                <Text>Horizontal Steel Extend Length</Text>
                <TextId>1210</TextId>
                <Value>500</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>HoriSteel_1</Name>
                <Text>Horizontal Steel 1 (group by two)</Text>
                <TextId>1300</TextId>
                <ValueType>Expander</ValueType>
                <Parameter>
                    <Name>HoriSideCover</Name>
                    <Text>Horizontal Side Cover</Text>
                    <Value>50</Value>
                    <TextId>1301</TextId>
                    <ValueType>length</ValueType>
                </Parameter>
            </Parameter>
            <Parameter>
                <Name>HoriSteel_2</Name>
                <Text>Horizontal Steel 2</Text>
                <TextId>1400</TextId>
                <ValueType>Expander</ValueType>
                <Parameter>
                    <Name>Degrees_HS2</Name>
                    <Text>90 Degrees_HS2</Text>
                    <TextId>1401</TextId>
                    <Value>false</Value>
                    <ValueType>checkbox</ValueType>
                </Parameter>
                <Parameter>
                    <Name>DegreesHook_HS2</Name>
                    <Text>90 Degrees Hook_HS2</Text>
                    <TextId>1402</TextId>
                    <Value>200</Value>
                    <ValueType>length</ValueType>
                    <Visible>Degrees_HS2 == True</Visible>
                </Parameter>
                <Parameter>
                    <Name>LeftAnchor_HS2</Name>
                    <Text>Left Anchor_HS2</Text>
                    <TextId>1403</TextId>
                    <Value>200</Value>
                    <ValueType>length</ValueType>
                </Parameter>
                <Parameter>
                    <Name>RightAnchor_HS2</Name>
                    <Text>Right Anchor_HS2</Text>
                    <TextId>1404</TextId>
                    <Value>200</Value>
                    <ValueType>length</ValueType>
                </Parameter>
            </Parameter>
        </Parameter>
    </Page>
    <Page>
        <Parameter>
            <Name>VerticalSteel</Name>
            <Text>Vertical Steel</Text>
            <TextId>1500</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>VertSteelVisual</Name>
                <Text>Vertical Steel Visual</Text>
                <TextId>1501</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>MarkIndex_Vert</Name>
                <Text>Vert Steel Mark Index</Text>
                <TextId>1502</TextId>
                <Value>11</Value>
                <ValueType>Integer</ValueType>
            </Parameter>
            <Parameter>
                <Name>VertSteelGrade</Name>
                <Text>Vertical Steel Grade</Text>
                <TextId>1503</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>VertSteelDia</Name>
                <Text>Vertical Steel Diameter</Text>
                <TextId>1504</TextId>
                <Value>8</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>VertSideCover</Name>
                <Text>Vertical Side Cover</Text>
                <TextId>1505</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>VertDistance</Name>
                <Text>Vertical Steel Distance</Text>
                <TextId>1506</TextId>
                <Value>500</Value>
                <ValueType>length</ValueType>
            </Parameter>

            <Parameter>
                <Name>TopAnchor</Name>
                <Text>Top Anchor</Text>
                <TextId>1600</TextId>
                <ValueType>Expander</ValueType>

                <Parameter>
                    <Name>Length_TA</Name>
                    <Text>Top Anchor Length</Text>
                    <TextId>1601</TextId>
                    <Value>500</Value>
                    <ValueType>length</ValueType>
                </Parameter>
                <Parameter>
                    <Name>BendingAnchor</Name>
                    <Text>Bending Anchor</Text>
                    <TextId>1602</TextId>
                    <Value>False</Value>
                    <ValueType>checkbox</ValueType>
                </Parameter>
                <Parameter>
                    <Name>BendingAnchorArea</Name>
                    <Text>Bending Anchor Area</Text>
                    <TextId>1603</TextId>
                    <ValueType>Expander</ValueType>

                    <Parameter>
                        <Name>BendPosition</Name>
                        <Text>Bend Position</Text>
                        <TextId>1604</TextId>
                        <Value>150</Value>
                        <ValueType>length</ValueType>
                        <Visible>BendingAnchor == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>BendLength</Name>
                        <Text>Bend Length</Text>
                        <TextId>1605</TextId>
                        <Value>150</Value>
                        <ValueType>length</ValueType>
                        <Visible>BendingAnchor == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>BendWidth</Name>
                        <Text>Bend Width</Text>
                        <TextId>1606</TextId>
                        <Value>100</Value>
                        <ValueType>length</ValueType>
                        <Visible>BendingAnchor == True</Visible>
                    </Parameter>
                </Parameter>
            </Parameter>


            <Parameter>
                <Name>Length_BA</Name>
                <Text>Bottom Anchor Length</Text>
                <TextId>1607</TextId>
                <Value>100</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
    </Page>


    <Page>
        <Parameter>
            <Name>TieSteel</Name>
            <Text>Tie Steel</Text>
            <TextId>1700</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>TieSteelVisual</Name>
                <Text>Tie Steel Visual</Text>
                <TextId>1701</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>MarkIndex_Tie</Name>
                <Text>Tie Steel Mark Index</Text>
                <TextId>1702</TextId>
                <Value>12</Value>
                <ValueType>Integer</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieSteelGrade</Name>
                <Text>Tie Steel Grade</Text>
                <TextId>1703</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieSteelDia</Name>
                <Text>Tie Steel Diameter</Text>
                <TextId>1704</TextId>
                <Value>8</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieMode</Name>
                <Text>Tie Mode</Text>
                <TextId>1705</TextId>
                <Value>1</Value>
                <ValueList>1|2</ValueList>
                <ValueType>IntegerComboBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieSteelHook</Name>
                <Text>Tie Steel Hook Length</Text>
                <TextId>1706</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>


<!--             <Parameter>
                <Name>TieType</Name>
                <Text>Tie Type</Text>
                <TextId>1708</TextId>
                <Value>1</Value>
                <ValueList>1|2</ValueList>
                <ValueType>IntegerComboBox</ValueType>
            </Parameter> -->
<!--             <Parameter>
                <Name>TieSteelAngle</Name>
                <Text>Tie Steel Hook Angle</Text>
                <TextId>1707</TextId>
                <Value>90</Value>
                <ValueType>angle</ValueType>
            </Parameter> -->
        </Parameter>
    </Page>


    <Page>
        <Name>Page2</Name>
        <Text>form</Text>
        <TextId>1800</TextId>
        <TextId>2001</TextId>      
        <Parameter>
            <Name>FormExpander</Name>
            <Text>Form Attribute</Text>
            <TextId>1801</TextId>
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