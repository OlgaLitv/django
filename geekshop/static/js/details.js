window.onload = function (){
    $('.details_of_product').on('click','a[href="details2"]', function (){
        let t_href = event.target
        console.log(t_href.name)
        console.log(t_href.value)
        $.ajax(
        {
            url: '/products/details/' + t_href.name,
            success: function(data){
                $('.details_of_product').html(data.result)
            }
        });
        event.preventDefault()

    })
}
