extern crate kiss3d;

use kiss3d::light::Light;
use kiss3d::nalgebra::{ArrayStorage, Translation3, UnitQuaternion, Vector3};
use kiss3d::scene::SceneNode;
use kiss3d::window::Window;
use rand::prelude::*;

fn main() {
    let mut window = Window::new("Kiss3d: cube");
    window.set_light(Light::StickToCamera);

    let (mut window, mut particles) = create_particles(4, window);

    let mut rng = rand::thread_rng();
    for particle in &mut particles {
        let x: f32 = rng.gen_range(0.0..=10.0); // generates a float between 0 and 10
        let y: f32 = rng.gen_range(0.0..=10.0); // generates a float between 0 and 10
        let z: f32 = rng.gen_range(0.0..=10.0); // generates a float between
        println!("{}", x);
        let t: Translation3<f32> = translate(x, y, z);
        particle.prepend_to_local_translation(&t);
    }
    while window.render() {}
}

fn translate(x: f32, y: f32, z: f32) -> Translation3<f32> {
    Translation3::new(x, y, z)
}

fn create_particles(num_p: i32, mut window: Window) -> (Window, Vec<SceneNode>) {
    let mut particles = Vec::new();
    for i in 0..num_p {
        let particle = window.add_sphere(1.0);
        particles.push(particle);
        println!("Created particle {}", i);
    }
    (window, particles)
}
