/*
Main JS File
 */

//@requires typeof(synthesized_data) == Object;
function create_table(synthesized_data)
{
    var table = document.getElementById("data_table");

    for (var key in synthesized_data)
    {
        //Value is each event as an JS Struct Obj
        var value = synthesized_data[key];

        //Get attributes
        var title = value['title'];
        var location = value['location'];
        var time = value['time'];

        //Insert Rows and make their cells
        var row = table.insertRow(1);
        var tit_cell = row.insertCell(0);
        var loc_cell = row.insertCell(1);
        var tim_cell = row.insertCell(2);

        //Apply values into the tag in HTML
        tit_cell.innerHTML = title;
        loc_cell.innerHTML = location;
        tim_cell.innerHTML = time;

        //Test Code
        console.log(time);
    }
    return 0;
}

//Change the id of a tag in html
function changeID(id, classname){
    document.getElementById(id).className = classname;
}

//Run and refresh the table in the html
function main(){
    //Raw Data First Retrieved: dtype == string
    //var raw_data_string = fetch(); // dtype == String;
    //var synthesized_data = JSON.parse(raw_data_string); // dtype == Object;
    var test_data = make_test_data();
    create_table(test_data);
    return 0;

}

//Test Field
function make_test_data(){
    var a = {
        'title': "Tartan eat shit",
        'location': "CAUC McConomy",
        'time': "tomorrow at 6"
    }
    var b = {
        'title': "Tartan eat suckers",
        'location': "CAUC sucks",
        'time': "tomorrow at 666"
    }
    var c = {
        'title': "Lucas is shit",
        'location': "Jesus Fuck",
        'time': "never"
    }
    var d = {
        'a': a,
        'b': b,
        'c': c
    }
    return d;

}

//Debug Mode: refresh the table
function delete_row(){
    var table = document.getElementById("data_table");
    table.deleteRow(1);
}

//Useless Comments
function comment(){
    var a = {
        name: 'a',
        age: 14
    };
    var b = {
        name: 'b',
        age: 15
    };
    var c = {
        name: 'c',
        age: 16
    }
    var d = {
        i: a,
        j: b,
        k: c
    }
    let str = JSON.stringify(d, null, ' ');
    console.log(d);
    console.log((str));
    return 0;
}



































