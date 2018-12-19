
$(function(){
        $("#btn").click(function(){
            var text=$('#tocheck').val();
            var reg=/QQ号(\d*).密码(.*?)。/
            var res = reg.exec(text)
            $("#username").val(res[1]);
            $("#password").val(res[2]);
        })
        $("#username").blur(function(){
            var username=$('#username').val();
            $("#copy").val(username);
        })
})