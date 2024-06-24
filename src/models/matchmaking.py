from sqlalchemy import Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class Matchmaking():
    __tablename__ = 'matchmaking'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    status: Mapped[str] = mapped_column(String(150), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    opponent_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    admin_id: Mapped[int] = mapped_column(ForeignKey('admins.admin_id'))