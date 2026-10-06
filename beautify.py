import os

css = """
*{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',Arial}
body{background:#f5f7fb;color:#222}
nav{background:#0a1931;color:white;padding:15px 40px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0}
nav h2{letter-spacing:1px}
nav a{color:white;text-decoration:none;margin:0 12px;font-weight:500}
nav a:hover{color:#4da3ff}
.hero{background:linear-gradient(135deg,#0a1931 0%,#1a4d8f 100%);color:white;padding:80px 40px;text-align:center}
.hero h1{font-size:42px;margin-bottom:15px}
.hero p{font-size:18px;opacity:0.9;margin-bottom:25px}
.btn{background:#ffc107;color:#0a1931;padding:12px 28px;border:none;border-radius:6px;font-weight:bold;text-decoration:none;cursor:pointer;display:inline-block}
.btn:hover{background:#ffca2c}
.container{padding:40px;max-width:1100px;margin:auto}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;margin-top:20px}
.card{background:white;padding:25px;border-radius:12px;box-shadow:0 4px 15px rgba(0,0,0,0.08);transition:0.3s}
.card:hover{transform:translateY(-5px)}
.card h3{color:#0a1931;margin-bottom:10px}
form{background:white;padding:30px;border-radius:12px;box-shadow:0 4px 15px rgba(0,0,0,0.08);max-width:500px}
input,select{width:100%;padding:12px;margin:8px 0 15px 0;border:1px solid #ddd;border-radius:6px}
footer{background:#0a1931;color:white;text-align:center;padding:20px;margin-top:40px}
.badge{background:#e8f0fe;color:#0a1931;padding:4px 10px;border-radius:20px;font-size:12px}
"""

index = """
<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width,initial-scale=1'><link rel='stylesheet' href='/static/style.css'><title>Binmalik ICT</title></head><body>
<nav><h2>BINMALIK ICT</h2><div><a href='/'>Home</a><a href='/courses'>Courses</a><a href='/admission'>Admission</a><a href='/contact'>Contact</a><a href='/admin'>Admin</a></div></nav>
<div class='hero'><h1>Empower Your Future with ICT Skills</h1><p>Professional training in Computer, Programming, Graphics, Biotechnology & More - Abuja, Nigeria</p><a class='btn' href='/admission'>Apply Now</a></div>
<div class='container'><h2>Why Choose Us?</h2><div class='cards'>
<div class='card'><h3>💻 Certified Trainers</h3><p>Learn from industry experts with years of experience.</p></div>
<div class='card'><h3>📜 Certificate</h3><p>Get recognized certificate after completion.</p></div>
<div class='card'><h3>💼 Job Support</h3><p>We guide you to internship and job opportunities.</p></div>
</div></div><footer>© 2026 Binmalik ICT Institute, Abuja | 0810 643 0205</footer></body></html>
"""

courses = """
<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width,initial-scale=1'><link rel='stylesheet' href='/static/style.css'></head><body>
<nav><h2>BINMALIK ICT</h2><div><a href='/'>Home</a><a href='/courses'>Courses</a><a href='/admission'>Admission</a><a href='/contact'>Contact</a><a href='/admin'>Admin</a></div></nav>
<div class='container'><h1>Our Professional Courses</h1><div class='cards'>
<div class='card'><h3>Computer Basics</h3><p>MS Word, Excel, PowerPoint <br><br><span class='badge'>3 Months</span></p></div>
<div class='card'><h3>Web Development</h3><p>HTML, CSS, Python, Flask <br><br><span class='badge'>6 Months</span></p></div>
<div class='card'><h3>Python Programming</h3><p>From beginner to advanced <br><br><span class='badge'>4 Months</span></p></div>
<div class='card'><h3>Biotechnology Data</h3><p>Lab tech + ICT integration <br><br><span class='badge'>New!</span></p></div>
<div class='card'><h3>Graphics Design</h3><p>Photoshop, CorelDraw, Canva <br><br><span class='badge'>3 Months</span></p></div>
</div></div><footer>© 2026 Binmalik ICT Institute</footer></body></html>
"""

admission = """
<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width,initial-scale=1'><link rel='stylesheet' href='/static/style.css'></head><body>
<nav><h2>BINMALIK ICT</h2><div><a href='/'>Home</a><a href='/courses'>Courses</a><a href='/admission'>Admission</a><a href='/contact'>Contact</a><a href='/admin'>Admin</a></div></nav>
<div class='container'><h1>Admission Form</h1><p>Fill form to join Binmalik ICT</p><br>
<form method='post'><label>Full Name</label><input name='name' placeholder='e.g. Anas Faruk' required>
<label>Phone Number</label><input name='phone' placeholder='0810 643 0205' required>
<label>Choose Course</label><select name='course' required><option value=''>-- Select --</option><option>Computer Basics</option><option>Web Development</option><option>Python Programming</option><option>Biotechnology</option><option>Graphics Design</option></select>
<button class='btn' type='submit' style='width:100%'>Submit Application</button></form></div></body></html>
"""

contact = """
<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width,initial-scale=1'><link rel='stylesheet' href='/static/style.css'></head><body>
<nav><h2>BINMALIK ICT</h2><div><a href='/'>Home</a><a href='/courses'>Courses</a><a href='/admission'>Admission</a><a href='/contact'>Contact</a><a href='/admin'>Admin</a></div></nav>
<div class='container'><h1>Contact Us</h1><div class='cards'>
<div class='card'><h3>📍 Location</h3><p>Abuja, Federal Capital Territory, Nigeria</p></div>
<div class='card'><h3>📞 Phone</h3><p>0810 643 0205<br>Call / WhatsApp</p></div>
<div class='card'><h3>✉️ Email</h3><p>binmalikict@gmail.com</p></div>
</div></div><footer>© 2026 Binmalik ICT Institute</footer></body></html>
"""

admin = """
<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width,initial-scale=1'><link rel='stylesheet' href='/static/style.css'></head><body>
<nav><h2>BINMALIK ICT - ADMIN</h2><div><a href='/'>Home</a><a href='/admin'>Refresh</a></div></nav>
<div class='container'><h1>Students List ({{students|length}})</h1><br>
<div class='cards'>
{% for s in students %}
<div class='card'><h3>{{s.name}}</h3><p>📞 {{s.phone}}<br>📚 {{s.course}}</p></div>
{% else %}
<div class='card'><p>No admission yet</p></div>
{% endfor %}
</div></div></body></html>
"""

with open("static/style.css","w",encoding="utf-8") as f: f.write(css)
with open("templates/index.html","w",encoding="utf-8") as f: f.write(index)
with open("templates/courses.html","w",encoding="utf-8") as f: f.write(courses)
with open("templates/admission.html","w",encoding="utf-8") as f: f.write(admission)
with open("templates/contact.html","w",encoding="utf-8") as f: f.write(contact)
with open("templates/admin.html","w",encoding="utf-8") as f: f.write(admin)
print("BEAUTIFUL DESIGN APPLIED!")