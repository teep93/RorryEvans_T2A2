from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from init import db, ma

class Matchmaking(db.Model):
    __tablename__ = 'matchmaking'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    status: Mapped[str] = mapped_column(String(150), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    opponent_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    admin_id: Mapped[int] = mapped_column(ForeignKey('admins.admin_id'))

    user: Mapped['User'] = relationship('User', foreign_keys=[user_id], back_populates='matchmaking_user')
    opponent: Mapped['User'] = relationship('User', foreign_keys=[opponent_id], back_populates='matchmaking_opponent')
    admin: Mapped['Admin'] = relationship('Admin', back_populates='matchmaking')

class MatchmakingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'status')