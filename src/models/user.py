from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from init import db, ma

class User(db.Model):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    public_info: Mapped[str] = mapped_column(Text)
    
    gym_id: Mapped[int] = mapped_column(Integer, ForeignKey('gyms.gym_id'))
    sensitive_info_id: Mapped[int] = mapped_column(Integer, ForeignKey('sensitive_info.sensitive_info_id'))

    gyms: Mapped['Gym'] = relationship('Gym', back_populates='user')
    sensitive_info: Mapped['SensitiveInfo'] = relationship('SensitiveInfo', back_populates='user')
    self_fight_records: Mapped[list['FightRecord']] = relationship('FightRecord', foreign_keys='FightRecord.user_id', back_populates='user')
    opponent_fight_records: Mapped[list['FightRecord']] = relationship('FightRecord', foreign_keys='FightRecord.opponent_id', back_populates='opponent')
    matchmaking_user: Mapped[list['Matchmaking']] = relationship('Matchmaking', foreign_keys='Matchmaking.user_id', back_populates='user')
    matchmaking_opponent: Mapped[list['Matchmaking']] = relationship('Matchmaking', foreign_keys='Matchmaking', back_populates='opponent')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'public_info')