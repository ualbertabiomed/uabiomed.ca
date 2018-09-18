doFetch("auth_test", 'get').then(data=>{console.log(data);}).catch(msg=>{console.log(msg);});
doFetch("authenticate", 'POST', '{"ccid":"reckhard", "passwd":"1497646"}').then(data=>{console.log(data);}).catch(msg=>{console.log(msg);});
doFetch("auth_test", 'get').then(data=>{console.log(data);}).catch(msg=>{console.log(msg);});


function doFetch(sub_url, req_type, bdy){
    return fetch("http://localhost:8888/"+sub_url, {
        method: req_type,
        headers: {
                "Content-Type": "application/json; charset=utf-8",
            },
        body: bdy,
    }).then(response=>{return response.json();});
}

