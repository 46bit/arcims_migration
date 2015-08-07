/* (c) 2014 Open Source Geospatial Foundation - all rights reserved
 * (c) 2001 - 2013 OpenPlans
 * This code is licensed under the GPL 2.0 license, available at the root
 * application directory.
 */

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

import org.apache.commons.io.IOUtils;
import org.geoserver.catalog.SLDHandler;
import org.geoserver.catalog.Styles;
import org.geotools.styling.Style;
import org.geotools.styling.StyledLayerDescriptor;
import org.geotools.styling.css.CssParser;
import org.geotools.styling.css.CssTranslator;
import org.geotools.styling.css.Stylesheet;

public class CSS2SLD
{
    public static void main(String [] args)
    {
        try {
            BufferedReader inp = new BufferedReader(new InputStreamReader(System.in));

            Stylesheet styleSheet = CssParser.parse(IOUtils.toString(inp));
            Style style = (Style) new CssTranslator().translate(styleSheet);
            StyledLayerDescriptor sld = Styles.sld(style);
            String sld_string = Styles.string(sld, new SLDHandler(), null, true);

            System.out.println(sld_string);
        } catch (IOException e) {}
    }
}
