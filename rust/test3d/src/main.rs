extern crate kiss3d;

use kiss3d::light::Light;
use kiss3d::nalgebra::{Translation3, Vector3};
use kiss3d::scene::SceneNode;
use kiss3d::window::Window;
use rand::prelude::*;
use std::cmp;
use std::thread::sleep;
use std::time::{Duration, Instant};

struct Particle {
    sphere: SceneNode,
    pos: Vector3<f32>,
    momentum: Vector3<f32>,
    mass: f32,
}

fn main() {
    let mut window = Window::new("Kiss3d: cube");
    window.set_light(Light::StickToCamera);
    let (mut window, mut particles) = create_particles(5, window);

    let mut rng = rand::thread_rng();
    for particle in &mut particles {
        let x: f32 = rng.gen_range(0.0..=10.0); // generates a float between 0 and 10
        let y: f32 = rng.gen_range(0.0..=10.0); // generates a float between 0 and 10
        let z: f32 = rng.gen_range(0.0..=10.0); // generates a float between
        let px: f32 = rng.gen_range(5.0..=10.0); // generates a float between 0 and 10
        let py: f32 = rng.gen_range(5.0..=10.0); // generates a float between 0 and 10
        let pz: f32 = rng.gen_range(5.0..=10.0); // generates a float between
        translate(particle, x, y, z);
        particle.momentum = Vector3::new(px, py, pz);
    }

    const dt: f32 = 0.01;
    // const dt: f32 = 1.0;
    const iters_per_sec: f32 = 60.0;
    let time_interval = Duration::from_secs_f32(1.0 / iters_per_sec);

    let mut previous_time = Instant::now();
    let mut accumulator: Duration = Duration::from_millis(0);

    while window.render() {
        let current_time = Instant::now();
        let elapsed_time = current_time - previous_time;
        previous_time = current_time;

        accumulator += elapsed_time;

        while accumulator >= time_interval {
            for particle in &mut particles {
                let dx = (particle.momentum.x / particle.mass) * dt;
                let dy = (particle.momentum.y / particle.mass) * dt;
                let dz = (particle.momentum.z / particle.mass) * dt;
                translate(particle, dx, dy, dz);
                // println!("{}", particle.pos.magnitude());
                if (particle.pos.magnitude() >= 0.2) {
                    particle.momentum = -particle.momentum; // figure out how to bound them
                }
            }

            accumulator -= time_interval;
        }
        sleep(cmp::max(
            Duration::from_secs(0),
            time_interval - (Instant::now() - current_time),
        ));
    }
}

fn translate(particle: &mut Particle, x: f32, y: f32, z: f32) {
    particle.pos = Vector3::new(x, y, z);
    let t = Translation3::new(x, y, z);
    particle.sphere.prepend_to_local_translation(&t);
}

fn particle(sphere: SceneNode, pos: (f32, f32, f32), mom: (f32, f32, f32), mass: f32) -> Particle {
    let position: Vector3<f32> = Vector3::new(pos.0, pos.1, pos.2);
    let momentum: Vector3<f32> = Vector3::new(mom.0, mom.1, mom.2);
    Particle {
        sphere: sphere,
        pos: position,
        momentum: momentum,
        mass: mass,
    }
}

fn create_particles(num_p: i32, mut window: Window) -> (Window, Vec<Particle>) {
    let mut particles = Vec::new();
    for i in 0..num_p {
        let sphere = window.add_sphere(1.0);
        let pos = (0.0, 0.0, 0.0);
        let mom = (0.0, 0.0, 0.0);
        let mass = 1.0;
        let particle = particle(sphere, pos, mom, mass);
        particles.push(particle);
        println!("Created particle {}", i);
    }
    (window, particles)
}

fn grav_force(particle1: &Particle, particle2: &Particle) -> Vector3<f32> {
    // Gmm/r^2
    const G: f32 = 1.0;
    let r = particle2.pos - particle1.pos;
    // print!("distance {}", r.norm());
    let rhat = r / r.norm(); // Orient the force vector
    let force = (G * particle1.mass * particle2.mass) / f32::powf(r.magnitude(), 2.0);
    println!("force {}", force);
    rhat * force
}

fn apply_impulse(particle: &mut Particle, force: Vector3<f32>, dt: f32) {
    let imp = force * dt;
    particle.momentum += imp;
    // particle.momentum
}
