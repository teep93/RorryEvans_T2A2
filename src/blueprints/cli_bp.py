from flask import Blueprint
from models.user import User
from models.admin import Admin
from models.fight_record import FightRecord
from models.gym import Gym
from models.matchmaking import Matchmaking
from models.sensitive_info import SensitiveInfo
from init import db

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def create_database():
    db.drop_all()
    print("Tables dropped.")
    db.create_all()
    print
