def defineRoutes(Route): # EXAMPLE FILE
    return # don't want to block core functionality on new installs, remove return when writing real routing

    # all commands are chainable, path for example will act like prefix when chained while also following original functionality
    Route.path('cli command example', 'packagename.fileorfilename')#maybe later have .name('shorthand') on the end later for quick imports

    # prefix lets us group our commands
    test = Route.prefix('test')
    test.path('all', 'testpackage.runalltestsmodule') # the same as Route.path('test all', 'testpackage.runalltestsmodule')
    test.path('specific', 'testpackage.runspecifictestmodule') # the same as Route.path('test specific', 'testpackage.runspecifictestmodule')

    test.clone('specific', '') # the package@module for 'test specific' will now also be used by 'test'
    # also the same as
    # Route.clone('test specific', 'test')

    # instead of specifying a module you can also pass a function into path, lambda or regular
    def hi():
        print('hello')
    Route.path('say hello', hi)
    Route.path('say bye', lambda: print('bye'))

    # for an import path (non function path) you can also specify a call, this one will call meow() on the animals.cat import
    Route.path('cat meow', 'animals.cat').call('meow')
    # we can also pass in optional parmeters with flags such as `--frequency=5`
