from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from init import db, ma

class FightRecord(db.Model):
    __tablename__ = 'fight_records'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    date: Mapped[Date] = mapped_column(Date, nullable=False)
    result: Mapped[str] = mapped_column(String(50), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    opponent_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    admin_id: Mapped[int] = mapped_column(ForeignKey('admins.admin_id'))

    user: Mapped['User'] = relationship('User', foreign_keys=[user_id], back_populates='fight_records')
    opponent: Mapped['User'] = relationship('User', foreign_keys=[opponent_id], back_populates='fight_opponent_records')
    admin: Mapped['Admin'] = relationship('Admin', back_populates='fight_records')

class FightRecordSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'result')