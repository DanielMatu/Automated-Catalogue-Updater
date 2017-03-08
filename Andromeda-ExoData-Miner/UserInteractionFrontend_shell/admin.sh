#!/bin/bash

echo "--------------------------------------------"
echo "[USER HOMEPAGE] Welcome: admin"
# echo "[OPTION] TO CHECK FOR UPDATES FROM NASA & EU CATALOGS: type '1'"
echo "[OPTION] TO VIEW THE CHANGES MADE: type '2' "
echo "[OPTION] TO GO BACK TO ADMIN HOMEPAGE: type '3'"
echo "[OPTION] TO EXIT THE SYSTEM: press '0' "
echo "ENTER: "
read inputString

while [ "$inputString" -ne 0 ]
do
	#if [ "$inputString" -eq 1 ]
	#then
		#echo "--------------------------------------------"
		#echo "CHECKING FOR UPDATES"
		#echo " Um . okay needa fix this crap ---- "
		
	
	# fi
	
	if [ "$inputString" -eq 2 ]
	then
		echo "--------------------------------------------"
		echo "VIEWING THE CHANGES MADE"
		sh ./frontend_admin.sh
		
	fi

	if [ "$inputString" -eq 3 ]
	then
		echo "GOING BACK TO ADMIN HOMEPAGE"
		echo "[REMINDER] YOU HAVE TO LOG IN AGAIN"
		sh ./start_up.sh
	fi
	
	echo "--------------------------------------------"
	echo "[USER HOMEPAGE] Welcome: admin"
	# echo "[OPTION] TO CHECK FOR UPDATES FROM NASA & EU CATALOGS: type '1'"
	echo "[OPTION] TO VIEW THE CHANGES MADE: type '2' "
	echo "[OPTION] TO GO BACK TO ADMIN HOMEPAGE: type'3'"
	echo "[OPTION] TO EXIT THE SYSTEM : press '0' "
	read inputString
	
done

exit 0
