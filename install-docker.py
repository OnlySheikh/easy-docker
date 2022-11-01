import   os 

print ( "Welcome to Easy-Docker v1.0 (By: OnlySheikh)" ) 
#First, update your existing list of packages: 
aptgetUPDATE  =  'sudo apt-get update' 
os . system ( aptgetUPDATE ) 

#Next, install a few prerequisite packages which let apt use packages over HTTPS: 
isntallPackages  =  'sudo apt install apt-transport-https ca-certificates curl software-properties-common -y' 
os . system ( isntallPackages ) 

#Then add the GPG key for the official Docker repository to your system: 
GPGkey  =  'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -' 
os . system ( GPGkey ) 

#Add the Docker repository to APT sources: 
addRepository  =  'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"' 
os . system ( addRepository ) 

#Make sure you are about to install from the Docker repo instead of the default Ubuntu repo: 
Sure  =  'apt-cache policy docker-ce' 
os . system ( Sure ) 

#Finally, install Docker: 
print ( "###Enter 'y' and Press 'Enter' to countinue...###" ) 
installDocker  =  'sudo apt install docker-ce -y' 
os . system ( installDocker ) 

print ( "Thanks for Using Easy-Docker v1.0 (By:OnlySheikh)" ) 
print ( "Your Docker Installed Successfully! Enjoy Your Docker... :D" ) 
print ( "Visit my profile on github: https://github.com/OnlySheikh/" ) 
print ( "" ) 

dockerPS  =  'sudo docker ps' 
os . system ( dockerPS )
