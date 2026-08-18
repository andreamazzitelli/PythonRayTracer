from raytracer.image.canvas import Canvas, Color

def test_canvas_creation():
    canvas = Canvas(10, 20, Color(0, 0, 0))

    assert canvas.width == 10
    assert canvas.height == 20

    for row in canvas.pixels:
        for pixel in row:
            assert pixel == Color(0, 0, 0)

def test_canvas_default_color():
    canvas = Canvas(10, 20)

    for row in canvas.pixels:
        for pixel in row:
            assert pixel == Color(0, 0, 0)

def test_write_pixel():
    canvas = Canvas(10, 20)
    red = Color(1, 0, 0)

    canvas.write_pixel(2, 3, red)

    assert canvas.pixel_at(2, 3) == red

def test_ppm_header():
    canvas = Canvas(5, 3)

    ppm = canvas.to_ppm()
    lines = ppm.splitlines()

    assert lines[0] == "P3"
    assert lines[1] == "5 3"
    assert lines[2] == "255"

def test_ppm_pixel_data():
    canvas = Canvas(5, 3)

    canvas.write_pixel(0, 0, Color(1.0, 0.0, 0.0))
    canvas.write_pixel(2, 1, Color(0.0, 0.5, 0.0))
    canvas.write_pixel(4, 2, Color(-1.0, 0.0, 2.0))

    ppm = canvas.to_ppm()
    lines = ppm.splitlines()

    assert lines[3] == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    assert lines[4] == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
    assert lines[5] == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"