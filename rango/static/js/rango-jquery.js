//
// $(document).ready(function () {
// $("#about-btn").click(function (event) {
//     alert('you click the button by jquery');
// });
// });
$(document).ready(function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });
    // $("#changepage").click( function(event) {
    //     alert("You clicked the button using JQuery!");
    // });




   //覆盖在 p上文字变红
   $("p").hover(function () {
        $(this).css('color','red');
    },
      function () {
          $(this).css('color','blue')
      }
      );

   $(".ouch").click(function (event) {
       alert("you click me ouch")
   })
   $("#about-btn").click(function (event) {
       //响应id 赋值操作
       msgstr=$("#msg").html()
       msgstr=msgstr+"o"
       $("#msg").html(msgstr)
   });
   //从响应的页面把参数取出来  传递到urls中的方法 这样就完成了不用刷新的功能 通过ajax和 url交互
   $('.rango-add').click(function () {
       var catid=$(this).attr('data-catid');
       var url=$(this).attr('data-url');
       var title=$(this).attr('data-title');
       var me=$(this)
       //向这个页面传递参数
       $.get('/rango/auto_add_page/',{category_id:catid,url:url,title:title},
           function (data) {
               $('#pages').html(data);
               me.hide();
           });

   });

}


);
