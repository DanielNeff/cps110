
import bottle
import random

SOUNDS = ["236982__devengarber__jacob-allen-evil-laugh",
    "347547__masgame__applause",
    "371339__johanneskristjansson__cheer-crowd",
    "stupick3-men-cheering"]
    
@bottle.route('/')
def picker():
    stuName, stuUsername = students[random.randrange(len(students))]
    effect = SOUNDS[random.randrange(len(SOUNDS))]

    return HTML.format(stuName, stuUsername, effect)

@bottle.route('/<filename:path>')
def send_static(filename):
    """Serve up images and sounds."""
    return bottle.static_file(filename, root='.')

HTML = """
<html>
<body>
<h1>{0}</h1>
<img src="/pics/{1}.bmp" width="200">
<audio autoplay>
  <source src="/sounds/{2}.mp3" type="audio/mpeg" >
</audio>
</body>
</html>
"""

students = []
def readStudentFile():
    stufile = open('students.txt')
    line = stufile.readline()
    while len(line) != 0:
        # 110,01,James,An,han962
        line = line.strip()
        [courseno, coursesect, firstname, lastname, username] = line.split(',')
        students.append((firstname + " " + lastname, username))
        line = stufile.readline()
    stufile.close()

    print("Loaded data: ", students)

if __name__ == '__main__':
    readStudentFile()

    # Launch the BottlePy dev server
    bottle.run(host='localhost', debug=True)
