from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from chorectl.app import create_app
from chorectl.models.db import db


app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
