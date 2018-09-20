const address = "http://localhost:8888/";
function login(usr, passwd){
    doFetch("authenticate", 'POST', {ccid:usr, passwd:passwd})
        .then(response=>{return response.json();})
        .then(data=>{
            console.log(data);
            localStorage.setItem("tok", data.token);
            localStorage.setItem("usr", JSON.stringify(data));
        })
        .then(()=>{window.location.href=address+"admin/main.html";})
        .catch(msg=>{console.log(msg);});
}


doFetch("auth_test", 'POST')
    .then(rep=>{return rep.text();})
    .then(data=>{console.log(data);})
    .catch(msg=>{console.log(msg);});


function doFetch(sub_url, req_type, bdy){
    if(req_type == "POST" || req_type == "PUT"){
        if(bdy == null){
            bdy = {};
        }
        if(localStorage.tok != undefined){
            bdy.token = localStorage.getItem("tok");
        }else{
            bdy.token = "eyJ0aW1lb3V0IjogMH1+bGFsYWxsbGE=";
        }
    }
    return fetch(address+sub_url, {
        method: req_type,
        headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
        body: JSON.stringify(bdy),
    });
}

