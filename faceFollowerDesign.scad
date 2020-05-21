monitor_width = 22;
monitor_height = 12;
MG996R_full_width = 55;
MG996R_full_depth = 20;
MG996R_screw_width = 7;
MG996R_screw_depth = 18;
MG996R_screw_height = 28;
screw_hole_diameter = 1;
screw_hole_height = 12;



thickness = 2;

// over monitor
cube([MG996R_full_width,
    monitor_width,
    thickness]);

// front of monitor
translate ([0,
    monitor_width,
    -monitor_height])
cube([MG996R_full_width,
    thickness,
    monitor_height + thickness]);

// back of monitor
translate ([0,
    -thickness,
    -MG996R_screw_height + thickness])
cube([MG996R_full_width,
    thickness,
    MG996R_screw_height]);

// MG996R floor
translate([0,
    -(MG996R_full_depth + 2 * thickness),
    -MG996R_screw_height + thickness])
cube([MG996R_full_width,
    MG996R_full_depth + 2 * thickness,
    thickness]);

// MG996R back
translate ([0,
    -(MG996R_full_depth + 2 * thickness),
    -MG996R_screw_height + thickness])
cube([MG996R_full_width,
    thickness,
    MG996R_screw_height]);

// MG996R right
translate ([0,
    -(MG996R_full_depth + 2 * thickness),
    -MG996R_screw_height + thickness])
cube([MG996R_screw_width,
    MG996R_full_depth + thickness,
    MG996R_screw_height]);

// MG996R left
translate ([MG996R_full_width - MG996R_screw_width,
    -(MG996R_full_depth + 2 * thickness),
    -MG996R_screw_height + thickness])
cube([MG996R_screw_width,
    MG996R_full_depth + thickness,
    MG996R_screw_height]);


