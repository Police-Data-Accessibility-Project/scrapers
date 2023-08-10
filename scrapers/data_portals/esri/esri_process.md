There's no script or scraper to do this yet, but you can run this manual process with utilities to convert an endpoint to usable data.

# Manual process
If you have an Esri REST endpoint, you can get a .geojson file and turn that into a CSV. You need to be in a layer of the REST API for it to work. For example: http://gismaps.oaklandca.gov/oaklandgis/rest/services/callforservice_2015_FC/FeatureServer/0

Here's one way to do it:

1. Use the "esri2geojson" utility to turn your REST endpoint URL into a .geojson file. https://github.com/openaddresses/pyesridump
2. Download QGIS (https://www.qgis.org/).
3. Open the .geojson file. You should see it appear as a layer.
4. Right click on the layer and export ("Save Features As...") to CSV.

### Further reading
https://developers.arcgis.com/rest/
