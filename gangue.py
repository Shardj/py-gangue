# Entry point

import pyfiglet
from app.configs.local import projectName

print(pyfiglet.figlet_format(projectName, font = "slant"))

import core.packages.router.route_manager as route_manager
route_manager.RouteManger()
