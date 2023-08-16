extern crate kiss3d;

use std::array;
use std::iter::Enumerate;

use kiss3d::nalgebra::{Vector3, UnitQuaternion, Translation3, ArrayStorage};
use kiss3d::window::{Window};
use kiss3d::scene::SceneNode;
use kiss3d::light::Light;


fn main() {
    let mut window = Window::new("Kiss3d: cube");
    window.set_light(Light::StickToCamera);

    create_particles(3, window);

    while window.render() {
        // c.prepend_to_local_rotation(&rot);
        // let t : Translation3<f32> = translate(0.01,0.0,0.0);
        // c.prepend_to_local_translation(&t);
    }
}

fn translate(x: f32,y: f32,z: f32) -> Translation3<f32> {
    Translation3::new(x,y,z)
}

fn create_particles(num_p: i32, mut window: Window) -> Vec<SceneNode> {
    let mut particles = Vec::new();
    for i in 1..num_p {
        let particle = window.add_sphere(1.0);
        particles.push(particle);
        println!("Created particle {}", i);
    }
    particles
}


