# Layer 1 Driver Debugging

This guide is a short review of Python Layer 1 (L1) driver debugging process.


* ## Run PyCharms as SYSTEM
To attach PyCharms debugger to the driver process called by CloudShell it should be run as SYSTEM.
An easy way to get a CMD prompt as SYSTEM is to grab [PSEXEC](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) from Microsoft Sysinternals:

1. Download [PSEXEC](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) and unzip to some folder.
2. Open an elevated CMD prompt as an administrator.
3. Navigate to the folder where you unzipped PSEXEC.EXE
4. Run:
```cmd
     PSEXEC -i -s -d CMD
```
You will have a new CMD prompt open, as SYSTEM

6. Run PyCharms in opened CMD:
```cmd
C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2016.1.4\bin\pycharm.exe
```

* ## Open the driver as a Project in PyCharms and configure interpreter 
1. Press Open and specify driver folder, like *C:\Program Files (x86)\QualiSystems\CloudShell\Server\Drivers\cloudshell-L1-driver_example*
2. Specify Project interpreter from the driver virtualenv. Set python executable from the driver folder, like *C:\Program Files (x86)\QualiSystems\CloudShell\Server\Drivers\cloudshell-L1-fiberzone_afm\Scripts\python.exe*


* ## Run driver in a debug mode
1. Edit Runtime Configuration of the driver *C:\Program Files (x86)\QualiSystems\CloudShell\Server\Drivers\cloudshell-L1-driver_example\driver_example_RuntimeConfig.yml*
2. Specify *DEBUG_ENABLED* option to *TRUE*
```yaml
DEBUG_ENABLED: TRUE
```
3. Kill python process of the driver. Find PID of the driver process in the commands log and kill it in the Task Manager.

* ## Attach PyCharms debugger to the driver process
1. Specify breakpoints in sources of the driver project.
2. Use CloudShell to call driver commands. For example, call *Autoload* in ResourceManager. 
3. Find in the commands log of the driver, PID of the driver process.
4. Attach PyCharms debugger to the driver process. In PyCharms press *Run>Attach to LocalProcess* and choose process with the same PID you found in the commands log.
5. Wait when it stops on the breakpoint.