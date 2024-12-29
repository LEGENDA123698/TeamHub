$(document).ready(function(){
    $('.search').on('input', function(){
      let query = $(this).val();
      let searchUrl = $(this).data('search-url');  // Получаем URL из data-атрибута
      if(query.length > 2){
        $.ajax({
          url: searchUrl,
          data: {
            'q': query
          },
          dataType: 'json',
          // Остальной код без изменений
        });
      } else {
        $('#search-results').empty();
      }
    });

    // Остальной код без изменений
  });