/**
 * Created by marshallfate on 2017/4/13.
 */

function data_to_table(data) {
    document.getElementById('table-contain').innerHTML="";
    data = JSON.parse(data)
    var line = data.length
    var table = document.createElement("table");
    for (var index = 0; index < line; index++) {
        var tr = document.createElement("tr");
        var chaanel = document.createElement("td")
        chaanel.innerText = 'chnnel_' + index
        tr.appendChild(chaanel)
        var value = document.createElement("td")
        value.innerText = data[index]
        tr.appendChild(value)
        table.appendChild(tr);
    }
    document.getElementById("table-contain").appendChild(table);
}
