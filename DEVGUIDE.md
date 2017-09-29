# L1 Driver Devguide
This guide is short review of python L1 driver and describes basic steps of developing new driver.

## L1 Driver Review

L1 driver is an application which is runing by CloudShell with a specific port like an argument "L1_DRIVER.exe 4000". 
It starts listening to a specified port and waits for a connection from the CloudShell. 
CloudShell communicate with the driver using XML commands.

**Request command example**
```xml
<Commands xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.qualisystems.com/ResourceManagement/DriverCommands.xsd">
    <Command CommandName="Login" CommandId="ae39207a-a65c-40e9-bec3-4996ddcef727">
        <Parameters xsi:type="LoginCommandParameters">
            <Address>192.168.42.240</Address>
            <User>admin</User>
            <Password>admin</Password>
        </Parameters>
    </Command>
</Commands>
```
**Response example**
```xml
<Responses xmlns="http://schemas.qualisystems.com/ResourceManagement/DriverCommandResult.xsd" Success="true">
    <CommandResponse CommandName="Login" Success="true" CommandId="ae39207a-a65c-40e9-bec3-4996ddcef727">
        <Error/>
        <Log/>
        <Timestamp>14.12.2016 11:41:52</Timestamp>
        <ResponseInfo/>
    </CommandResponse>
    <ErrorCode/>
    <Log>No need for Sync</Log>
</Responses>
```

### Commands description

#### Login
Opens new session to the device, called before each command tuple

**Attributes**
* *Address* - IP address of the device
*  *User* - Login username
*  *Password* - Password

#### GetStateId
Checks synchronization state with CloudShell, if state_id is different, then CloudShell and device is not synchronized. Return -1 if not used.

#### SetStateId
Set synchronization state id to the device, it calls after any change done

**Attributes**
* *StateId* - Id

...

### Basic files
* main.py - Enter pont of the driver, reads runtime configuration, initialize driver_commands, loggers and executor instances, start listening.
* driver_commands.py - Class DriverCommands implementations driver commands.

### How it works
CloudShell starts driver executable with port value as an argument ```L1_DRIVER.exe 4000```. It unpack interpreter with libraries into local virtual environment, then starts ```main.py``` with arguments.
```main.py``` module reads runtime configuration, initializes instances of loggers, driver commands, [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py), and [DriverListener](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/driver_listener.py), then start listening new connections. 
When driver started, CloudShell initiate new connection to the driver and send XML commands tuple. Each commands tuple has Login command at the beginning. 
New connections handles by [ConnectionHandler](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/connection_handler.py), xml request parses by [RequestParser](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/requests_parser.py) and creates list of [CommandRequest](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/command_request.py) objects.
Then [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py) handles each [CommandRequest](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/command_request.py) instance, it extracts command_name and call [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py) method defined for this command_name. It extracts attributes and calls methods of DriverCommands class defined for this driver command.
For each [CommandRequest](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/command_request.py) [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py) creates [CommandResponse](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/response/command_response.py) instance, which uses for generating response. It has response_info attribute which can be defined by [ResponseInfo](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/response/response_info.py) instance.
DriverCommands class methods can return [ResponseInfo](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/response/response_info.py) object if needed. 
Class DriverCommands - is a main drive class, it implements [DriverCommandsInterface](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/driver_commands_interface.py), each method handles driver command with a specific attributes, should be implemented. 