from flask import Blueprint, request, render_template, redirect

main = Blueprint("main",__name__)

@main.route('/student', methods=['POST', 'GET'])
def index():
    from models import Student
    from app import db
    if request.method == 'POST':
        new_student = Student()
        new_student.name = request.form['name']
        new_student.class_name = request.form['class_name']
        new_student.date_of_birth = request.form['dob']
        
        try:
            db.session.add(new_student)
            db.session.commit()
            return redirect('/student')
        except Exception as e:
            return "There was an issue while adding a student"+str(e)
            
    else:
        students = Student.query.all()
        return render_template('index.html', students=students)

@main.route('/addStudent')
def student():
    return render_template('addStudent.html')

@main.route('/updateStudent/<int:id>', methods=["POST", "GET"])
def update_student(id):
    from models import Student
    from app import db
    student_to_update = Student.query.get_or_404(id)
    
    if request.method == "POST":
        try:
            student_to_update.name = request.form['name']
            student_to_update.class_name = request.form['class_name']
            student_to_update.date_of_birth = request.form['dob']
            
            db.session.commit()
            return redirect('/student')
        except Exception as e:
            return "Exeption while updating student "+str(e)
        
    else:
        return render_template('updateStudent.html', student=student_to_update)

@main.route('/deleteStudent/<int:id>')
def delete_student(id):
    from models import Student
    from app import db
    student_to_delete = Student.query.get_or_404(id)
    try:
        db.session.delete(student_to_delete)
        db.session.commit()
        return redirect('/student')
    except Exception as e:
        return "Exception while deleting student " +str(e)
        
    
