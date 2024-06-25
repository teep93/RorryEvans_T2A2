from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from init import db, ma

class Admin(db.Model):
    __tablename__ = 'admins'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    fight_records: Mapped[list['FightRecord']] = relationship('FightRecord', back_populates='admin')
    matchmaking: Mapped[list['Matchmaking']] = relationship('Matchmaking', back_populates='admin')

class AdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
    


