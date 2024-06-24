from sqlalchemy import Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class SensitiveInfo():
    __tablename__ = 'sensitive_info'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    blood_work_completed: Mapped[bool] = mapped_column(Boolean, nullable=False)
    blood_work_date: Mapped[Date] = mapped_column(Date)
    other_sensitive_data: Mapped[Text] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))