import os

from raytracer.geometry.point import Point
from raytracer.geometry.ray import Ray
from raytracer.geometry.intersection import hit
from raytracer.shapes.sphere import Sphere
from raytracer.image.canvas import Canvas, Color

def render_silhouette() -> None:
    # Ray origin (our virtual "eye")
    ray_origin = Point(0, 0, -5)
    
    # The "wall" we are projecting the shadow onto
    wall_z = 10.0
    wall_size = 7.0
    
    # Canvas resolution
    canvas_pixels = 250
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2.0
    
    canvas = Canvas(canvas_pixels, canvas_pixels)
    red = Color(1, 0, 0)
    shape = Sphere()

    print(f"Rendering {canvas_pixels}x{canvas_pixels} silhouette...")

    # Iterate through every pixel on the canvas
    for y in range(canvas_pixels):
        # Compute the world y coordinate (top = +half, bottom = -half)
        world_y = half - pixel_size * y
        
        for x in range(canvas_pixels):
            # Compute the world x coordinate (left = -half, right = +half)
            world_x = -half + pixel_size * x
            
            # Target point on the wall
            position = Point(world_x, world_y, wall_z)
            
            # The ray cast from the eye to the target on the wall
            ray_direction = (position - ray_origin).normalize()
            r = Ray(ray_origin, ray_direction)
            
            # Check for intersections
            intersections = shape.intersect(r)
            
            # If there is a hit, paint the pixel red
            if hit(intersections) is not None:
                canvas.write_pixel(x, y, red)

    # Save the output
    os.makedirs("renders", exist_ok=True)
    output_path = "renders/first_sphere.ppm"
    
    print(f"Writing image to {output_path}...")
    with open(output_path, "w") as f:
        f.write(canvas.to_ppm())
        
    print("Done!")

if __name__ == "__main__":
    render_silhouette()