var current_rank = '';
function removeMember(ccid, disabled){
    if(disabled == "disabled"){
        console.log(ccid);
    }
}

function flipConfirm(ccid){
    doFetch("flipMember", 'POST', {"ccid": ccid})
        .then(rep=>{getSubordinates(current_rank);})
        .catch(msg=>{console.log(msg);});

}

function addMember(person, team, confirmed, ccid){
    let isconfirmed = "";
    let disabled = "";
    let accept = "";
    if(confirmed == 1){
        disabled = "disabled";
        accept = "Associte";
    }else{
        isconfirmed  = "not-confirmed";
        accept = "Developer";
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
                 onclick="removeMember(\'${ccid}\', ${disabled})">Delete</button>
           </div>
         </div>`;

    var ul = document.getElementById("member_list");
    var li = document.createElement("li");
    li.innerHTML = html;
    ul.appendChild(li);
}

function loadTeams(ranks){
    document.getElementById("team_list").innerHTML = "";
    for(let x of ranks){
        if(getTeamFromRank(x)){
            addTeam(getTeamFromRank(x), x);
        }
    }
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


var team_map = {};
function getTeamFromRank(rank){
    if(team_map.hasOwnProperty(rank)){
        return team_map[rank];
    }else{
        updateMaps();
    }
    return false;
}

function updateMaps(){
    doFetch("teams", 'GET')
        .then(rep=>{return rep.json();})
        .then(dat=>{return dat.teams;})
        .then(data=>{
            document.getElementById("team_list").innerHTML = "";
            for(let x of data){
                addTeam(x.name, x.id);
                team_map[x.id] = x.name;
            }
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
                if(!teams.includes(x.rank)){
                    teams.push(x.rank);
                }
            }

            loadTeams(teams);
            document.getElementById("team").innerText = getTeamFromRank(team);
        })
        .catch(msg=>{/*console.log(msg);*/});
}


function loadView(){
    current_rank = JSON.parse(localStorage.getItem("usr")).rank;
    updateMaps();
}

loadView();

