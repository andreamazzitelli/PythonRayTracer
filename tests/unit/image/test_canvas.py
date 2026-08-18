from raytracer.image.canvas import Canvas, Color

def test_canvas_creation():
    c = Canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    for y in range(20):
        for x in range(10):
            assert c.pixel_at(x, y) == Color(0, 0, 0)

def test_write_pixel():
    c = Canvas(10, 20)
    red = Color(1, 0, 0)
    c.write_pixel(2, 3, red)
    assert c.pixel_at(2, 3) == red

def test_canvas_to_ppm_header():
    c = Canvas(5, 3)
    ppm = c.to_ppm()
    lines = ppm.split('\n')
    assert lines[0] == "P3"
    assert lines[1] == "5 3"
    assert lines[2] == "255"

def test_canvas_to_ppm_pixel_data():
    c = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    
    ppm = c.to_ppm()
    lines = ppm.split('\n')
    
    # Line 3 is the first line of pixel data
    assert lines[3] == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    assert lines[4] == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
    assert lines[5] == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"