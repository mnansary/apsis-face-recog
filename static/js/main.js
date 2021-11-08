$(document).ready(function () {
    // Init
    $('#btn-predict').hide();
    $('.loader').hide();
    $('#result').hide();
    // Upload Preview
    function readimg1(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview1').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview1').hide();
                $('#imagePreview1').fadeIn(650);
                
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    function readimg2(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview2').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview2').hide();
                $('#imagePreview2').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imageUpload1").change(function () {
        $('#result').text('');
        $('#result').hide();
        readimg1(this);
    });
    $("#imageUpload2").change(function () {
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readimg2(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var formdata = new FormData(document.getElementById("upload-file"));
        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: formdata,
            cache: false,
            processData: false,
            async: true,
            contentType:false,
            success: function (data) {
                console.log(data)
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $.each(data, function(i,v){
                $('#result').append('<p>'+ i + ': ' + v +'</p>');
                });
                console.log('Success!');
            },
        });
    });

});