$(document).ready(function() {
    $('#countButton').click(function() {
        var text = $('#text').val();
        $.ajax({
            url: '/count_words',
            method: 'POST',
            data: { text: text },
            success: function(response) {
                var wordCount = '';
                for (var word in response) {
                    wordCount += word + ': ' + response[word] + '<br>';
                }
                $('#wordCount').html(wordCount);
            }
        });
    });
});
