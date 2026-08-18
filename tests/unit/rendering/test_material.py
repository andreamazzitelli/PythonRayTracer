from raytracer.rendering.material import Material


def test_default_material():
    material = Material()

    assert material.color == (1, 1, 1)
    assert material.ambient == 0.1
    assert material.diffuse == 0.9
    assert material.specular == 0.9
    assert material.shininess == 200
