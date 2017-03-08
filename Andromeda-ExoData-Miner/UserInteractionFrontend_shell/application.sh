#!/bin/bash

#KO: delete sfork directory as to retrieve a new copy of OEC repo each time
if [ ! -d "sfork" ]; then
    mkdir sfork
else
    rm -rf sfork
    mkdir sfork
fi
cd sfork
git clone https://github.com/roy-samson13/open_exoplanet_catalogue.git
cd ..

echo " ---------------- ALL CHANGES ------------------- "
#KO: to check both folders
diff -r -q sfork/open_exoplanet_catalogue/systems mfork/open_exoplanet_catalogue/systems
diff -r -q sfork/open_exoplanet_catalogue/systems_kepler mfork/open_exoplanet_catalogue/systems_kepler
echo "---------------------------------------------------------------------------------"
echo "[OPTION] If you would like to see the changes from one of these systems:"
echo "         Type the folder and system name (e.g. systems/11 Com.xml)" 
echo "         Otherwise, press 'n' to exit"
echo "---------------------------------------------------------------------------------"
read systemString

while [ "$systemString" != "n" ]
do
	#KO: systemString specifies the xml file as well as the folder it's in
	diff -c --suppress-common-lines sfork/open_exoplanet_catalogue/"$systemString" mfork/open_exoplanet_catalogue/"$systemString"

	echo "---------------------------------------------------------------------------------"
	echo "[OPTION] Do you want to accept or reject the changes?" 
	echo "[Accept] Type 'a' for accept"
	echo "[REJECT] Type 'r' for reject"
	read input_str
	
	if [ "$input_str" = "a" ]
	then
		# using --force for cp so there is no need to prompt the user again 
		cp -f mfork/open_exoplanet_catalogue/"$systemString"  sfork/open_exoplanet_catalogue/"$systemString"
		echo "[UPDATE] SYSTEM $systemString has been ACCEPTED. ----- "
		
	fi

	if [ "$input_str" = "r" ]
	then
		
		echo "[UPDATE] SYSTEM $systemString has been rejected. ----- "
	fi

	echo "---------------------------------------------------------------------------------"
	echo "[OPTION] To see changes for another system:"
	echo "         Type its folder and name (e.g. systems/11 Com.xml)" 
	echo "         Otherwise, Press 'n' to exit"
	read systemString
done
