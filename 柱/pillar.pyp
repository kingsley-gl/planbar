<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>pillar.py</Name> <!--file.pyc-->  
        <Title>pillar</Title>
        <TextId>1000</TextId>
        <ReadLastInput>true</ReadLastInput>
        <Version>1.0</Version>
       <Interactor>False</Interactor>
    </Script>
    <Page>
        <Name>Page</Name>
        <Text>Parameter</Text>
        <TextId>1001</TextId>   

        <Parameter>
            <Name>ExpanderGeo</Name>
            <Text>Geometry</Text>
            <TextId>1101</TextId>
            <ValueType>Expander</ValueType>

            <!--Parameter-->           
            <Parameter>
                <Name>Length</Name>
                <Text>Length</Text>
                <TextId>1102</TextId>
                <Value>1000.</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>Width</Name>
                <Text>Width</Text>
                <TextId>1103</TextId>
                <Value>1000.</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>Height</Name>
                <Text>Height</Text>
                <TextId>1104</TextId>
                <Value>1000.</Value>
                <ValueType>length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>ConcreteGrade</Name>
                <Text>Concrete Grades</Text>
                <TextId>1105</TextId>
                <Value>4</Value>
                <ValueType>ReinfConcreteGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>ConcreteCover</Name>
                <Text>Concrete Cover</Text>
                <TextId>1106</TextId>
                <Value>30</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
        <Parameter>
            <Name>ExpanderSteel</Name>
            <Text>Longitudinal Steel</Text>
            <TextId>1200</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>VisualSteel</Name>
                <Text>Visual Steel</Text>
                <TextId>1201</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>SteelGrade</Name>
                <Text>Steel Grade</Text>
                <TextId>1202</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>Diameter</Name>
                <Text>Diameter</Text>
                <TextId>1203</TextId>
                <Value>2</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>Pairs</Name>
                <Text>Pairs</Text>
                <TextId>1204</TextId>
                <Value>2</Value>
                <ValueList>2|3|4</ValueList>
                <ValueType>IntegerComboBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>Shape</Name>
                <Text>Shape</Text>
                <TextId>1205</TextId>
                <Value>straight</Value>
                <ValueTextId>1214</ValueTextId>
                <ValueList>straight|bend</ValueList>
                <ValueList_TextIds>1215</ValueList_TextIds>
                <TextId>1205|1214|1215</TextId>
                <ValueType>StringComboBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>Separator1</Name>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>A_FrontCover</Name>
                <Text>A_Front Cover</Text>
                <TextId>1206</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>A_SideCover</Name>
                <Text>A_Side Cover</Text>
                <TextId>1207</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>UpperStretch</Name>
                <Text>Upper Stretch</Text>
                <TextId>1208</TextId>
                <Value>20</Value>
                <ValueType>length</ValueType>
            </Parameter>      
            <Parameter>
                <Name>BottomShrink</Name>
                <Text>Bottom Shrink</Text>
                <TextId>1209</TextId>
                <Value>20</Value>
                <ValueType>length</ValueType>
            </Parameter>   
            <Parameter>
                <Name>A_Length</Name>
                <Text>A_Length</Text>
                <TextId>1210</TextId>
                <Value>20</Value>
                <ValueType>length</ValueType>
                <Visible>Shape in {"bend"}</Visible>
            </Parameter>
            <Parameter>
                <Name>B_HoriLength</Name>
                <Text>B_Horizontal Length</Text>
                <TextId>1211</TextId>
                <Value>0</Value>
                <ValueType>length</ValueType>
                <Visible>Shape in {"bend"}</Visible>
            </Parameter>
            <Parameter>
                <Name>B_VertLength</Name>
                <Text>B_Vertical Length</Text>
                <TextId>1212</TextId>
                <Value>20</Value>
                <ValueType>length</ValueType>
                <Visible>Shape in {"bend"}</Visible>
            </Parameter>
            <Parameter>
                <Name>C_Length</Name>
                <Text>C_Length</Text>
                <TextId>1213</TextId>
                <Value>0</Value>
                <ValueType>length</ValueType>
                <Visible>Shape in {"bend"}</Visible>
            </Parameter>
        </Parameter>
        <Parameter>
            <Name>Stirrup1</Name>
            <Text>Stirrup 1</Text>
            <TextId>1300</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>VisualStir1</Name>
                <Text>Visual Stirrup 1</Text>
                <TextId>1301</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupGrade1</Name>
                <Text>Stirrup Grade 1</Text>
                <TextId>1302</TextId>
                <Value>2</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>DensArea</Name>
                <Text>Dens Area</Text>
                <TextId>1303</TextId>
                <Value>500.</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>SeparatorLow</Name>
                <ValueType>separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>LowDensDia</Name>
                <Text>Low Dens Diameter</Text>
                <TextId>1304</TextId>
                <Value>2</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>LDBendDia</Name>
                <Text>Low Dens Bend Diameter</Text>
                <TextId>1305</TextId>
                <Value>20</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>LDPitch</Name>
                <Text>Low Dens Pitch</Text>
                <TextId>1306</TextId>
                <Value>100</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>LDPrimPitch</Name>
                <Text>Low Dens Primary Pitch</Text>
                <TextId>1307</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>SeparatorHigh</Name>
                <ValueType>separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>HighDensDia</Name>
                <Text>High Dens Diameter</Text>
                <TextId>1308</TextId>
                <Value>2</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>HDBendDia</Name>
                <Text>High Dens Bend Diameter</Text>
                <TextId>1309</TextId>
                <Value>20</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>HDPitch</Name>
                <Text>High Dens Pitch</Text>
                <TextId>1310</TextId>
                <Value>100</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>HDPrimPitch</Name>
                <Text>High Dens Primary Pitch</Text>
                <TextId>1311</TextId>
                <Value>50</Value>
                <ValueType>length</ValueType>
            </Parameter>
        </Parameter>
        <Parameter>
            <Name>Stirrup2</Name>
            <Text>Stirrup2</Text>
            <TextId>1400</TextId>
            <ValueType>Expander</ValueType>

            <Parameter>
                <Name>VisualStir2</Name>
                <Text>Visual Stirrup 2</Text>
                <TextId>1401</TextId>
                <Value>True</Value>
                <ValueType>checkbox</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupGrade2</Name>
                <Text>Stirrup Grade2</Text>
                <TextId>1402</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupDia2</Name>
                <Text>Stirrup Diameter2</Text>
                <TextId>1403</TextId>
                <Value>2</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>Position1</Name>
                <Text>Position1</Text>
                <TextId>1404</TextId>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>Position2</Name>
                <Text>Position2</Text>
                <TextId>1405</TextId>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>Position3</Name>
                <Text>Position3</Text>
                <TextId>1406</TextId>
                <Value>False</Value>
                <Visible>Pairs in {3,4}</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>Position4</Name>
                <Text>Position4</Text>
                <TextId>1407</TextId>
                <Value>False</Value>
                <Visible>Pairs in {4}</Visible>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>HookLength</Name>
                <Text>Hook Length</Text>
                <TextId>1408</TextId>
                <Value>75</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>HookAngle</Name>
                <Text>Hook Angle</Text>
                <TextId>1409</TextId>
                <Value>90</Value>
                <ValueType>angle</ValueType>
            </Parameter>
        </Parameter>
    </Page>
</Element>