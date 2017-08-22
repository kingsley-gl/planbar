<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>beam_chn_std.pyc</Name>  
        <Title>beam</Title>
        <TextId>0001</TextId>
        <ReadLastInput>True</ReadLastInput>
        <Version>1.0</Version>
       <Interactor>False</Interactor>
    </Script>
    <Page>
        <Name>Page1</Name>
        <Text>figure</Text>  
        <TextId>1001</TextId>

        <Parameter>
            <Name>PolyhedronExpander</Name>
            <Text>Polyhedron Size</Text>
            <TextId>1101</TextId>
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
            <Name>StirrupExpander</Name>
            <Text>Stirrup Parameter</Text>
            <TextId>1201</TextId>
            <ValueType>Expander</ValueType>
            <Parameter>
                <Name>HighDensityDistance</Name>
                <Text>High Density Area Distance</Text>
                <TextId>1202</TextId>
                <Value>200.</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>LowDensityDistance</Name>
                <Text>Low Density Area Distance</Text>
                <TextId>1203</TextId>
                <Value>300.</Value>
                <ValueType>length</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupConcreteGrade</Name>
                <Text>Stirrup Concrete Grade</Text>
                <TextId>1204</TextId>
                <Value>1</Value>
                <ValueType>ReinfConcreteGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupSteelGrade</Name>
                <Text>Stirrup Steel Grade</Text>
                <TextId>1205</TextId>
                <Value>3</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupDiameter</Name>
                <Text>Stirrup Diameter</Text>
                <TextId>1206</TextId>
                <Value>10.</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupConcreteCover</Name>
                <Text>Stirrup Concrete Cover</Text>
                <TextId>1207</TextId>
                <Value>20.</Value>
                <ValueType>ReinfConcreteCover</ValueType>
            </Parameter>
            <Parameter>
                <Name>StirrupType</Name>
                <Text>Stirrup Type</Text>
                <TextId>1208</TextId>
                <Value>Normal</Value>
                <ValueType>String</ValueType>
                <Enable>True</Enable>
            </Parameter>
            <Parameter>
                <Name>StirrupBendingRoller</Name>                
                <Text>Stirrup Bending Roller</Text>
                <TextId>1209</TextId>
                <Value>4.</Value>
                <ValueType>ReinfBendingRoller</ValueType>
            </Parameter>
        </Parameter>
        <Parameter>
            <Name>BarExpander</Name>
            <Text>Bar Parameter</Text>
            <TextId>1301</TextId>
            <ValueType>Expander</ValueType>
            <Parameter>
                <Name>BarConcreteGrade</Name>
                <Text>Bar Concrete Grade</Text>
                <TextId>1302</TextId>
                <Value>4</Value>
                <ValueType>ReinfConcreteGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>BarSteelGrade</Name>
                <Text>Bar Steel Grade</Text>
                <TextId>1303</TextId>
                <Value>4</Value>
                <ValueType>ReinfSteelGrade</ValueType>
            </Parameter>
            <Parameter>
                <Name>TopBarCount</Name>
                <Text>Top Bar Count</Text>
                <TextId>1304</TextId>
                <Value>3</Value>
                <ValueType>Integer</ValueType>
                <MinValue>0</MinValue>
            </Parameter>
            <Parameter>
                <Name>BottomBarCount</Name>
                <Text>Bottom Bar Count</Text>
                <TextId>1305</TextId>
                <Value>3</Value>
                <ValueType>Integer</ValueType>
                <MinValue>0</MinValue>
            </Parameter>
            <Parameter>
                <Name>TopBarDistance</Name>
                <Text>Top Bar Distance</Text>
                <TextId>1306</TextId>
                <Value>200.0</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>BottomBarDistance</Name>
                <Text>Bottom Bar Distance</Text>
                <TextId>1307</TextId>
                <Value>150.0</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>TopBarDiameter</Name>
                <Text>Top Bar Diameter</Text>
                <TextId>1308</TextId>
                <Value>10.</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>BottomBarDiameter</Name>
                <Text>Bottom Bar Diameter</Text>
                <TextId>1309</TextId>
                <Value>20.</Value>
                <ValueType>ReinfBarDiameter</ValueType>
            </Parameter>
            <Parameter>
                <Name>TopBarExtendLength</Name>
                <Text>Top Bar Extend Length</Text>
                <TextId>1310</TextId>
                <Value>0.</Value>
                <ValueType>Length</ValueType>
            </Parameter>
            <Parameter>
                <Name>BottomBarExtendLength</Name>
                <Text>Bottom Bar Extend Length</Text>
                <TextId>1311</TextId>
                <Value>0.</Value>
                <ValueType>Length</ValueType>
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
            <Parameter>
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
            </Parameter>
        </Parameter>            
    </Page>
</Element>