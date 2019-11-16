var shaderProgram = 0
var time = 0

function getText(path)
{
    var p = new Promise(function(resolve, reject) {
        var reader = new FileReader()
        reader.readAsText(path)
        reader.onload = function() {
            resolve(this.result)
        }
    });
    var str;
    p.then(function(result) {
        str = result;
    });
    return str;
}

function glProgram(glContext)
{
    if (shaderProgram != 0)
    {
        glContext.useProgram(shaderProgram);
        return;
    }

    var vertexShaderSource = document.getElementById("vertex-shader").text;
    var fragmentShaderSource = document.getElementById("fragment-shader").text;

    var vertShader = glContext.createShader(glContext.VERTEX_SHADER);
    glContext.shaderSource(vertShader, vertexShaderSource);
    glContext.compileShader(vertShader);
    var vertSucc = glContext.getShaderParameter(vertShader, glContext.COMPILE_STATUS);
    if (!vertSucc)
    {
        console.log("Vertex Shader Error:"+glContext.getShaderInfoLog(vertShader));
        return;
    }

    var fragShader = glContext.createShader(glContext.FRAGMENT_SHADER);
    glContext.shaderSource(fragShader, fragmentShaderSource);
    glContext.compileShader(fragShader);
    var fragSucc = glContext.getShaderParameter(fragShader, glContext.COMPILE_STATUS);
    if (!fragSucc)
    {
        console.log("Fragment Shader Error:"+glContext.getShaderInfoLog(fragShader));
        return;
    }
    
    shaderProgram = glContext.createProgram();
    glContext.attachShader(shaderProgram, vertShader);
    glContext.attachShader(shaderProgram, fragShader);
    glContext.linkProgram(shaderProgram);
    var linkSucc = glContext.getProgramParameter(shaderProgram, glContext.LINK_STATUS);
    if (!linkSucc) {
        console.log("Shader Link Error:"+glContext.getProgramInfoLog(shaderProgram));
        return;
    }
    glContext.useProgram(shaderProgram);
}

function sleep(delay) {
    var start = (new Date()).getTime();
    while ((new Date()).getTime() - start < delay) {
      continue;
    }
  }

window.onload = function () 
{
    var canvas = document.getElementById('canvas');    
    var gl = canvas.getContext('webgl');
    if (!gl) {
        console.log("Failed");
        return;
    }      

    var vertices = [
        -1.0, 1.0, 0.0,
        -1.0, -1.0, 0.0,
        1.0, -1.0, 0.0,
        1.0, 1.0, 0.0,
    ];
    var indices = [0,1,2,2,3,0];    

    var vert_buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vert_buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, null);

    var index_buf = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, index_buf);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indices), gl.STATIC_DRAW);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);
    
    gl.clearColor(0.1,0,0,0.9);
    gl.enable(gl.DEPTH_TEST);

    glProgram(gl);
    var position = gl.getAttribLocation(shaderProgram, "pos");
    var t = gl.getUniformLocation(shaderProgram, "_time");
    var resolution = gl.getUniformLocation(shaderProgram, "iResolution");
    gl.uniform2f(resolution, canvas.width, canvas.height);

    function updateFrame()
    {
        time+= 0.016;

         

        gl.bindBuffer(gl.ARRAY_BUFFER, vert_buf);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, index_buf);
        
        gl.vertexAttribPointer(position, 3, gl.FLOAT, false, 0, 0);
        gl.enableVertexAttribArray(position);
        
        gl.uniform1f(t, time);
       
        gl.clear(gl.COLOR_BUFFER_BIT);
        gl.viewport(0,0, canvas.width, canvas.height);
    
        gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT, 0);  

        requestAnimationFrame(updateFrame);
    }
    requestAnimationFrame(updateFrame);    
}