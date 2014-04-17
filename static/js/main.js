$(function() {

    NProgress.configure({ 
        minimum: 0,
        trickle: false
    });

    function handleFiles(files) {
        var formData = new FormData();
        for (var i = 0; i < files.length; i++) {
            formData.append('file', files[i]);
            showUploadUI(files[i]);
        }
        formData.append('token', '');
        upload(formData);
    }

    function render(tmpl_selector, data) {
        return Mustache.render($(tmpl_selector).html(), data);
    }

    function showUploadUI(file) {
        var html = render('#upload-ui-tmpl', file);
        $('#dropzone').html(html);
    }

    function showResultUI(result) {
        var html = Mustache.render('#result-ui-tmpl', result);
    }

    function upload(formData) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                if (xhr.status == 200) {
                    NProgress.done();
                    showResultUI(JSON.parse(xhr.responseText));
                }
                else{
                    NProgress.remove();
                    alert('上传失败');
                }
            }
        };
        xhr.upload.onprogress = function (event) {
            if (event.lengthComputable) {
                var percent = event.loaded / event.total;
                NProgress.set(percent);
            }
        };
        xhr.open('POST', 'http://up.qiniu.com', true);
        xhr.send(formData);

        NProgress.start();
    }


    var dropzone = $('#dropzone');

    dropzone.on('dragover', function(event) {
        event.preventDefault();  
        event.stopPropagation();
        $(this).addClass('hover');
    });
    dropzone.on('dragend', function(event) {
        event.preventDefault();  
        event.stopPropagation();
        $(this).removeClass('hover');
    });
    dropzone.on('dragleave', function(event) {
        event.preventDefault();  
        event.stopPropagation();
        $(this).removeClass('hover');
    });
    dropzone.on('drop', function(event) {
        event.preventDefault();
        event.stopPropagation();
        $(this).removeClass('hover');
        handleFiles(event.originalEvent.dataTransfer.files);
    });

});
