<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>mold.py</Name> <!--\file.pyc-->  
        <Title>title</Title>
        <Text>mold</Text>
        <!-- <TextId>1000</TextId> -->
        <ReadLastInput>true</ReadLastInput>
        <Version>1.0</Version>
       <Interactor>False</Interactor>
    </Script>
    <Page>
        <Name>Page</Name>
        <Text>Component Figure</Text>
        <TextId>1001</TextId>   

        <Parameter>
            <Name>ComponentExpander</Name>
            <Text>Component Parameter</Text>
            <TextId>1101</TextId>
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
                <Name>Length</Name>
                <Text>Length</Text>
                <TextId>1102</TextId>
                <Value>500.</Value>
                <ValueType>Length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>Width</Name>
                <Text>Width</Text>
                <TextId>1103</TextId>
                <Value>300.</Value>
                <ValueType>Length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
            <Parameter>
                <Name>Thick</Name>
                <Text>Thick</Text>
                <TextId>1104</TextId>
                <Value>250.</Value>
                <ValueType>Length</ValueType>
                <MinValue>100</MinValue>
            </Parameter>
        </Parameter>

        <Parameter>
            <Name>StiffenerExpander</Name>
            <Text>Stiffener Parameter</Text>
            <TextId>1105</TextId>
            <ValueType>Expander</ValueType>
            <Parameter>
                <Name>StiffenerThick</Name>
                <Text>Stiffener Thick</Text>
                <TextId>1106</TextId>
                <Value>6.</Value>
                <ValueList>6.|8.</ValueList>
                <ValueType>LengthCombobox</ValueType>
            </Parameter>

            <Parameter>
                <Name>SideStiffenerNum</Name>
                <Text>Side Stiffener Num</Text>
                <TextId>1107</TextId>
                <Value>5</Value>
                <ValueType>Integer</ValueType>
            </Parameter>
            <Parameter>
                <Name>SideStiffenerMidThick</Name>
                <Text>Side Stiffener Mid Thick</Text>
                <TextId>1108</TextId>
                <Value>6.</Value>
                <ValueList>6.|8.</ValueList>
                <ValueType>LengthCombobox</ValueType>
            </Parameter>                       
            <Parameter>
                <Name>SideStiffenerDistance</Name>
                <Text>Side Stiffener Distance</Text>
                <TextId>1109</TextId>
                <Value>200.</Value>
                <ValueType>Length</ValueType>
                <MinValue>50</MinValue>
            </Parameter>                        

            <Parameter>
                <Name>LongEdgeMainExtendLength</Name>
                <Text>Long Edge Main Stiffener Extend Length</Text>
                <TextId>1110</TextId>
                <Value>86.</Value>
                <ValueType>Length</ValueType>
            </Parameter>                             

            <Parameter>
                <Name>BottomStiffenerWidth</Name>
                <Text>Bottom Stiffener Width</Text>
                <TextId>1112</TextId>
                <Value>80.</Value>
                <ValueType>Length</ValueType>
            </Parameter>

            <Parameter>
                <Name>LongSurface</Name>
                <Text>Long Surface Material</Text>
                <TextId>e_SURFACE</TextId>
                <Value>SMT\\concrete_exposed_concrete_holes</Value>
                <DisableButtonIsShown>False</DisableButtonIsShown>
                <ValueType>MaterialButton</ValueType>
            </Parameter>

            <Parameter>
                <Name>ShortSurface</Name>
                <Text>Short Surface Material</Text>
                <TextId>e_SURFACE</TextId>
                <Value>SMT\\concrete_exposed_concrete_holes</Value>
                <DisableButtonIsShown>False</DisableButtonIsShown>
                <ValueType>MaterialButton</ValueType>
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


            
        </Parameter>            
    </Page>        

</Element>