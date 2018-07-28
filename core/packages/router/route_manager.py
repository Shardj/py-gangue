import sys, os, pickle, core.packages.router.route as RouteImport, core.helpers as Helpers

class RouteManger:
    cliRouteImportStrings = [{'path': 'core.routes.cli_routing' , 'initFunction' : 'defineRoutes'}, {'path': 'app.routes.cli_routing' , 'initFunction' : 'defineRoutes'}]
    def __init__(self):
        self.routeInstance = RouteImport.Route()
        args = sys.argv[1:]
        if len(args) == 0:
            Helpers.printError('Missing arguments')
            sys.exit()

        self.executeRoutingFiles()
        # our self.routeInstance should now have a very large `imports` and `calls` attribute which we need to lookup with our arguments
        print(pickle.dumps(self.routeInstance.imports))
        sys.exit()

    def executeRoutingFiles(self):
        Route = self.routeInstance
        for importString in self.cliRouteImportStrings:
            try:
                importedRouting = __import__(importString['path'], globals(), locals(), [importString['initFunction']])
                getattr(importedRouting, importString['initFunction'])(Route)
            except ImportError as e:
                print('Route not found at ' + importString)
                raise e
