# Description
This project contains type stub .pyi files for `arcpy`. This makes development of ArcGIS Pro scripts smoother by providing editors with type information for linting and code completion. 

[Arcpy now includes its own type stubs as of ArcGIS Pro 3.3](https://www.esri.com/arcgis-blog/products/arcgis-pro/developers/typehints-have-arrived-in-arcgis-pro-3-3), but this project will be maintained as an easy entry-point for setting up type stubs in editors unable to access library information inside your ArcGIS Pro conda environment or on machines without ArcGIS Pro installed.

# Installation
Type stub .pyi files can be used by cloning the repository into the root of the project into a folder named `arcpy` by running:
```
cd SWCD-Tools/
git clone git@github.com:bcmertz/arcpy-typestubs.git arcpy
```

After cloning the repo, check the branch of the arcpy version you are running:
```
git checkout 3.x
```

# Supported arcpy versions
This project currently has type stubs for arcpy 3.3 and 3.4

# Creating type stub
- add mypy to default arcgispro conda environment (arcgispro-py3)
- open arcgis pro python command prompt
- stubgen -p arcpy -o <output folder>


If arcgis pro is a more recent version than the arcpy library listed by anaconda and version errors occur:
- open python command prompt (https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/upgrade-an-environment.htm)
- switch to a non-default conda environment (not arcgispro-py3)
- run `conda proup -n <default environment-name>`
- then proceed with regular generation of type stubs

# ArcGIS Pro third-party library support
Third-party library version information is maintained in a spreadsheet [here](<./arcpy libraries by version.ods>).

# Future Direction
- Improve existing stub files which are incomplete and contain errors
  - Test which tools generate most accurate stubs: [stubgen](https://github.com/python/typeshed/blob/main/scripts/create_baseline_stubs.py), or [other](https://typing.python.org/en/latest/guides/writing_stubs.html)
- Consider supporting stubs for different versions of arcpy
- Consider if new native arcpy typing is backwards compatible with older arcpy versions (probably not)
  - possibility to use newer stubs to make older versions more complete or accurate
- Consider publishing to a package repository
- Consider merging into [python-typeshed](https://github.com/python/typeshed?tab=contributing-ov-file)
