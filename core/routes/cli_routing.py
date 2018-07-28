def defineRoutes(Route): # EXAMPLE FILE

    def dbSetup():
        import sql.setup as Setup
        import sql.upgrade as Upgrade
        Setup.Setup()
        Upgrade.Upgrade()
    Route.path('setup database', dbSetup)

    # chaining, handles both `test` and `test all`
    Route.path('test', 'core.packages.testing.test').call('Test').path('all', 'core.packages.testing.test').call('Test')
    
    requirements = Route.prefix('requirements')
    requirements.path('check', 'core.packages.requirements.check').call('Check')
    requirements.path('install', 'core.packages.requirements.install').call('Install')
