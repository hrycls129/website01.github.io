docstring = """
<!DOCTYPE html>

<html>
    <head>
        <title>Scratch</title>
    </head>

    <body>
        <h3>You scratch at the door.</h3>

        <p>
            %s.
        </p>
        
        <a href="https://hrycls129.github.io/website01.github.io/room47/scratch/scratch%s">Keep scratching.</a>
        <br>
        <a href="https://hrycls129.github.io/website01.github.io/room47/page03">Alright, enough of this.</a>
    </body>

</html>
"""

scratch_string = "Scratch"
for i in range(1,47):
    num_string = str(i)
    next_num_string = str(i+1)

    if len(num_string) < 2:
        num_string = "0" + num_string

    if len(next_num_string) < 2:
        next_num_string = "0" + next_num_string

    with open("room47/scratch/scratch%s.html"%num_string, "w") as f:
        f.write(docstring%(scratch_string, next_num_string))

    scratch_string += " scratch"
