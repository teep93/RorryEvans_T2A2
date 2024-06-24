from sqlalchemy import Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import Mapped, mapped_column

class FightRecord():
    __tablename__ = 'fight_records'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    date: Mapped[Date] = mapped_column(Date, nullable=False)
    result: Mapped[str] = mapped_column(String(50), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    opponent_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    admin_id = Mapped[int] = mapped_column(ForeignKey('admins.admin_id'))