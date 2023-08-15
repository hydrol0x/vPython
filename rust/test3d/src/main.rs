extern crate kiss3d;

use std::array;
use std::iter::Enumerate;

use kiss3d::nalgebra::{Vector3, UnitQuaternion, Translation3};
use kiss3d::window::{Window};
use kiss3d::scene::SceneNode;
use kiss3d::light::Light;


fn main() {
    let mut window = Window::new("Kiss3d: cube");
    let mut c      = window.add_cube(1.0,1.0,1.0);
    let mut c2      = window.add_cube(0.1,0.1,0.1);
    let mut p1 = window.add_sphere(0.5);
    let mut p2 = p1.clone();
    
    let particles = [p1,p2];

    let mut i:f32 = 0.0;

    for mut particle in particles {
        particle.set_color(0.0, 1.0, 0.0);
        let trans = translate(0.0,i,0.0);
        particle.prepend_to_local_translation(&trans);
        i+=1.0; 
    }

    window.set_light(Light::StickToCamera);

    // let rot = UnitQuaternion::from_axis_angle(&Vector3::y_axis(), 0.014);

    while window.render() {
        // c.prepend_to_local_rotation(&rot);
        let t : Translation3<f32> = translate(0.01,0.0,0.0);
        c.prepend_to_local_translation(&t);
    }
}

fn translate(x: f32,y: f32,z: f32) -> Translation3<f32> {
    Translation3::new(x,y,z)
}

fn testprint() {
    let nums = [1,2];
    for num in nums{
        println!("{}",num);
    }
}


