$('#likes').click(function () {
    var catid;
    catid=$(this).attr('data-catid');
    //通过get 跳转到urls 找到对应的方法 在views中更新数据库内容 然后返回likes数据 ，把数据更新到 like_count中
    $.get('/rango/like_category/',{category_id:catid},function (data) {
        $('#like_count').html(data);
        $('#likes').hide();
    })
})
//键盘放上面就会触发的事件
$('#suggestion').keyup(function () {
    var query;
    query=$(this).val();
    $.get('/rango/suggest_category/',{suggestion:query},
        function (data) {
            $('#cats').html(data)
        });
})