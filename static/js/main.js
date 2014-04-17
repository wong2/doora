(function() {

    Dropzone.options.dropzone = {
        method: 'post',
        maxFilesize: 20,
        init: function() {
            this.on('sending', function(file, xhr, formData) {
                formData.append('token', UP_TOKEN);
            });
            this.on('success', function(file, resp) {
                showResultPanel(resp.download_url);
            });
            this.on('reset', function() {
            });
        }
    };

    function showResultPanel(download_url) {
        var tmpl = $('#result-panel-tmpl').html(),
            html = tmpl.replace('${download_url}', download_url);

        $('#dropzone').append(html);
        $('.download-url').focus().select();

        renderQRCode(download_url);

        $('.dz-preview').animate({
            width: '700px',
            height: '330px'
        });
    }

    function renderQRCode(url) {
        $('#qrcode-container').qrcode({
            text: url,
            width: 250,
            height: 250
        });
    }

})();
