// function bindEmailCaptchaClick() {
//   $("#captcha-btn").click(function (event) {
//       // this: 代表当前按钮的 jQuery 对象
//       var $this = $(this);
//       // 阻止默认的事件
//       event.preventDefault();

//       var email = $("input[name='email']").val();
//       $.ajax({
//           url: "/auth/captcha/email?eee=" + email,
//           method: "GET",
//           success: function (result) {
//               var code = result['code'];
//               if (code == 200) {
//                   var countdown = 60;
//                   // 开始倒计时之前，取消按钮的点击事件
//                   $this.off("click");
//                   var timer = setInterval(function () {
//                       $this.text(countdown);
//                       countdown -= 1;
//                       // 倒计时结束时执行
//                       if (countdown <= 0) {
//                           // 清除定时器
//                           clearInterval(timer);
//                           // 按钮文本恢复原样
//                           $this.text("获取验证码");
//                           // 重新绑定点击事件
//                           bindEmailCaptchaClick();
//                       }
//                   }, 1000);
//                    $("#success-message").text("邮箱验证码发送成功!").show();
//                     setTimeout(function () {
//                         $("#success-message").hide(); // 3秒后隐藏消息
//                     }, 3000);
//               } else {
//                   alert(result['message']);
//               }
//           },
//           error: function (error) {
//               console.log(error);
//           }
//       });
//   });
// }

// // 整个网页加载完成后再执行
// $(function () {
//   bindEmailCaptchaClick();
// });

// 发送不成
function bindEmailCaptchaClick(){


$(function(){
    $('#captcha-btn').click(function(event){

        var $this = $(this);
        event.preventDefault();
        // var eamil = $("input[name='eamil']").val();
        var eamil = $('#exampleInputEmail1').val();

        // alert(eamil)

        // alert(eamil);
        $.ajax({
            url:"/auth/captcha/email?eee="+ eamil,
            method: "GET",
            success: function (result){
                console.log(result);
                var code = result['code']
                if(code == 200){

                    var countdown = 10;
                    $this.off("click");
                    var timer = setInterval(function(){
                        $this.text(countdown);
                        countdown -= 1;
                        if(countdown <= 0){
                            clearInterval(timer)
                            $this.text('获取验证码');
                            bindEmailCaptchaClick();
                        }
                    }, 1000);

                    // alert("邮箱验证码发送成功"); 
                }else{

                    // alert(result['message']);

                }
            },
            fail:function (error){
                console.log(error);
                alert('发生错误！！！')
            }



        })
        // alert('nitamade ');
    });
});

}
$(function(){

    bindEmailCaptchaClick();
});




// 成了！呃呃呃
// $(function(){
//     $('#captcha-btn').click(function(event){

//         var $this = $(this);
//         event.preventDefault();
//         // var eamil = $("input[name='eamil']").val();
//         var eamil = $('#exampleInputEmail1').val();

//         // alert(eamil)

//         // alert(eamil);
//         $.ajax({
//             url:"/auth/captcha/email?eee="+ eamil,
//             method: "GET",
//             success: function(result){
//                 alert('发送成功！');
//             },
//             // success: function (result){
//             //     console.log(result);
//             //     var code = result['code']
//             //     if(code == 200){

//             //         var countdown = 10;
//             //         $this.off("click");
//             //         var timer = setInterval(function(){
//             //             $this.text(countdown);
//             //             countdown -= 1;
//             //             if(countdown <= 0){
//             //                 clearInterval(timer)
//             //                 $this.text('获取验证码');
//             //                 bindEmailCaptchaClick();
//             //             }
//             //         }, 1000);

//             //         // alert("邮箱验证码发送成功"); 
//             //     }else{

//             //         // alert(result['message']);

//             //     }
//             // },
//             fail:function (error){
//                 console.log(error);
//                 alert('发生错误！！！')
//             }



//         })
//         // alert('nitamade ');
//     });
// });


// 真的无语 ？？？ 哪里来的问题，重写一遍就更新一下就没问题了...