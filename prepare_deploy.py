# create files needed for deployment
with open("requirements.txt","w") as f:
    f.write("Flask==3.0.0\ngunicorn==21.2.0\n")

with open("gunicorn_config.py","w") as f:
    f.write("")

# Fix app.py to work online
with open("app.py","r",encoding="utf-8") as f:
    code = f.read()

if "app.run" not in code:
    code += "\nif __name__ == '__main__':\n    app.run()"

# Ensure app.py has correct host for deploy
if "0.0.0.0" not in code:
    code = code.replace("app.run()", "app.run(host='0.0.0.0', port=10000)")

with open("app.py","w",encoding="utf-8") as f:
    f.write(code)

print("Ready for deploy!")