from app import db
from sqlalchemy.dialects.postgresql import JSON

class Student(db.Model):
    __tablename__ = 'student_data'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    class_name = db.Column(db.String(200), nullable=False)
    date_of_birth = db.Column(db.Date)

    def __repr__(self) -> str:
        return "<studentID %s>" % self.id
    
class Student(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return "<studentID %s>" % self.id