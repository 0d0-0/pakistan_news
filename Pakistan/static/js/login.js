function getStorage(){
    let name=document.getElementById("name").value;
    let str =localStorage.getItem(name);
    let data =JSON.parse(str);
    if(!data){
        //alert("请你先注册");
        document.getElementById('msg').innerHTML="请先+<a href='register.html'>注册!</a>";
    return false;
        }else{
            let pw=document.getElementById('password').value;
            if(data.password==pw){
                document.location.href="index.html";
                return false;
            }else{
                document.getElementById('msg').innerHTML="密码错误";
                return false;
            }
        }
        }