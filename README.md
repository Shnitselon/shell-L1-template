# Shell L1 Driver Standard

Usage:

Start new shell with [shellfoundry](https://github.com/QualiSystems/shellfoundry):
```bash
$ shellfoundry new DriverName --template layer-1-switch
```
Install requirements:
```bash
$ pip install -r requirements.txt

```

Implement all driver functions in driver_handler.py module

Compile driver to exe file using pyinstaller:

- download required packages from requirements.txt and uncompress them at the same level as driver. Note: [cloudshell-core](https://github.com/QualiSystems/cloudshell-core) and [cloudshell_l1_networking_core](https://github.com/QualiSystems/cloudshell-L1-networking-core) are required packages and must have next pathes:
cloudshell-core package: "../cloudshell-core"
cloudshell_l1_networking_core package: "../cloudshell-L1-networking-core"

- [install pyinstaller](http://pyinstaller.readthedocs.io/en/latest/installation.html)

- run compile_driver.bat (Driver exe file will appear in "dist" directory)
