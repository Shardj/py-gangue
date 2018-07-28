import types, sys, core.helpers as Helpers

class Route:
    imports = {} # share between all instances of Route, aka class variable
    calls = {}

    def __init__(self, prefix = ""):
        self.currentPrefix = prefix # only exists in each class instance

    def path(self, route, save):
        toReturn = Route(self.currentPrefix)
        if not callable(save) and not isinstance(save, str):
            Helpers.printError('Invalid variable type passed to route', True)

        toReturn.currentPrefix += route if len(toReturn.currentPrefix) == 0 else ' ' + route
        route = toReturn.currentPrefix
        route = route.split(' ')
        newRoute = toReturn.imports
        for index, part in enumerate(route):
            if index < len(route)-1: # if not last iteration
                if not part in newRoute: # if next part of route not found, create it
                    newRoute[part] = {}
                newRoute = newRoute[part] # move into found or created part
            else:
                if part in newRoute and (callable(newRoute[part]) or isinstance(newRoute[part], str)):
                    Helpers.printError('Duplicate route path given', True)
                newRoute[part] = save
        return toReturn

    def prefix(self, route):
        toReturn = Route(self.currentPrefix)
        toReturn.currentPrefix += route if len(toReturn.currentPrefix) == 0 else ' ' + route
        return toReturn

    def clone(self, path, newPath):
        toReturn = Route(self.currentPrefix)
        path = path if len(toReturn.currentPrefix) == 0 else toReturn.currentPrefix + ' ' + path
        save = toReturn.imports
        route = path.split(' ')
        for part in route:
            try:
                save = save[part]
            except KeyError:
                Helpers.printError('You tried to clone a route which doesn\'t exist', True)

        self.path(newPath, save)
        return toReturn

    def call(self, toCall):
        toReturn = Route(self.currentPrefix)
        if not isinstance(toCall, str):
            Helpers.printError('Invalid variable type passed to route', True)

        route = toReturn.currentPrefix
        route = route.split(' ')
        newRoute = toReturn.calls
        for index, part in enumerate(route):
            if index < len(route)-1: # if not last iteration
                if not part in newRoute: # if next part of route not found, create it
                    newRoute[part] = {}
                newRoute = newRoute[part] # move into found or created part
            else:
                if part in newRoute and isinstance(newRoute[part], str):
                    Helpers.printError('Duplicate route path given', True)
                newRoute[part] = toCall
        return toReturn
