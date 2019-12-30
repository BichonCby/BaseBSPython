# BaseBSPython
logiciel de base du soft pyhton pour ev3dev. Sera à instancier pour chaque robot
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
 