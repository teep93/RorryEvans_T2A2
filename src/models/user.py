from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

class User():
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    public_info: Mapped[str] = mapped_column(Text)
    gym_id: Mapped[int] = mapped_column(Integer, ForeignKey('gyms.gym_id'))
    sensitive_info_id: Mapped[int] = mapped_column(Integer, ForeignKey('sensitive_info.sensitive_info_id'))

