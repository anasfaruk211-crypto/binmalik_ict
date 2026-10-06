import os
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

files = {
"templates/index.html": """<!DOCTYPE html><html><head><link rel='stylesheet' href='/static/style.css'><title>Binmalik</title></head><body><nav><h2>BINMALIK ICT</h2><a href='/'>Home</a> | <a href='/courses'>Courses</a> | <a href='/admission'>Admission</a> | <a href='/contact'>Contact</a> | <a href='/admin'>Admin</a></nav><h1>Welcome to Binmalik ICT Institute</h1><p>Learn Computer, Programming, Graphics and more.</p><a href='/admission'><button>Apply Now</button></a></body></html>""",
"templates/courses.html": """<!DOCTYPE html><html><head><link rel='stylesheet' href='/static/style.css'></head><body><nav><h2>BINMALIK ICT</h2><a href='/'>Home</a> | <a href='/courses'>Courses</a> | <a href='/admission'>Admission</a> | <a href='/contact'>Contact</a> | <a href='/admin'>Admin</a></nav><h1>Our Courses</h1><ul><li>Computer Basics</li><li>Web Development</li><li>Python Programming</li><li>Graphics Design</li></ul></body></html>""",
"templates/admission.html": """<!DOCTYPE html><html><head><link rel='stylesheet' href='/static/style.css'></head><body><nav><h2>BINMALIK ICT</h2><a href='/'>Home</a> | <a href='/courses'>Courses</a> | <a href='/admission'>Admission</a> | <a href='/contact'>Contact</a> | <a href='/admin'>Admin</a></nav><h1>Admission Form</h1><form method='post'><input name='name' placeholder='Full Name' required><br><br><input name='phone' placeholder='Phone' required><br><br><input name='course' placeholder='Course' required><br><br><button type='submit'>Submit</button></form></body></html>""",
"templates/contact.html": """<!DOCTYPE html><html><head><link rel='stylesheet' href='/static/style.css'></head><body><nav><h2>BINMALIK ICT</h2><a href='/'>Home</a> | <a href='/courses'>Courses</a> | <a href='/admission'>Admission</a> | <a href='/contact'>Contact</a> | <a href='/admin'>Admin</a></nav><h1>Contact Us</h1><p>Phone: 080XXXXXXXX</p><p>Location: Abuja, Nigeria</p></body></html>""",
"templates/admin.html": """<!DOCTYPE html><html><head><link rel='stylesheet' href='/static/style.css'></head><body><nav><h2>BINMALIK ICT</h2><a href='/'>Home</a> | <a href='/courses'>Courses</a> | <a href='/admission'>Admission</a> | <a href='/contact'>Contact</a> | <a href='/admin'>Admin</a></nav><h1>Admin - Students List</h1>{% for s in students %}<p>{{s.name}} - {{s.phone}} - {{s.course}}</p>{% else %}<p>No admission yet</p>{% endfor %}</body></html>""",
"static/style.css": """body{font-family:Arial;padding:20px;background:#f4f4f4}nav{background:#0d2a54;color:white;padding:15px}nav a{color:white;margin:5px;text-decoration:none}button{padding:10px;background:#0d2a54;color:white;border:none}input{padding:8px;width:250px}"""
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Fixed! All files recreated.")