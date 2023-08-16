extern crate kiss3d;

use kiss3d::light::Light;
use kiss3d::nalgebra::Translation3;
use kiss3d::scene::SceneNode;
use kiss3d::window::Window;
use rand::prelude::*;

struct Particle {
    sphere: SceneNode,
    pos: (f64, f64, f64),
    momentum: (f64, f64, f64),
}

fn main() {
    let mut window = Window::new("Kiss3d: cube");
    window.set_light(Light::StickToCamera);

    let (mut window, mut particles) = create_particles(200, window);

    let mut rng = rand::thread_rng();
    for particle in &mut particles {
        let x: f32 = rng.gen_range(0.0..=10.0); // generates a float between 0 and 10
        let y: f32 = rng.gen_range(0.0..=10.0); // generates a float between 0 and 10
        let z: f32 = rng.gen_range(0.0..=10.0); // generates a float between
        println!("{}", x);
        let t: Translation3<f32> = translate(x, y, z);
        particle.sphere.prepend_to_local_translation(&t);
    }
    while window.render() {}
}

fn translate(x: f32, y: f32, z: f32) -> Translation3<f32> {
    Translation3::new(x, y, z)
}

fn particle(sphere: SceneNode, pos: (f64, f64, f64), mom: (f64, f64, f64)) -> Particle {
    Particle {
        sphere: sphere,
        pos: pos,
        momentum: mom,
    }
}

fn create_particles(num_p: i32, mut window: Window) -> (Window, Vec<Particle>) {
    let mut particles = Vec::new();
    for i in 0..num_p {
        let sphere = window.add_sphere(1.0);
        let pos = (0.0, 0.0, 0.0);
        let mom = (0.0, 0.0, 0.0);
        let particle = particle(sphere, pos, mom);
        particles.push(particle);
        println!("Created particle {}", i);
    }
    (window, particles)
}
