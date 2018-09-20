function addMember(person, team){
    let html = `
         <div class="hor pad">
             <h3>${person}</h3>
             <p>${team}</p>
             <button>Confirm</button>
             <button>Delete</button>
         </div>`;

    var ul = document.getElementById("member_list");
    var li = document.createElement("li");
    li.innerHTML = html;
    ul.appendChild(li);
}


doFetch("getallsubordinates", 'POST',
    JSON.parse(localStorage.getItem("usr")))
    .then(rep=>{return rep.json();})
    .then(data=>{
        for(let x of data.members){
            addMember(x.fname+" "+x.lname, x.rank);
        }
    })
    .catch(msg=>{console.log(msg);});

