# Shell L1 Driver Standard

**Creation and configuration of the driver environment:**

1. Start a new project with [shellfoundry](https://github.com/QualiSystems/shellfoundry):
```bash
$ shellfoundry new DriverName --template layer-1-switch
```
2. Create new Python virtualenv in the project folder. Specify the same python executable which used by CloudShell.
```bash
virtualenv --python="c:\Program Files (x86)\QualiSystems\CloudShell\Server\python\2.7.10\python.exe" --always-copy .\cloudshell-L1-DriverName
```
3. Activate projects virtualenv
```bash
.\cloudshell-L1-DriverName\Scripts\activate.bat
```
4. Edit and install requirements (from the new project folder):
```bash
$ pip install -r requirements.txt

```
**Implementation:**

1. Implement methods of DriverCommands class in <project_slug>/driver_commands.py. Follow [DEVGUIDE](https://github.com/QualiSystems/shell-L1-standard/blob/dev/DEVGUIDE.md) and docstrings with description, as an example of L1 driver with CLI usage you can use [cloudshel-L1-mrv](https://github.com/QualiSystems/cloudshell-L1-mrv)

2. Update the driver version and metadata in version.txt


**Compile the driver executable and build package:**
1. Download [Bat To Exe](http://www.f2ko.de/en/b2e.php) Converter
2. Compile *DriverName.bat* to *DriverName.exe*
4. Create new zip archive with *Cloudshell-L1-DriverName* project folder and *Cloudshell-L1-DriverName\DriverName.exe* executable, located at the same level as project folder.

**Test in CloudShell:**

1. Extract the driver package to Drivers folder (usually "C:\\Program Files (x86)\\QualiSystems\\CloudShell\\Server\\Drivers")

2. [Follow this guide](http://help.quali.com/Online%20Help/8.1.0.4291/Portal/Content/Admn/Cnct-Ctrl-L1-Swch.htm) to import the new datamodel, create a resource, set the timeout period, auto load it and configure its physical connections

  * When you execute the auto load (or any other command later), the log files will get created under the Server\\Logs folder

3. After validating the auto load, you can validate the mapping functions either from Resource Manager or in the CloudShell Portal, [build a blueprint](http://help.quali.com/Online%20Help/8.1.0.4291/Portal/Content/CSP/LAB-MNG/Rsc-Cnct/Phys-Ntwrk-Crt.htm) with 2 resources and a route, then reserve this blueprint and connect the route.
