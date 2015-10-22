# Architecture-Platforms
Projet intégration 3A

Context :

Each monitor displays a graphical representation of an urban road system. Each monitor is responsible for the display of a specific region. Which region and its road system description are obtained from a WebService in JSON. The regions are connected through bridges which let vehicles travel from one region to another.

Once all the monitors are setup and ready, we can simulate vehicles travelling the road system. More specifically, the vehicles are cabs which can be commanded to go to a specific location. Using algorithms learned in graph theory or AI courses, you must resolve a path for the cab to go from its current location to the requested location. (This assumes the cab is available; if already on route then the cab must first reach its current destination before acquiring a new one).

Cabs have an odometer (travelled distance, reset to zero upon acquiering a new destination) and a binary availability state (busy/free). A cab can only seek one destination at once. Each cab will have a dedicated device to report its state and the odometer's value. Provided the cab is available, this device will also be used by human operators to let the cab know it should acquire the next available destination (otherwise the cab just remains at its current location after reaching a destination).

Monitors will update continuously the display of the location of the cabs. To do so, instead of polling frequently the WebService, the monitors will be notified via a Pub/Sub implemented with WebSockets.
The simulation has as many cabs as there are counters connected.
Human end users have the following means of interaction with the system:
        request a new destination (through the monitors by click or touch),
        assign a cab the next destination in cue (provided the cab is available and using the Intel Galileo LCD shield buttons).


Folder description : 
    
      Documentation :   All documentations wrote is there.
      Galileo :         Groups all test of operations & final file for Arduino Galileo.
      Monitors :        Groups computers interface.
      TableCab :        This folder is for the Android Application.
      Serveur :         Groups two server : http server and websocket server for the Raspberry PI.
      
Thanks for reading.
