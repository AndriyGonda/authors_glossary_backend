from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from pathlib import Path
from dotenv import load_dotenv
from app import create_app
from app.models import db

ENV_FILE_PATH = Path('.') / '.env'

load_dotenv(dotenv_path=ENV_FILE_PATH)
app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
