#!/bin/bash

echo "--------------------------------------------"
echo "[USER HOMEPAGE] Welcome: main"
# echo "[OPTION] TO CHECK FOR UPDATES FROM NASA & EU CATALOGS: type '1'"
echo "[OPTION] TO VIEW THE UPDATES AND ACCEPT/REJECT CHANGES MADE: type '2' "
echo "[OPTION] TO GO BACK TO USER HOMEPAGE: type '3'"
echo "[OPTION] TO MAKE A PULL REQUEST: type '4'"
echo "[OPTION] TO EXIT THE SYSTEM: press '0' "
read input_str

while [ "$input_str" -ne 0 ]

do
#	if [ "$input_str" -eq 1 ]
#	then
#		echo "CHECKING FOR UPDATES :"
#		echo " Um . okay fix this"
#	fi

	if [ "$input_str" -eq 2 ]
	then
		echo "VIEWING UPDATES AND ACCP"
		echo "--------------------------------------------"
		sh ./application.sh
	fi

	if [ "$input_str" -eq 3 ]
	then
		echo "GOING BACK TO USER HOMEPAGE"
		echo "[REMINDER] YOU HAVE TO LOG IN AGAIN"
		sh ./start_up.sh
	fi 

	if [ "$input_str" -eq 4 ]
	then
		cd sfork/open_exoplanet_catalogue
		git add .
		git commit -m "modified oec files"
		git push
		hub pull-request -b DanielMatu:master
		cd ..
		cd ..
	fi 

	echo "--------------------------------------------"
	echo "[USER HOMEPAGE] Welcome: main"
	echo "[OPTION] TO CHECK FOR UPDATES FROM NASA & EU CATALOGS: type '1'"
	echo "[OPTION] TO VIEW THE UPDATES AND ACCEPT/REJECT CHANGES MADE: type '2' "
	echo "[OPTION] TO GO BACK TO USER HOMEPAGE: type '3'"
	echo "[OPTION] TO MAKE A PULL REQUEST: type '4'"
	echo "[OPTION] TO EXIT THE SYSTEM: press '0' "	
	read input_str

done

exit 0


