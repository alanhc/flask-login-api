let login;

function setup() {
    createCanvas(400, 400);

    button = createButton('login');
    button.position(19, 19);
    button.mousePressed(() => {
        let url = 'http://127.0.0.1:5000/';
        location.replace(url);
    })
    print(sessionStorage.getItem('login'))
}

function draw() {
    background(220);
    
    
    text("test", 10, 100);
}

