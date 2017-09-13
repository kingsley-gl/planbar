<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <!-- <Name>beam_chn_std.pyc</Name> -->
        <Name>JunheModels\beam.pyc</Name>   
        <Title>beam</Title>
        <TextId>1000</TextId>
        <ReadLastInput>False</ReadLastInput>
        <Version>1.0</Version>
       <Interactor>False</Interactor>
    </Script>
    <Page>
        <Name>Page1</Name>
        <Text>figure</Text>  
        <TextId>1002</TextId>

        <Parameter>
            <Name>PolyhedronExpander</Name>
            <Text>Polyhedron Size</Text>
            <TextId>1002</TextId>
            <ValueType>Expander</ValueType>     
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
        <Parameter>
            <Name>CutPara</Name>
            <Text>Cutter Parameter</Text>
            <TextId>1003</TextId>
            <ValueType>expander</ValueType>

            <Parameter>
                <Name>CutLength</Name>
                <Text>Cutter Length</Text>
                <TextId>1004</TextId>
                <Value>500</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>CutPosition</Name>
                <Text>Cutter Position</Text>
                <TextId>1005</TextId>
                <Value>3500</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
        <Parameter>
            <Name>SlotPara</Name>
            <Text>Slot Parameter</Text>
            <TextId>1501</TextId>
            <ValueType>expander</ValueType>
            <Parameter>
                <Name>SlotSide</Name>
                <Text>Slot Side distance</Text>
                <TextId>1502</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>SlotBottom</Name>
                <Text>Slot Bottom distance</Text>
                <TextId>1503</TextId>
                <Value>70</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>SlotLength</Name>
                <Text>Slot Length</Text>
                <TextId>1504</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
        <Parameter>
            <Name>KeyslotPara</Name>
            <Text>Keyslot Parameter</Text>
            <TextId>2001</TextId>
            <ValueType>expander</ValueType>

            <Parameter>
                <Name>KeyslotSide</Name>
                <Text>Keyslot Side Distance</Text>
                <TextId>2002</TextId>
                <Value>150</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>KeyslotEdge</Name>
                <Text>Keyslot Edge Distance</Text>
                <TextId>2003</TextId>
                <Value>15</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>KeyslotBottom</Name>
                <Text>Keyslot Bottom Distance</Text>
                <TextId>2004</TextId>
                <Value>350</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>KeyslotThick</Name>
                <Text>Keyslot Thick</Text>
                <TextId>2005</TextId>
                <Value>55</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>KeyslotHeight</Name>
                <Text>Keyslot Height</Text>
                <TextId>2006</TextId>
                <Value>75</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
    </Page>
    <Page>
        <Name>Page2</Name>
        <Text>Stirrup</Text>  
        <TextId>2501</TextId>
        <Parameter>
            <Name>StirrupExpander</Name>
            <Text>Stirrup Parameter</Text>
            <TextId>2501</TextId>
            <ValueType>Expander</ValueType>
            <Parameter>
                <Name>StirVisual</Name>
                <Text>Stirrup Visual</Text>
                <TextId>2500</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>ConcreteGrade</Name>
                <Text>Concrete Grade</Text>
                <TextId>2502</TextId>
                <Value>1</Value>
                <ValueType>ReinfConcreteGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>ConcreteCover</Name>
                <Text>Concrete Cover</Text>
                <TextId>2503</TextId>
                <Value>25</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirSteelGrade</Name>
                <Text>Stirrup Steel Grade</Text>
                <TextId>2504</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirDiameter</Name>
                <Text>Stirrup Diameter</Text>
                <TextId>2505</TextId>
                <Value>8</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>HeadCover</Name>
                <Text>Head Cover</Text>
                <TextId>2506</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>EndCover</Name>
                <Text>End Cover</Text>
                <TextId>2507</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirDistance</Name>
                <Text>Stirrup Distance</Text>
                <TextId>2508</TextId>
                <Value>200</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirBendDia</Name>                
                <Text>Stirrup Bending Roller Diameter</Text>
                <TextId>2509</TextId>
                <Value>2.</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirExtendLength</Name>
                <Text>Stirrup Extend Length</Text>
                <TextId>2510</TextId>
                <Value>140</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
    </Page>
    <Page>
        <Name>Page3</Name>
        <Text>LongitudinalBar</Text>  
        <TextId>3001</TextId>
        <Parameter>
            <Name>LongitudinalBar</Name>
            <Text>Longitudinal Bar Parameter</Text>
            <TextId>3001</TextId>
            <ValueType>Expander</ValueType>
            <Parameter>
                <Name>LongbarVisual</Name>
                <Text>Long Bar Visual</Text>
                <TextId>3000</TextId>
                <Value>true</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>LongBarLines</Name>
                <Text>Longitudinal Bar Lines</Text>
                <TextId>3002</TextId>
                <Value>2</Value>
                <ValueType>integer</ValueType>
            </Parameter>
            <Parameter>
                <Name>BarSteelGrade</Name>
                <Text>Bar Steel Grade</Text>
                <TextId>3003</TextId>
                <Value>4</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>FirstLine</Name>
                <Text>First Line</Text>
                <TextId>3501</TextId>
                <ValueType>expander</ValueType>

                <Parameter>
                    <Name>FirstDia</Name>
                    <Text>First Line Diameter</Text>
                    <TextId>3502</TextId>
                    <Value>12</Value>
                    <ValueType>ReinfBarDiameter</ValueType>
                </Parameter>
                <Parameter>
                    <Name>FirstNum</Name>
                    <Text>First Line Number</Text>
                    <TextId>3503</TextId>
                    <Value>4</Value>
                    <ValueType>integer</ValueType>
                </Parameter>
                <Parameter>
                    <Name>AnchorLength</Name>
                    <Text>Anchor Length</Text>
                    <TextId>3504</TextId>
                    <Value>500</Value>
                    <ValueType>length</ValueType>
                </Parameter>
                <Parameter>
                    <Name>AnchorBend</Name>
                    <Text>Anchor Bend</Text>
                    <TextId>3505</TextId>
                    <Value>False</Value>
                    <ValueType>checkbox</ValueType>
                </Parameter>
                <Parameter>
                    <Name>anchor</Name>
                    <ValueType>separator</ValueType>
                    <Visible>AnchorBend == True</Visible>
                </Parameter>

                <Parameter>
                    <Name>AnchorHeadBend</Name>
                    <Text>Anchor Head Bend</Text>
                    <TextId>3506</TextId>
                    <Value>False</Value>
                    <ValueType>CheckBox</ValueType>
                    <Visible>AnchorTailBend == False and AnchorBend == True</Visible>
                </Parameter>
                <Parameter>
                    <Name>AnchorTailBend</Name>
                    <Text>Anchor Tail Bend</Text>
                    <TextId>3507</TextId>
                    <Value>False</Value>
                    <ValueType>CheckBox</ValueType>
                    <Visible>AnchorHeadBend == False and AnchorBend == True</Visible>
                </Parameter>         
                <Parameter>
                    <Name>AnchorBendLength</Name>
                    <Text>Anchor Bend Lenght</Text>
                    <TextId>3508</TextId>
                    <Value>400</Value>
                    <ValueType>length</ValueType>
                    <Visible>AnchorBend == True</Visible>
                </Parameter>      
                <Parameter>
                    <Name>A_Anchor</Name>
                    <Text>A Anchor Lenght</Text>
                    <TextId>3509</TextId>
                    <Value>100</Value>
                    <ValueType>length</ValueType>
                    <Visible>AnchorBend == True</Visible>
                </Parameter>
                <Parameter>
                    <Name>B_HoriAnchor</Name>
                    <Text>B Horizontal Anchor</Text>
                    <TextId>3510</TextId>
                    <Value>200</Value>
                    <ValueType>length</ValueType>
                    <Visible>AnchorBend == True</Visible>
                </Parameter>
                <Parameter>
                    <Name>B_VertAnchor</Name>
                    <Text>B Vertical Anchor</Text>
                    <TextId>3511</TextId>
                    <Value>50</Value>
                    <ValueType>length</ValueType>
                    <Visible>AnchorBend == True</Visible>
                </Parameter>

                
            </Parameter>
            <Parameter>
                <Name>OtherLines</Name>
                <Text>Other Lines</Text>
                <TextId>4001</TextId>
                <ValueType>expander</ValueType>
                <!-- <Visible>LongBarLines not in {1}</Visible> -->

                <Parameter>
                    <Name>OtherDia</Name>
                    <Text>Other Lines Diameter</Text>
                    <TextId>4002</TextId>
                    <Value>10</Value>
                    <ValueType>ReinfBarDiameter</ValueType>
                </Parameter>
                <Parameter>
                    <Name>BarDistance</Name>
                    <Text>Bar Distance</Text>
                    <TextId>4003</TextId>
                    <Value>20</Value>
                    <ValueType>length</ValueType>
                </Parameter>
                <Parameter>
                    <Name>OtherHeadCover</Name>
                    <Text>Other Head Cover</Text>
                    <TextId>4004</TextId>
                    <Value>20</Value>
                    <ValueType>length</ValueType>
                </Parameter>
            </Parameter>
        </Parameter>
    </Page>
    <Page>
        <Name>Page4</Name>
        <Text>Waist and Tie</Text>  
        <TextId>4501</TextId>
        <Parameter>
            <Name>WaistBar</Name>
            <Text>Waist Bar</Text>
            <TextId>4501</TextId>
            <ValueType>expander</ValueType>
            <Parameter>
                <Name>WaistVisual</Name>
                <Text>Waist Bar Visual</Text>
                <TextId>4500</TextId>
                <Value>true</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistBarGrade</Name>
                <Text>Waist Bar Steel Grade</Text>
                <TextId>4502</TextId>
                <Value>5</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistBarDia</Name>
                <Text>Waist Bar Diameter</Text>
                <TextId>4503</TextId>
                <Value>8</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistPosition</Name>
                <Text>Waist Bar Position</Text>
                <TextId>4504</TextId>
                <Value>300</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistDistance</Name>
                <Text>Waist Bar Distance</Text>
                <TextId>4505</TextId>
                <Value>100</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistNum</Name>
                <Text>Waist Bar Num</Text>
                <TextId>4506</TextId>
                <Value>3</Value>
                <ValueType>integer</ValueType>
            </Parameter>
            <Parameter>
                <Name>WaistHeadCover</Name>
                <Text>Waist Head Cover</Text>
                <TextId>4507</TextId>
                <Value>20</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>CutBarExtend</Name>
                <Text>Cutter Bar Extend</Text>
                <TextId>4508</TextId>
                <Value>100</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieBarVisual</Name>
                <Text>Tie Bar Visual</Text>
                <TextId>4512</TextId>
                <Value>true</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieBarDia</Name>
                <Text>Tie Bar Diameter</Text>
                <TextId>4509</TextId>
                <Value>8</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieBarGrade</Name>
                <Text>Tie Bar Grade</Text>
                <TextId>4510</TextId>
                <Value>2</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>TieBarRatio</Name>
                <Text>Tie Bar Ratio</Text>
                <TextId>4511</TextId>
                <Value>1</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
    </Page>
    <Page>
        <Name>Page2</Name>
        <Text>form</Text>
        <TextId>9001</TextId>      
        <Parameter>
            <Name>FormExpander</Name>
            <Text>Form Attribute</Text>
            <TextId>9002</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>Surface</Name>
                <Text>Surface Material</Text>
                <TextId>e_SURFACE</TextId>
                <Value>SMT\\concrete_exposed_concrete_holes</Value>
                <DisableButtonIsShown>False</DisableButtonIsShown>
                <ValueType>MaterialButton</ValueType>
            </Parameter>
<!--             <Parameter>
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