class Route:

    def __init__(self, lookupString):
        self.routes = {}
        self.lookupString = lookupString
        self.currentPrefix = ""

    def defineRoutes(self, routes: types.FunctionType):
        routes()
        foundFunc = self.lookupRoutes()
        foundFunc()

    def path(self, route: str, instructions: types.FunctionType):
        route = self.currentPrefix + ' ' + route
        route = route.split(' ')
        newRoute = self.routes
        for index, part in enumerate(route):
            if index < len(route)-1: # if not last iteration
                if not part in newRoute: # if next part of route not found, create it
                    newRoute[part] = {}
                newRoute = newRoute[part] # move into found or created part
            else:
                newRoute[part] = instructions

    def prefix(self, route: str, callback: types.FunctionType):
        # add to currentPrefix, run callback, remove what was added to current
        self.currentPrefix += route if len(self.currentPrefix) == 0 else ' ' + route
        callback()
        self.currentPrefix = self.currentPrefix[:-len(route)] //cut off however many characters we added


    def lookupRoutes(self):
        lookupString = self.lookupString.split(' ')
        lookupResult = self.routes
        try:
            for index, part in enumerate(lookupString):
                if index < len(lookupString)-1: # if not last iteration
                    lookupResult = lookupResult[part]
                else:
                    toReturn = lookupResult[part]
                    if callable(toReturn):
                        return toReturn # return the looked up function
                    else:
                        return False # found something other than function here
        except TypeError, KeyError:
            return False # couldn't find
