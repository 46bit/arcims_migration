<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd">
  <!-- LAYER NAME level220_erosion -->
  <NamedLayer>
    <Name>NAME GOES HERE</Name>
    <UserStyle>
      <FeatureTypeStyle>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Sheet</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#006600</CssParameter>
            </Fill>
            <CssParameter>
              <CssParameter name="stroke">#d4d0c8</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </CssParameter>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Non</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#00c800</CssParameter>
            </Fill>
            <CssParameter>
              <CssParameter name="stroke">#000000</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </CssParameter>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Cons</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#cccc99</CssParameter>
            </Fill>
            <CssParameter>
              <CssParameter name="stroke">#d4d0c8</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </CssParameter>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Push</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#cccc66</CssParameter>
            </Fill>
            <CssParameter>
              <CssParameter name="stroke">#d4d0c8</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </CssParameter>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Mix</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#999967</CssParameter>
            </Fill>
            <CssParameter>
              <CssParameter name="stroke">#d4d0c8</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </CssParameter>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Incise</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#669932</CssParameter>
            </Fill>
            <CssParameter>
              <CssParameter name="stroke">#d4d0c8</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </CssParameter>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Sheet</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">#d4d0c8</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </Stroke>
          </LineSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Till</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#003300</CssParameter>
            </Fill>
            <CssParameter>
              <CssParameter name="stroke">#d4d0c8</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </CssParameter>
          </PolygonSymbolizer>
        </Rule>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblGUF.Eros</ogc:PropertyName>
              <ogc:Literal>Non</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <LineSymbolizer>
            <Stroke>
              <CssParameter name="stroke">#d4d0c8</CssParameter>
              <CssParameter name="stroke-width">1</CssParameter>
            </Stroke>
          </LineSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
