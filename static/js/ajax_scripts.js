$(function () {
  $('.js-send').click( function () {
    var url = $(this).data('url');
    var message = $('.js-user_data').val();
    $.ajax({
      type: 'get',
      url: url,
      dataType: 'json',
      data: {'message': message},
      async: true,
      success: function (data) {
        console.log(data)
        $('.message').text(data.message);
      },
      error: function () {
        console.error('server error');
      }
    })
  });


  $('.js-send2').click( function () {
    var url = $(this).data('url');
    var message = $('.js-user_data').val();
    $.ajax({
      type: 'get',
      url: url,
      dataType: 'html',
      data: {'message': message},
      async: true,
      success: function (data) {
        console.log(data);
        $('.message').html(data);
      },
      error: function () {
        console.error('server error');
      }
    })
  });

});

