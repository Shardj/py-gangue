import sys

class bot:
    # command: function
    commandFunctionMap = {
        'setup' : {
            'database' : 'setupDatabase'
        },
        'test' : {
            'all' : 'allTests'
        },
        'requirements' : {
            'check' : 'checkRequirements',
            'install': 'installRequirements'
        }
    }

    def __init__(self): # init, aka, interpret command
        args = sys.argv[1:]
        try:
            command = args.pop(0) # take first argument from args
            self.interpretCommandOptions(command, args) # call first argument as local function, pass in remaining args
        except IndexError:
            print('No command given')

    def interpretCommandOptions(self, command, options):
        try:
            firstOption = options.pop(0)
            self.runCommand(command, firstOption, options)
        except IndexError: # pop failed so no specific option set, so we run all options
            try:
                for firstOption in self.commandFunctionMap[command]:
                    self.runCommand(command, firstOption, [])
            except KeyError:
                print('`' + command + '` isn\'t in the function map')

    def runCommand(self, command, option, parameters):
        try:
            funcName = self.commandFunctionMap[command][option]
        except KeyError:
            print('Command `' + command + ' ' + option + '` isn\'t in the function map')
            sys.exit()
        try:
            func = getattr(self, funcName)
        except AttributeError:
            print('Command `' + command + ' ' + option + '` maps to function `' + self.commandFunctionMap[command][option] + '` which cannot be found')
            sys.exit()
        func(parameters)

    def setupDatabase(self, options):
        import sql.setup
        import sql.upgrade

    def allTests(self, options):
        import unittest
        print('checking __name__ == "__main__"')
        if __name__ == "__main__":
            all_tests = unittest.TestLoader().discover('tests')
            print('Attempting to run tests')
            unittest.TextTestRunner().run(all_tests)
            print('Tests completed')

    def checkRequirements(self, options):
        import pkg_resources
        dependencies = []
        with open('requirements.txt', 'r') as fp:
            read_lines = fp.readlines()
            dependencies = [line.rstrip('\n') for line in read_lines]

        failedDependencies = []
        for dependency in dependencies:
            try:
                pkg_resources.require(dependency)
            except pkg_resources.DistributionNotFound as e:
                print(e)
                failedDependencies.append(dependency)
        return failedDependencies

    def installRequirements(self, options):
        import os
        failedDependencies = self.checkRequirements([])
        for package in failedDependencies:
            run = 'sudo python3 -m pip install "' + package + '"'
            print('running: `' + run + '`')
            os.system(run)


bot()
