<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd">
  <!-- LAYER NAME level212_cartridge_density -->
  <NamedLayer>
    <Name>NAME GOES HERE</Name>
    <UserStyle>
      <FeatureTypeStyle>
        <Rule>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#d4cfc7</CssParameter>
            </Fill>
            <CssParameter>
              <CssParameter name="stroke">#d4cfc7</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </CssParameter>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>0.02709</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>1.59921</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>circle</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#336699</CssParameter>
                </Fill>
              </Mark>
              <Size>6</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>1.59921</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>4.08169</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>circle</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#336699</CssParameter>
                </Fill>
              </Mark>
              <Size>8</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>4.08169</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>7.43736</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>circle</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#336699</CssParameter>
                </Fill>
              </Mark>
              <Size>11</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>7.43736</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>12.39746</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>circle</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#336699</CssParameter>
                </Fill>
              </Mark>
              <Size>13</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>12.39746</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>22.5901</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>circle</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#336699</CssParameter>
                </Fill>
              </Mark>
              <Size>16</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>22.5901</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:PropertyName>qrycaden.cartridge</ogc:PropertyName>
                <ogc:Literal>39.61484</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>circle</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#336699</CssParameter>
                </Fill>
              </Mark>
              <Size>18</Size>
            </Graphic>
          </PointSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
