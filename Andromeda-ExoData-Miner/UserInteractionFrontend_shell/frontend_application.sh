#!/bin/bash

mkdir sfork
cd sfork
git clone https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue.git
cd ..
touch -f lastupdate.txt
echo $(date +%F) > lastupdate.txt   #for temporary testing

echo " ---------------- ALL CHANGES ------------------- "
#KO: to check both folders
diff -r -q sfork/open_exoplanet_catalogue/systems mfork/open_exoplanet_catalogue/systems
diff -r -q sfork/open_exoplanet_catalogue/systems_kepler mfork/open_exoplanet_catalogue/systems_kepler
echo "---------------------------------------------------------------------------------"
echo "If you would like to see the changes from one of these systems:"
echo "type the folder and system name (e.g. systems/11 Com.xml)" 
echo "Otherwise, press 'n' to exit"
echo "---------------------------------------------------------------------------------"
read systemString

while [ "$systemString" != "n" ]
do
	#KO: systemString specifies the xml file as well as the folder it's in
	diff -c --suppress-common-lines sfork/open_exoplanet_catalogue/"$systemString" mfork/open_exoplanet_catalogue/"$systemString"
	echo "---------------------------------------------------------------------------------"
	echo "[OPTION] To see another system, type its name (e.g. '11 Com.xml')" 
	echo "Otherwise, Press 'n' to exit. "
	read systemString
done

echo "---------------------------------------------------------------------------------"
echo "[OPTION] If you would like to modify one of these suggested updates: "
echo "Type the name of the system (e.g. '11 Com.xml')." 
echo "Otherwise, press 'n' to exit"
echo "---------------------------------------------------------------------------------"
read systemString2

while [ "$systemString2" != "n" ]
do
	
	# SUHAILAH's CODE: 
	# Getting user input
	echo "---------------------------------------------------------------------------------"
	echo "[OPTION] Do you want to accept or reject the changes?" 
	echo "[Accept] Type 'a' for accept, [REJECT] type 'r' for reject"
	read input_str
	
	if [ "$input_str" = "a" ]
	then
	# using --force for cp so there is no need to prompt the user again
		cp -f sfork/open_exoplanet_catalogue/systems/"$systemString2"  mfork/open_exoplanet_catalogue/systems/"$systemString2" 
		echo "[UPDATE] SYSTEM $systemString2 has been ACCEPTED. ----- "
	
	fi
	
	if [ "$input_str" = "r" ]
	then
		echo "[UPDATE] SYSTEM $systemString2 has been rejected. ----- "
	fi
	
	echo "---------------------------------------------------------------------------------"	
	echo "[OPTION] Would you like to modify another system:"
	echo "type the name of the system (e.g. 11 Com.xml)"
	echo "Otherwise, press 'n' to exit"	
	echo "---------------------------------------------------------------------------------"
	read systemString2
done 



#echo "would you like to issue a pull request based on this update?"
#read pullRequest

#if [ $(pullRequest) -eq 'y' ]
#	git push
#fi
#echo $(date +%F) > lastupdate.txt
