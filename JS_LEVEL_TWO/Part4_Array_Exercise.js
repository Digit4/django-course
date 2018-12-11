// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT
function addNew(name) {
     roster.push(name);
}
// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function removeStud(name) {
     var index = roster.indexOf(name);
     if (index > -1) {
          roster.splice(index,1);
     }
}
// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
     console.log(roster);
     alert(roster);
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

var ch = confirm("Do you wish to use the smart app?");
while (ch) {
     var selection = prompt("Press\n1.Add student\n2.Remove student\n3.Display list\n4.Quit\nSelect your Poison:");
     switch (selection) {
          case "1":
               var nm = prompt("Enter Student Name:");
               addNew(nm);
               break;
     
          case "2":
               var nm = prompt("Enter Student Name to be Deleted:");
               removeStud(nm );
               break;
          case "3":
               display();
               break;
          default:
               ch = false;
               break;
     }
}