# BaseBSPython
logiciel de base du soft pyhton pour ev3dev. Sera à instancier pour chaque robot
# Astuces Git
On utilise Visual Studio Code
Installer Visual Studio Code
Installer l’extension pour ev3dev
Faire un download (ou pull) du code Brickstory
Modifier éventuellement le fichier settings.json en ajoutant
	"ev3devBrowser.additionalDevices": [{"name": "ev3dev1","ipAddress": "169.254.54.197"}]
Pour pouvoir utiliser le code sur PC :
Télécharger le github ev3dev dans un autre répertoire et rajouter à la variable d’environnement windows PYTHONPATH (la créer si besoin) le nom du répertoire contenant ev3dev2


une fois les modifications faites sur Visual
- lancer le programme pour vérifier qu'il tourne bien ;-)
- cliquer sur le troisième icone à gauche (Source Control)
- sur la ligne "changes" cliquer sur le + (Stage all changes)
- Entrer un message de commit et faire un commit (tic en haut)
- sur les  ... choisir push et rentrer login et mot de passe GitHub

# liste des pages utiles
https://github.com/BichonCby/BaseBSPython
https://github.com/ev3dev/vscode-ev3dev-browser
https://github.com/ev3dev
https://marketplace.visualstudio.com/items?itemName=ev3dev.ev3dev-browser
https://code.visualstudio.com/docs/?dv=win64
https://github.com/ev3dev/ev3dev-lang-python/tree/ev3dev-stretch/ev3dev2
https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/sensors.html
http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/sensors.html
https://github.com/ev3dev/lego-linux-drivers/blob/89bde527d77ada5efad10a3b3d6a737c67e982ff/sensors/nxt_i2c_sensor_defs.c
https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/sensors.html
https://github.com/ev3dev/ev3dev-lang-python/blob/ev3dev-stretch/ev3dev2/motor.py

# Architecture des fichiers
GR2020.py est le fichier à lancer. il contient l'appel de toutes les classes dans l'ordre.
Les threads de Duree de match et de séquence récurrente sont définis aussi
Robot.py gère les particularités du robot et du match
Sensor.py gère les capteurs
Action.py : gère les actionneurs , hors propulsion
Position.py : gère la position du robot
Asserv.py : gestion de l'asservissement, depuis la position jusqu'au pilotage des moteurs
MoveManager.py : fonctions pour faire bouger le robot
Strategy.py : stratégie de haut niveau, pour l'instant un thread unique

#Classes
Robot : c'est la classe qui va gérer les éléments liés au robot et au match en général
- Couleur (texte)
- Largeur, Longueur, recalage (selon la méca du robot)
- Score (dynamique)
- StepTime (la fréquence d'appel de l'asserv)
- DisplayScore() : affichage à l'écran
- SetColor() : affecte la couleur (appelée par la classe de capteur)

Sensor : Classe qui va gérer les différents capteur et leur analyse
- Tirette, BAU, bouton
- EncoderRight, EncoderLeft (les codeurs pour l'asserv)
- ReadEncoder() : lecture des codeurs
- ReadTCHMUX() : lecture des contacteurs
- ReadSMUX() : Lecture des sonars pour la detection

Action : Classe qui gère les actionneurs et les états des actionneurs
- StateDoor, CntDoor : les états d'un des actionneurs
- ActionState() : fonction récurrente 
- OpenDoor()... : fonction qui va positionner la machine à état. Cette fonction est appelée par l'IA

Position : 
- X, Y, angle : coordonnées du robot (en absolu)
- CalculPosition() : fonction récurrente
- SetPosition() : impose la position, au départ ou après recalage (ou balise?)

Asserv : Classe qui gère l'asservissement du déplacement du robot
- Converge, Blocage : état de l'asservissement
- Distance, Angle : écart entre la cible et le réel
- SpdAvCns, SpdRotCns, SpdxxxCns : consignes des moteurs réels ou virtuels
- TgtX, TgtY, TgtAngle : position cible 
- Type : type de déplacement souhaité
- CalculAsserv() : fonction récurrente 
- GenerateVirtualSpeed() : sous fonction pour déterminer les consignes des moteurs virtuels
- DriveWheels() : sous fonction de pilotage des moteurs
- DetermineBlocage() : fonction qui va remonter un flag de blocage (voir comment on l'appelle)

MoveManager : Classe qui va utiliser es fonction pour faire bouger le robot
- GoFor(), GoBack() : on va à un point en avant ou en arrière
- DontMove() : on reste statique
- Rotate() : rotation vers un angle
- MoveManu() : on bouge les roues manuellement

# Les threads
MatchRobot : un thread lancé quand la tirette est tirée. C'est un thread interruptable à cause de l'arrêt d'urgence et de la funny actionneurs
DureeMatch : thread lancé au départ. Il attend la tireete, puis attend le BAU ou le les 100s
Sequence : thread lancé au départ. Il va appeler les fonctions récurrents dans les 3 phases de vie : avant, pendant et après match
 