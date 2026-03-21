# Notice
[Arcpy now includes its own type stubs as of ArcGIS Pro 3.3](https://www.esri.com/arcgis-blog/products/arcgis-pro/developers/typehints-have-arrived-in-arcgis-pro-3-3), this project is being maintained for those using earlier versions or developing on machines without arcpy installed.

# Future Direction
- Improve existing stub files which are incomplete and contain errors
- Consider supporting stubs for different versions of arcpy
  - Consider if new native arcpy typing is backwards compatible with older arcpy versions (probably not)
    - possibility to use newer stubs to make older versions more complete or accurate
  - Test which tools generate most accurate stubs: mypy, pyright, based-pyright, etc
- Consider publishing to a package repository
- Consider mergeing into [python-typeshed](https://github.com/python/typeshed?tab=contributing-ov-file)


# ArcGIS Pro third-party library support

Third-party library version information is maintained in a spreadsheet [here](<./arcpy libraries by version.ods>).
