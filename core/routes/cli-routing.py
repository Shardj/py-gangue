# ---------- how it would be with current py routing, pretty bad although it can be cleaned up ---------
def get-routes(lookup = False):
    if !lookup:
        return False
    Route = # use bootstrap builtins import function to import route from core/packages/router
    routeClass = new Route(lookup)

    def ourRoutes():
        def databaseSetup():
            import setup from sql as setupimport
            setupimport.Setup()
            import upgrade from sql as upgradeimport
            upgradeimport.Upgrade()
        routeClass.path("setup database", databaseSetup)

        def testingRoutes():
            def all():
                import test from core/packages/testing as testimport
                testimport.Test(True)
            routeClass.path("all", all)

            def specific():
                import test from core/packages/testing as testimport
                testimport.Test(False)
            routeClass.path("", specific)
        routeClass.prefix("test", testingRoutes)

    # will return found route or False if not found
    return routeClass.defineRoutes(ourRoutes)

# ------------------- ideal way for it to look ----------------------
Route.path('cli command example', 'packagename@fileorfilename')#maybe later have .name('shorthand') on the end later for quick imports

# prefix lets us group our commands
test = Route.prefix('test')
test.path('all', 'testpackage@runalltestsmodule') # the same as Route.path('test all', 'testpackage@runalltestsmodule')
test.path('specific', 'testpackage@runspecifictestmodule') # the same as Route.path('test specific', 'testpackage@runalltestsmodule')

test.clone('specific', '') # the package@module for 'test specific' will now also be used by 'test'
# also the same as
Route.clone('test specific', 'test')
