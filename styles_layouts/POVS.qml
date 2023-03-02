<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyMaxScale="1" simplifyDrawingHints="1" simplifyAlgorithm="0" simplifyDrawingTol="1" version="3.16.0-Hannover" minScale="100000000" simplifyLocal="1" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" labelsEnabled="1" readOnly="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal enabled="0" accumulate="0" durationField="" endExpression="" endField="" fixedDuration="0" startField="" mode="0" durationUnit="min" startExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 type="singleSymbol" forceraster="0" enableorderby="0" symbollevels="0">
    <symbols>
      <symbol type="fill" alpha="1" force_rhr="0" clip_to_extent="1" name="0">
        <layer locked="0" enabled="1" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="0,170,0,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontItalic="0" fontKerning="1" capitalization="0" blendMode="0" fontStrikeout="0" multilineHeight="1" fontSize="10" useSubstitutions="0" allowHtml="0" textOrientation="horizontal" previewBkgrdColor="255,255,255,255" fontUnderline="0" textOpacity="1" fontWeight="50" textColor="0,0,0,255" fontFamily="MS Shell Dlg 2" namedStyle="Regular" fontWordSpacing="0" isExpression="1" fontSizeUnit="Point" fontLetterSpacing="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fieldName="sitecode + ' ' + sitename">
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="1" bufferBlendMode="0" bufferDraw="1" bufferSize="1" bufferSizeUnits="MM" bufferJoinStyle="128" bufferOpacity="1" bufferColor="255,255,255,255"/>
        <text-mask maskSize="1.5" maskEnabled="0" maskedSymbolLayers="" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskJoinStyle="128" maskType="0" maskSizeUnits="MM" maskOpacity="1"/>
        <background shapeOffsetUnit="MM" shapeRadiiY="0" shapeSizeType="0" shapeType="0" shapeJoinStyle="64" shapeOffsetX="0" shapeOpacity="1" shapeSizeX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeFillColor="255,255,255,255" shapeSizeY="0" shapeRotation="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeSizeUnit="MM" shapeOffsetY="0" shapeRadiiX="0" shapeBorderWidth="0" shapeDraw="0" shapeSVGFile="" shapeRadiiUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeBorderColor="128,128,128,255" shapeSizeMapUnitScale="3x:0,0,0,0,0,0">
          <symbol type="marker" alpha="1" force_rhr="0" clip_to_extent="1" name="markerSymbol">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="164,113,88,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadius="1.5" shadowOffsetGlobal="1" shadowOffsetDist="1" shadowOffsetUnit="MM" shadowDraw="0" shadowUnder="0" shadowScale="100" shadowRadiusAlphaOnly="0" shadowRadiusUnit="MM" shadowOpacity="0.7" shadowOffsetAngle="135" shadowColor="0,0,0,255" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format formatNumbers="0" autoWrapLength="0" plussign="0" decimals="3" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" rightDirectionSymbol=">" leftDirectionSymbol="&lt;" wrapChar="" placeDirectionSymbol="0" multilineAlign="3" reverseDirectionSymbol="0"/>
      <placement quadOffset="4" preserveRotation="1" maxCurvedCharAngleIn="25" lineAnchorPercent="0.5" maxCurvedCharAngleOut="-25" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" rotationAngle="0" centroidWhole="0" priority="5" overrunDistanceUnit="MM" geometryGeneratorType="PointGeometry" centroidInside="0" polygonPlacementFlags="2" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" distMapUnitScale="3x:0,0,0,0,0,0" dist="0" placementFlags="10" distUnits="MM" repeatDistanceUnits="MM" yOffset="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorEnabled="0" overrunDistance="0" placement="0" offsetType="0" offsetUnits="MM" repeatDistance="0" geometryGenerator="" lineAnchorType="0" xOffset="0" layerType="PolygonGeometry" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0"/>
      <rendering drawLabels="1" obstacleType="1" fontMinPixelSize="3" scaleMin="0" fontMaxPixelSize="10000" displayAll="0" minFeatureSize="0" labelPerPart="0" limitNumLabels="0" scaleMax="0" mergeLines="0" fontLimitPixelSize="0" obstacle="1" upsidedownLabels="0" obstacleFactor="1" scaleVisibility="0" maxNumLabels="2000" zIndex="0"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" value="" name="name"/>
          <Option name="properties"/>
          <Option type="QString" value="collection" name="type"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option type="QString" value="pole_of_inaccessibility" name="anchorPoint"/>
          <Option type="Map" name="ddProperties">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
          <Option type="bool" value="false" name="drawToAllParts"/>
          <Option type="QString" value="0" name="enabled"/>
          <Option type="QString" value="point_on_exterior" name="labelAnchorPoint"/>
          <Option type="QString" value="&lt;symbol type=&quot;line&quot; alpha=&quot;1&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot; name=&quot;symbol&quot;>&lt;layer locked=&quot;0&quot; enabled=&quot;1&quot; pass=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol"/>
          <Option type="double" value="0" name="minLength"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale"/>
          <Option type="QString" value="MM" name="minLengthUnit"/>
          <Option type="double" value="0" name="offsetFromAnchor"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale"/>
          <Option type="QString" value="MM" name="offsetFromAnchorUnit"/>
          <Option type="double" value="0" name="offsetFromLabel"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale"/>
          <Option type="QString" value="MM" name="offsetFromLabelUnit"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property value="&quot;SITENAME&quot;" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory penWidth="0" showAxis="1" width="15" lineSizeType="MM" minimumSize="0" rotationOffset="270" penAlpha="255" spacing="5" height="15" enabled="0" spacingUnit="MM" spacingUnitScale="3x:0,0,0,0,0,0" diagramOrientation="Up" barWidth="5" sizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" penColor="#000000" backgroundAlpha="255" minScaleDenominator="0" scaleBasedVisibility="0" backgroundColor="#ffffff" maxScaleDenominator="1e+08" opacity="1" labelPlacementMethod="XHeight" scaleDependency="Area" direction="0" sizeScale="3x:0,0,0,0,0,0">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <axisSymbol>
        <symbol type="line" alpha="1" force_rhr="0" clip_to_extent="1" name="">
          <layer locked="0" enabled="1" pass="0" class="SimpleLine">
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" showAll="1" placement="1" linePlacementFlags="18" priority="0" obstacle="0" zIndex="0">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option type="double" value="0" name="allowedGapsBuffer"/>
        <Option type="bool" value="false" name="allowedGapsEnabled"/>
        <Option type="QString" value="" name="allowedGapsLayer"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field name="ogc_fid" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sitecode" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sitename" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ms" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sitetype" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="shape_leng" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="shape_area" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="em" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="url" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="ogc_fid" index="0"/>
    <alias name="" field="sitecode" index="1"/>
    <alias name="" field="sitename" index="2"/>
    <alias name="" field="ms" index="3"/>
    <alias name="" field="sitetype" index="4"/>
    <alias name="" field="shape_leng" index="5"/>
    <alias name="" field="shape_area" index="6"/>
    <alias name="" field="em" index="7"/>
    <alias name="" field="url" index="8"/>
  </aliases>
  <defaults>
    <default expression="" applyOnUpdate="0" field="ogc_fid"/>
    <default expression="" applyOnUpdate="0" field="sitecode"/>
    <default expression="" applyOnUpdate="0" field="sitename"/>
    <default expression="" applyOnUpdate="0" field="ms"/>
    <default expression="" applyOnUpdate="0" field="sitetype"/>
    <default expression="" applyOnUpdate="0" field="shape_leng"/>
    <default expression="" applyOnUpdate="0" field="shape_area"/>
    <default expression="" applyOnUpdate="0" field="em"/>
    <default expression="" applyOnUpdate="0" field="url"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="ogc_fid"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="sitecode"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="sitename"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="ms"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="sitetype"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="shape_leng"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="shape_area"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="em"/>
    <constraint exp_strength="0" constraints="0" notnull_strength="0" unique_strength="0" field="url"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="ogc_fid" exp=""/>
    <constraint desc="" field="sitecode" exp=""/>
    <constraint desc="" field="sitename" exp=""/>
    <constraint desc="" field="ms" exp=""/>
    <constraint desc="" field="sitetype" exp=""/>
    <constraint desc="" field="shape_leng" exp=""/>
    <constraint desc="" field="shape_area" exp=""/>
    <constraint desc="" field="em" exp=""/>
    <constraint desc="" field="url" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column type="field" hidden="0" width="-1" name="sitecode"/>
      <column type="field" hidden="0" width="-1" name="sitename"/>
      <column type="field" hidden="0" width="-1" name="sitetype"/>
      <column type="field" hidden="0" width="-1" name="ms"/>
      <column type="field" hidden="0" width="-1" name="url"/>
      <column type="actions" hidden="1" width="-1"/>
      <column type="field" hidden="0" width="-1" name="ogc_fid"/>
      <column type="field" hidden="0" width="-1" name="shape_leng"/>
      <column type="field" hidden="0" width="-1" name="shape_area"/>
      <column type="field" hidden="0" width="-1" name="em"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="em"/>
    <field editable="1" name="ms"/>
    <field editable="1" name="ogc_fid"/>
    <field editable="1" name="shape_area"/>
    <field editable="1" name="shape_leng"/>
    <field editable="1" name="sitecode"/>
    <field editable="1" name="sitename"/>
    <field editable="1" name="sitetype"/>
    <field editable="1" name="url"/>
  </editable>
  <labelOnTop>
    <field name="em" labelOnTop="0"/>
    <field name="ms" labelOnTop="0"/>
    <field name="ogc_fid" labelOnTop="0"/>
    <field name="shape_area" labelOnTop="0"/>
    <field name="shape_leng" labelOnTop="0"/>
    <field name="sitecode" labelOnTop="0"/>
    <field name="sitename" labelOnTop="0"/>
    <field name="sitetype" labelOnTop="0"/>
    <field name="url" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"sitename"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
