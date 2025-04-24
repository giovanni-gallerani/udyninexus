# udyninexus

## 1. Introduction
**udyninexus** is Python package for easy NeXus files creation made for [UdynI laboratory](https://www.udyni.eu/).  

This package makes the user able to create [NeXus files](https://www.nexusformat.org/) without the need to know how they are structured internally by using a simple class system instead of neeeding to learn the tree structure requred by the standard.  
In short this package provide a level of abstraction on the NeXus file implementation, enabling researcher to develop custom made acquisition scripts for different experimental station in a simpler way.

This first release of the packages saves data using an implementation of [NXoptical_spectroscopy](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXoptical_spectroscopy.html#nxoptical-spectroscopy) application definition.  
See `/NXoptical_spectroscopy_UdynI.pdf` for more details about the specific fields of the implementation used in the lab.


## 2. Using the package
In order to use the package just copy the `/udyninexus/` folder to system or project's include path.

### Installing requirements
You can install the requirements for the package by copying `/requirements.txt` and running the following command:
```bash
pip install -r requirements.txt
```

### Usage example
This package provides:
- A set of classes for creating the different components of the NeXus file.
- A function to save the NeXus file, provided with custom exceptions.
- Two functions for setting log level and a log file for the package.

For a usage example comprehensive of all the functionality of the package see `/example.py`.

## 3. Future developments
In the future the package could be extended with new functionalities.
- Add parameters in write_nexus function for specifying compression.
- Support for more types of instruments for creating better docuemented measurements. For now only Beam, Source, Detector are supported. There are plans for adding moving parts, that would be used in most of Axis reference attribute (an attribute that associates an instrument to an axis).
- Create methods for editing 'definition' attribute in NexusDataContainer class. For now it's hardcoded in the write_nexus function since the lab is planning to only use the implementation of NXoptical_spectroscopy described in `/NXoptical_spectroscopy_UdynI.pdf`.