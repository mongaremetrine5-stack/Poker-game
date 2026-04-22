from flask import Blueprint, jsonify,Flask


student_bp=Blueprint("student_Bp",__name__)

@student_bp.route("/single", methods=["GET"])
async def sing_student():
    return "single student"
    
@student_bp.route("/add", methods=["POST"])
async def add():
    return "add student"
   
@student_bp.route("/delete", methods=["DELETE"])
async def delete_student():  
    return "delete student"
   
@student_bp.route("/list_all", methods=["Get"])    
async def list_all():
    return "list all students"
    
#if __name__=="__main__":
    
    #app.register_blueprint(student_bp, url_prefix="/student")
    
    #app.run(debug=True)