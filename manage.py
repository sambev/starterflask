from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from app import make_app, db

app = make_app('dev')
manager = Manager(app)

# DB command to run create and run all migrations for models
manager.add_command('db', MigrateCommand)
# import models here for migrating. The is probably a better spot for this

@manager.command
def run():
    app.run()

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()
