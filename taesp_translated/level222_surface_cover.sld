<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd">
  <!-- LAYER NAME level222_surface_cover -->
  <NamedLayer>
    <Name>NAME GOES HERE</Name>
    <UserStyle>
      <FeatureTypeStyle>
        <Rule>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>tblguf.soilcov</ogc:PropertyName>
              <ogc:Literal>Sab</ogc:Literal>
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
          <ogc:Filter/>
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
              <ogc:PropertyName>tblguf.soilcov</ogc:PropertyName>
              <ogc:Literal>Sot</ogc:Literal>
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
              <ogc:PropertyName>tblguf.soilcov</ogc:PropertyName>
              <ogc:Literal>Shg</ogc:Literal>
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
              <ogc:PropertyName>tblguf.soilcov</ogc:PropertyName>
              <ogc:Literal>Smi</ogc:Literal>
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
              <ogc:PropertyName>tblguf.soilcov</ogc:PropertyName>
              <ogc:Literal>Sab</ogc:Literal>
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
              <ogc:PropertyName>tblguf.soilcov</ogc:PropertyName>
              <ogc:Literal>&lt;Null&gt;</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
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
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
