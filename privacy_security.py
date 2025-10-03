import hashlib

def anonymize_student_id(student_id):
    return hashlib.sha256(student_id.encode()).hexdigest()

def access_control(role):
    if role not in ["instructor", "admin"]:
        raise PermissionError("Access denied: Only instructor/admin allowed.")
    print(f"Access granted for role: {role}")

def opt_in_out(student_id, opt_in=True):
    print(f"Student {student_id} {'opted in' if opt_in else 'opted out'} for profiling.")

if __name__ == "__main__":
    print(anonymize_student_id("user_1"))
    try:
        access_control("student")
    except Exception as e:
        print(e)
    access_control("instructor")
    opt_in_out("user_1", opt_in=True)
    opt_in_out("user_2", opt_in=False)