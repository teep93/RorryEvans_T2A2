from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from init import db, ma

class Gym(db.Model):
    __tablename__ = 'gyms'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(200), nullable=False)

    users: Mapped[list['User']] = relationship('User', back_populates='gym')

class GymSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'location')