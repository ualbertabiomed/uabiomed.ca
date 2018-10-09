var current_rank = JSON.parse(localStorage.getItem("usr")).rank; // I should really do proper error handling here
function removeMember(ccid, disabled){
    if(disabled == ""){ // if it's not disabled
        // yes, I know this is hacky, But so is a lot of this
        // site, and I don't feel like fixing things now.
        doFetch("deleteMember", 'POST', {"ccid": ccid})
            .then(rep=>{getSubordinates(current_rank);})
            .catch(msg=>{console.log(msg);});
    }
}

function flipConfirm(ccid){
    doFetch("flipMember", 'POST', {"ccid": ccid})
        .then(rep=>{getSubordinates(current_rank);})
        .catch(msg=>{console.log(msg);});

}

function addNewUser(){
    if(confirm("You are now creating a new person, they will be added to the " + getTeamFromRank(current_rank) + " team. To proceed, ensure you know the CCID, First Name, and Last Name of the person, also, I apologize for using prompts for this.")){
        // This is temporary, this use of the prompt.
        // At least that's what I tell myself, it helps me sleep
        // better at night knowing that I'm never going to bother
        // getting around to changing this
        let fname = prompt("First Name");
        let lname = prompt("Last Name");
        let ccid = prompt("CCID (the word ID, the first part of your email)");

        let data = {"fname": fname, "lname": lname,
            "rank": current_rank, "ccid": ccid};
        console.log(data);

        doFetch("addMember", 'POST', data)
            .then(rep=>{getSubordinates(current_rank);})
            .catch(msg=>{console.log(msg);});

    }
}

function addMember(person, team, confirmed, ccid){
    let isconfirmed = "";
    let disabled = "";
    let accept = "";
    if(confirmed == 1){
        disabled = "disabled";
        accept = "Developer";
    }else{
        isconfirmed  = "not-confirmed";
        accept = "Associate";
    }
    team = getTeamFromRank(team);
    let html = `
         <div class="${isconfirmed} card hor member drift">
           <div class="hor spread wide">
             <p class="member-person">${person}</p>
             <p class="member-rank">${team}</p>
           </div><div class="hor drift wide">
             <button id="test" class="member-confirm"
                 onclick="flipConfirm(\'${ccid}\')">${accept}</button>
             <button class="member-delete ${disabled}"
                 onclick="removeMember(\'${ccid}\', \'${disabled}\')">Delete</button>
           </div>
         </div>`;

    var ul = document.getElementById("member_list");
    var li = document.createElement("li");
    li.innerHTML = html;
    ul.appendChild(li);
}


function addTeam(team, rank){
    let html = `
        <div class="team-wrapper">
            <button class="team-goto" onclick="clickTeam('${rank}')">${team}</button>
        </div>`;

    var ul = document.getElementById("team_list");
    var li = document.createElement("li");
    li.innerHTML = html;
    ul.appendChild(li);
}

function clickTeam(teamid){
    current_rank = teamid;
    getSubordinates(teamid);
}


var team_map = JSON.parse(localStorage.getItem('team') || "{}");
function getTeamFromRank(rank){
    if(rank == ""){
        return false;
    } else if(team_map.hasOwnProperty(rank)){
        return team_map[rank];
    }else{
        updateMaps();
    }
    return false;
}

function loadTeams(){
    document.getElementById("team_list").innerHTML = "";
    for(let x in team_map){
        if(x.startsWith(current_rank)){
            addTeam(getTeamFromRank(x), x);
        }
    }
}

function updateMaps(){
    doFetch("teams", 'GET')
        .then(rep=>{return rep.json();})
        .then(dat=>{return dat.teams;})
        .then(data=>{
            document.getElementById("team_list").innerHTML = "";
            for(let x of data){
                //addTeam(x.name, x.id);
                team_map[x.id] = x.name;
            }
            localStorage.setItem("teams", JSON.stringify(team_map));
            getSubordinates(current_rank);
        })
        .catch(msg=>{console.log(msg);});
}

function getSubordinates(rank){
    document.getElementById("member_list").innerHTML = "";
    let data = JSON.parse(localStorage.getItem("usr"));
    data.rank = rank;
    let teams = [];
    let team = data.rank;
    doFetch("getallsubordinates", 'POST', data)
        .then(rep=>{return rep.json();})
        .then(data=>{
            for(let x of data.members){
                addMember(x.fname+" "+x.lname, x.rank, x.status, x.ccid);
            }

            loadTeams();
            document.getElementById("team").innerText = getTeamFromRank(team);
        })
        .catch(msg=>{/*console.log(msg);*/});
}


function loadView(){
    current_rank = JSON.parse(localStorage.getItem("usr")).rank;
    updateMaps();
    //getSubordinates(current_rank);
}

loadView();

