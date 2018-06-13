# Shell L1 Driver Standard

**Creation and configuration of the driver's environment:**

1. Start a new project with [shellfoundry](https://github.com/QualiSystems/shellfoundry):
```bash
$ shellfoundry new DriverName --template layer-1-switch
```
2. Create a new Python virtualenv in the project's folder. Specify the same python executable which is used by CloudShell.
```bash
virtualenv --python="c:\Program Files (x86)\QualiSystems\CloudShell\Server\python\2.7.10\python.exe" --always-copy .\cloudshell-L1-DriverName
```
3. Activate the project's virtualenv
```bash
.\cloudshell-L1-DriverName\Scripts\activate.bat
```
4. Edit and install requirements (from the new project folder):
```bash
$ pip install -r requirements.txt

```
**Implementation:**

1. Implement methods of the DriverCommands class in <project_slug>/driver_commands.py. Follow the [DEVGUIDE](https://github.com/QualiSystems/shell-L1-standard/blob/dev/DEVGUIDE.md) and docstrings with description, as an example of an L1 driver with CLI usage you can reffer to the [cloudshel-L1-mrv](https://github.com/QualiSystems/cloudshell-L1-mrv) project.
To debug the driver use the [DEBUGGING GUIDE](https://github.com/QualiSystems/shell-L1-template/blob/dev/DEBUGGING.md).

2. Update the driver version and metadata in version.txt


**Install the driver and compile the driver executable:**
1. Copy the project's folder *Cloudshell-L1-DriverName* to the drivers folder (usually "C:\\Program Files (x86)\\QualiSystems\\CloudShell\\Server\\Drivers").
2. Compile the driver executable:
    * Download [Bat To Exe](http://www.f2ko.de/en/b2e.php) Converter
    * Open *bat To Exe Converter*
    * Select *Batch File:* from the project's folder. For example *cloudshell-L1-DriverName\\DriverName.bat*
    * Specify *Save As:* the drivers location with the driver's executable name. For example *C:\\Program Files (x86)\\QualiSystems\\CloudShell\\Server\\Drivers\\DriverName.exe*
    * Specify *Architecture*
    * Press *Compile*

**Test in CloudShell:**
1. [Follow this guide](http://help.quali.com/Online%20Help/8.3/Portal/Content/Admn/Cnct-Ctrl-L1-Swch.htm) to import the new datamodel, create a resource, set the timeout period, auto load it and configure its physical connections
  * When you execute the auto load (or any other command later), the log files will get created under the Server\\Logs folder
2. After validating the auto load, you can validate the mapping functions either from Resource Manager or in the CloudShell Portal, [build a blueprint](http://help.quali.com/Online%20Help/8.3/Portal/Content/CSP/LAB-MNG/Rsc-Cnct/Phys-Ntwrk-Crt.htm) with 2 resources and a route, then reserve this blueprint and connect the route.


**Build and extract the driver package (not necessary)**
1. Build the package:
    * Create new zip archive, *DriverName.zip*
    * Put there the project's folder, *C:\\Program Files (x86)\\QualiSystems\\CloudShell\\Server\\Drivers\\Cloudshell-L1-DriverName*
    * Put there the driver's executable, *C:\\Program Files (x86)\\QualiSystems\\CloudShell\\Server\\Drivers\\DriverName.exe*
2. Extract the package:
    * Extract the driver package to the Drivers folder *C:\\Program Files (x86)\\QualiSystems\\CloudShell\\Server\\Drivers*

