# UC4-Automic-AE-CLI-Binary-Repository

**Repository of all CLI Binaries (all compiled CLI projects)**

# Purpose:

provide a repository of **Command Line Interface Binaries** in order to extend the capabilities that the UI currently offers.

## Design:

**Each binary takes at least 2 possible flags/options:**
* **-help**: displays the list of AE Connection Parameters that can be specified (if overriding the parameters contained in connection.config file)
* **-h**:    displays the list of parameters (Mandatory, Optional etc.) required specifically for each binary
	
		 
**Each binary is designed to be SAFE: it will NOT modify / update / delete / create / execute anything UNLESS the -commit flag is added as a parameter.**
examples: 
OBJECTS_Delete.jar -name "*" => will NOT delete any objects, but instead will run a simulation of Objects to be deleted
	OBJECTS_Delete.jar -name "*" -commit => will delete ALL objects or ALL types (you should probably never use this command as-is ;)).
	TASKS_Operations.jar -f_name ".*" -f_status ".*aborted.*" -u_restart "*" => will NOT restart anything, but instead will run a simulation of Tasks to be restarted
	TASKS_Operations.jar -f_name ".*" -f_status ".*aborted.*" -u_restart "*" -commit => will restart ALL Tasks marked Aborted in the Activities Window	

**Most binaries have at least 2 sets of parameters available:**
* **-f_* **: Filter Parameters, parameters used to filter only specific objects (ex: -f_type "JOBS" or -f_title ".*[Mm]y [Tt]itle.*") => MOST f_* parameters support Regular Expressions
* **-u_* **: Update Parameters, parapeters used to update various things (ex: -u_process ["192.168.1.123","192.168.1.987"], or -u_title [".+","My New Title"], or -u_priority 100) => most parameters requiring ["A","B"] as a format will accept Regular Expressions for "A". "B" is the substitute String.  

**All binaries that have the ability to modify OBJECTS have the commit flag:**
* **-commit**: only add this commit once you are sure you want to carry out all modifications (running any command without -commit will run a simulation of all modifications)
	
**All Binaries leverage the Java Automic API Simplified Framework. Source Code can be found here:** https://github.com/brendanSapience/UC4-Automic---Java-API-Framework-Simplified
	
**All Binaries are self contained, all source code is available (see below), no guarantee is provided.**

## Compatibility:

	All Binaries compiled with most current version (v11.2) uc4.jar files (meaning it handles STORAGE, PERIOD, XML VARIABLE etc.)
	Most features (if not all) should work for at least v10 and v9, please test thoroughly in NON-PROD environments

## List of Binaries

	**## OBJECT Specific CLI Binaries:**

		* JOBF_Update.jar:      Update JOBF Objects. (ex: change the pattern for Destination File in all JOBF objects at once)
		* JOBP_Update.jar:      Update JOBP Objects. (ex: update all task names for all Workflows at once)
		* JOBS_SQL_Update.jar:  Update JOBS_SQL Objects (ex: modify the Database Connection name in all JOBS_SQL containing "*SQL1*" in their name)
		* JOBS_Update.jar:      Update JOBS Objects (ex: modify the name of a variable in all JOBS containing "*ABC*" in their title)

	**## GENERAL CLI Binaries:**

		* OBJECTS_Copy_Across_Clients.jar: Copy Objects Across Clients (v11 only for now).
		* OBJECTS_Create.jar: Create Objects of any type. (ex: create 200 JOBS Objects)
		* OBJECTS_Duplicate.jar: Duplicate Objects of any type. (ex: duplicate all objects matching name "*AB*PROD*" to "*AB*DEV*" at once)
		* OBJECTS_Execute: Execute now or schedule later (executable) Objects. (ex: run now all JOBP matching name "*DEV*JOBP*")
		* OBJECTS_List: -- Legacy Binary. Does not do much.
		* OBJECTS_Move: Move Objects of any type anywhere (within the same client) (ex: move all objects matching "*PROD*ABC*" to Folder "SANDBOX")
		* OBJECTS_Rename: Rename Objects of any type (ex: rename objects with title matching ".*Legacy.*" from "*ALPHA*" to "*BETA*")
		* OBJECTS_Show: -- Legacy Binary. Does not do much.
		* TASKS_Operations: Handle Operations on Activities Window (Deactivate all "Completed" tasks, restart aborted JOBS tasks with title matching ".*DEV.*")
		* UTIL_ClientAudit: Extract an Audit Report on Specific Client Usage (ex: number of active objects defined, etc.) 
		* UTIL_EnvironmentAudit: Extract Environment Wide Usage Report (ex: number of clients defined, etc.)

## CONFIGURATION Files:

	connection.config: contains connection parameters. This file is used by all binaries. All the parameters specified in it can be overriden when using any of the binaries. use -help flag to review override parameters.
