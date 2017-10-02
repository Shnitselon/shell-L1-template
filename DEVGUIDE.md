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

### Driver commands

#### Login
Opens new session to the device, called before each command tuple

**Attributes**
* *Address* - IP address of the device
*  *User* - Login username
*  *Password* - Password

**Example of implementation**
```python
    def login(self, address, username, password):
        # Define session attributes
        self._cli_handler.define_session_attributes(address, username, password)
        
        #open session and execute command
        with self._cli_handler.default_mode_service() as session:
            system_actions = SystemActions(session, self._logger)
            self._logger.info(system_actions.device_info())
```


#### GetStateId
Checks synchronization state with CloudShell, if state_id is different, then CloudShell and device is not synchronized. Return -1 if not used.

#### SetStateId
Set synchronization state id to the device, it calls after any change done

**Attributes**
* *StateId* - Id

### Basic modules and classes
* **Module main** *main.py* - Enter point of the driver, initialize and start driver.
* **Class DriverCommands** *driver_commands.py* - Main driver class, implements [DriverCommandsInterface](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/driver_commands_interface.py), one method for each driver command.
* **Class [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py)** - Extract attributes from the command request and execute specific method of the DriverCommands class implemented for this specific driver command.
* **Class [DriverListener](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/driver_listener.py)** - Listen for the new connections from the CloudShell.
* **Class [ConnectionHandler](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/connection_handler.py)** - Handle new connection, read requests and send responses.

### How it works
1. CloudShell starts driver executable with port value as an argument ```L1_DRIVER.exe 4000```. It unpack interpreter with libraries into local virtual environment, then starts ```main.py``` with arguments.
2. Module ```main``` reads runtime configuration, initializes instances of loggers, implemented DriverCommands class, [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py), and [DriverListener](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/driver_listener.py), then start listening new connections. 
3. When driver started, CloudShell initiate new connection to the driver and send XML command tuple. Each command tuple has Login command at the beginning.
4. New connections handles by [ConnectionHandler](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/connection_handler.py).
    * Read request data from the socket
    * Parse request data by [RequestParser](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/requests_parser.py) and creates list of [CommandRequest](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/command_request.py) objects.
    * Execute list of [CommandRequest](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/command_request.py) by [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py)  
5. [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py) extract command_name and attributes for each [CommandRequest](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/command_request.py) instance, call method of implemented DriverCommands class defined for this command_name.
    * For each [CommandRequest](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/request/command_request.py) [CommandExecutor](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/command_executor.py) creates [CommandResponse](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/response/command_response.py) instance, which uses for generating response.
6. [ResponseInfo](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/response/response_info.py) has response_info attribute, it can be defined by [ResponseInfo](https://github.com/QualiSystems/cloudshell-L1-networking-core/blob/refactoring/cloudshell/layer_one/core/response/response_info.py) instance, which can be returned from methods of DriverCommands class.
 
### CLI Usage

#### Implementation of using CLI [DriverCommands](https://github.com/QualiSystems/cloudshell-L1-mrv/blob/model_fixes/mrv/driver_commands.py)
