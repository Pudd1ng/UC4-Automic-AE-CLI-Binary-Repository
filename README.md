# UC4-Automic-AE-CLI-Binary-Repository

**Repository of all CLI Binaries (all compiled CLI projects)**

# Improvement / Feature Requests
Feel free to open "issues" (even if they arent issues) on this page to request improvements & features.

# Purpose:

provide a repository of **Command Line Interface Binaries** in order to extend the capabilities that the UI currently offers.

## Design:

**Each binary takes at least 2 possible flags/options:**
* **-help**: displays the list of AE Connection Parameters that can be specified (if overriding the parameters contained in connection.config file)
* **-h**:    displays the list of parameters (Mandatory, Optional etc.) required specifically for each binary

## Connection Parameters:

**Each binary needs to establish a connection to the Automation Engine. The connection parameters can be set either:**
* directly in the **connection.config** file
* in any other config file of your choice
* via CLI parameters (see **-help** option for list of available parameters: **-L login -W password -C client -D department -H hostname -P port -F filename ** etc.)
* Note: IF a parameter is specified both in connection.config and via a CLI parameter, the CLI parameter takes precedence. 
* Note: the Password can be passed in encrypted form both in the config file and thru the command line (see usage of ucybcryp.exe to encrypt your password)

## CONFIGURATION Files:

* **connection.config**: contains connection parameters. This file is used by all binaries. All the parameters specified in it can be overriden when using any of the binaries. use -help flag to review override parameters. Alternatively, you can create several config files and use the -F flag to use a specific one.
	
## Safety:

Each binary is designed to be SAFE and comes with a **mandatory COMMIT mechanism**: it will NOT modify / update / delete / create / execute anything **UNLESS the -commit flag is added as a parameter.**
## examples: 
* OBJECTS_Delete.jar -name "*" => will NOT delete any objects, but instead will run a simulation of Objects to be deleted
* OBJECTS_Delete.jar -name "*" -commit => will delete ALL objects or ALL types (you should probably never use this command as-is ;)).
* TASKS_Operations.jar -f_name ".*" -f_status ".*aborted.*" -u_restart "*" => will NOT restart anything, but instead will run a simulation of Tasks to be restarted
* TASKS_Operations.jar -f_name ".*" -f_status ".*aborted.*" -u_restart "*" -commit => will restart ALL Tasks marked Aborted in the Activities Window	

## Common Active Parameters: 

**Most binaries have at least 2 sets of parameters available:**
* **-f_**: Filter Parameters, parameters used to filter only specific objects (ex: -f_type "JOBS" or -f_title ".*[Mm]y [Tt]itle.*") => MOST f_* parameters support Regular Expressions
* **-u_**: Update Parameters, parapeters used to update various things (ex: -u_process ["192.168.1.123","192.168.1.987"], or -u_title [".+","My New Title"], or -u_priority 100) => most parameters requiring ["A","B"] as a format will accept Regular Expressions for "A". "B" is the substitute String.  

## Other information: 

* **All Binaries leverage the Java Automic API Simplified Framework. Source Code can be found here:** https://github.com/brendanSapience/UC4-Automic---Java-API-Framework-Simplified
	
* **All Binaries are self contained, all source code is available (see below), no guarantee is provided.**

## Compatibility:

	* Requires Java v1.6 minimum.
	* All Binaries compiled with most current version (v12.0) uc4.jar files (meaning it handles new objects like STORAGE, PERIOD, XML VARIABLE etc.)
	* All Binaries (unless indicated) are compatible with AE v9 and up, a version check is automatically performed before each command for safety.
	* It is strongly advised to test thoroughly in NON-PROD environments.

## List of Binaries:

	**## OBJECT Specific CLI Binaries:**

		* CALE_Update.jar: Update / import CALE Objects from JSON files. 
		* AGENTS_Management.jar: Manage Agents from Client 0 (assign to other clients, delete, etc.) (ex: allow all clients to use Agent WIN01 for Execution)
		* HOSTGROUPS_Management.jar: Manage Hostgroups (add agents, run simulations, remove agents, etc.)
		* CHANGES_Show.jar: 	Display content of Audit Trail with filters (needs to be activated in Client 0 first)	
		* CONN_Update.jar:	Update CONN Objects (including RA CONN such as SOAP or REST CONNs)
		* JOBS_RA_Update.jar:	Update RA Jobs (SOAP, REST, FTP, etc.)
		* JSCH_Update.jar:	Update SCHED Objects
		* LOGIN_Update.jar:	Update LOGIN Objects
		* STORAGE_Update.jar:	Update STORAGE Objects (only v11.2 and up)
		* TASKS_Operations.jar: Handle Operations on Activities Window (Deactivate all "Completed" tasks, restart aborted JOBS tasks with title matching ".*DEV.*")
		* USER_Update.jar:	Update USER Objects
		* VARA_SQL_Update.jar:	Update SQL VARA Objects
		* VARA_SQLI_Update.jar:	Update SQLI VARA Objects
		* VARA_STATIC_Update.jar: Update STATIC & XML VARA Objects (XML VARA is a subtype of STATIC)
		* VARA_Update.jar:	Update General Properties of VARA Objects
		* JOBF_Update.jar:      Update JOBF Objects. (ex: change the pattern for Destination File in all JOBF objects at once)
		* JOBP_Update.jar:      Update JOBP Objects. (ex: update all task names for all Workflows at once)
		* JOBS_SQL_Update.jar:  Update JOBS_SQL Objects (ex: modify the Database Connection name in all JOBS_SQL containing "*SQL1*" in their name)
		* JOBS_Update.jar:      Update JOBS Objects (ex: modify the name of a variable in all JOBS containing "*ABC*" in their title)

	**## GENERAL CLI Binaries:**

		* OBJECTS_Delete.jar: Delete Objects of any type. (with regular expressions...)
		* OBJECTS_Create.jar: Create Objects of any type. (ex: create 200 JOBS Objects)
		* OBJECTS_Duplicate.jar: Duplicate Objects of any type. (ex: duplicate all objects matching name "*AB*PROD*" to "*AB*DEV*" at once)
		* OBJECTS_Export_Import.jar: Import & Export Objects and dependencies (v11.2 and up)
		* OBJECTS_Execute.jar: Execute now or schedule later (executable) Objects. (ex: run now all JOBP matching name "*DEV*JOBP*")
		* OBJECTS_Move.jar: Move Objects of any type anywhere (within the same client) (ex: move all objects matching "*PROD*ABC*" to Folder "SANDBOX")
		* OBJECTS_Rename.jar: Rename Objects of any type (ex: rename objects with title matching ".*Legacy.*" from "*ALPHA*" to "*BETA*")
		* UTIL_ClientAudit.jar: Extract an Audit Report on Specific Client Usage (ex: number of active objects defined, etc.) 
		* UTIL_EnvironmentAudit.jar: Extract Environment Wide Usage Report (ex: number of clients defined, etc.)
		* UTIL_SystemOverview_Show.jar: Extract Content of the System Overview into a parsable format (JSON)
		
		

