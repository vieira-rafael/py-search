from flask.ext.script import Managerfrom flask.ext.migrate import Migrate, MigrateCommandfrom run import appfrom app.users.models import db
migrate = Migrate(app, db)
manager = Manager(app)manager.add_command('db', MigrateCommand)
if __name__ == '__main__':    manager.run()