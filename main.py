
from pyscript import document

# Members in each grade
grade_7 = {'Alex Rivera', 'Jamie Cruz'}
grade_8 = {'Sam Lee', 'Taylor Smith'}
grade_9 = {'Chris Tan', 'Jordan Reyes'}
grade_10 = {'Morgan Lim', 'Casey Santos'}

# Function to add a member
def add_member(event):
    fname = document.querySelector("#fname").value
    lname = document.querySelector("#lname").value

    new_member = fname + " " + lname

    all_members = grade_7.union(grade_8, grade_9, grade_10, {new_member})

    document.querySelector("#output").innerHTML = f"""
        <p><b>{new_member}</b> has been added! 💗</p>
        <p>Updated club members:</p>
        <p>{', '.join(sorted(all_members))}</p>
    """
