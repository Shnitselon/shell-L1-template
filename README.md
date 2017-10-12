# Shell L1 Driver Standard

**Usage:**

1. Start a new project with [shellfoundry](https://github.com/QualiSystems/shellfoundry):
```bash
$ shellfoundry new DriverName --template layer-1-switch
```
2. Install requirements (from the new project folder):
```bash
$ pip install -r requirements.txt

```

3. Implement methods of DriverCommands class in <project_slug>/driver_commands.py. Follow [DEVGUIDE](https://github.com/QualiSystems/shell-L1-standard/blob/dev/DEVGUIDE.md) and docstrings with description, as an example of L1 driver with CLI usage you can use [cloudshel-L1-mrv](https://github.com/QualiSystems/cloudshell-L1-mrv)

4. Update the driver version and metadata in version.txt

**Compile the driver:**

1. download required packages from requirements.txt and uncompress them at the same level as the project folder (next to it). Note: [cloudshell-core](https://github.com/QualiSystems/cloudshell-core) and [cloudshell_l1_networking_core](https://github.com/QualiSystems/cloudshell-L1-networking-core) are required packages and must have the next paths:

cloudshell-core package: "../cloudshell-core"

cloudshell_l1_networking_core package: "../cloudshell-L1-networking-core"

2. [install pyinstaller](http://pyinstaller.readthedocs.io/en/latest/installation.html):
```bash
$ pip install pyinstaller

```

3. run compile_driver.bat (the compiled driver will be created in a "dist" directory)

**Test in CloudShell:**

1. Copy the compiled driver and the <DRIVER_NAME>_RuntimeConfiguration.yml to the Drivers folder (usually "C:\\Program Files (x86)\\QualiSystems\\CloudShell\\Server\\Drivers")

2. [Follow this guide](http://help.quali.com/Online%20Help/8.1.0.4291/Portal/Content/Admn/Cnct-Ctrl-L1-Swch.htm) to import the new datamodel, create a resource, set the timeout period, auto load it and configure its physical connections

  * When you execute the auto load (or any other command later), the log files will get created under the Server\\Logs folder

3. After validating the auto load, you can validate the mapping functions either from Resource Manager or in the CloudShell Portal, [build a blueprint](http://help.quali.com/Online%20Help/8.1.0.4291/Portal/Content/CSP/LAB-MNG/Rsc-Cnct/Phys-Ntwrk-Crt.htm) with 2 resources and a route, then reserve this blueprint and connect the route.
